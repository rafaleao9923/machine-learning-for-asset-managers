#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from typing import Union, List
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def convert_notebook_to_python(notebook_path: Union[str, Path], output_path: Union[str, Path, None] = None) -> Path:
    """Convert a single Jupyter notebook to a Python file.
    
    Args:
        notebook_path: Path to the input notebook file
        output_path: Optional custom output path for the Python file
        
    Returns:
        Path to the generated Python file
    
    Raises:
        FileNotFoundError: If notebook file doesn't exist
        json.JSONDecodeError: If notebook is invalid JSON
    """
    notebook_path = Path(notebook_path).resolve()
    if not notebook_path.exists():
        raise FileNotFoundError(f"Notebook not found: {notebook_path}")
    
    output_path = Path(output_path) if output_path else notebook_path.with_suffix('.py')
    
    with notebook_path.open('r', encoding='utf-8') as f:
        try:
            notebook = json.load(f)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid notebook format in {notebook_path}: {str(e)}", e.doc, e.pos)
    
    python_code = []
    
    # Add header with source notebook information
    python_code.extend([
        f"# Generated from: {notebook_path.name}",
        "# Warning: This is an auto-generated file. Changes may be overwritten.\n"
    ])
    
    for cell in notebook.get('cells', []):
        if cell['cell_type'] == 'code':
            source = ''.join(cell.get('source', []))
            if source.strip():
                python_code.append(source)
                python_code.append('\n')
        
        elif cell['cell_type'] == 'markdown':
            source = ''.join(cell.get('source', []))
            if source.strip():
                commented_lines = [f'# {line}' if line.strip() else '#'
                                 for line in source.splitlines()]
                python_code.extend(commented_lines)
                python_code.append('\n')
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text('\n'.join(python_code), encoding='utf-8')
    return output_path

def process_directory(directory_path: Union[str, Path]) -> List[Path]:
    """Process all Jupyter notebooks in a directory and convert them to Python files.
    
    Args:
        directory_path: Path to directory containing notebooks
        
    Returns:
        List of paths to generated Python files
    """
    directory_path = Path(directory_path).resolve()
    if not directory_path.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory_path}")
    
    converted_files = []
    for notebook_path in directory_path.glob('**/*.ipynb'):
        if '.ipynb_checkpoints' in notebook_path.parts:
            continue
            
        try:
            output_path = convert_notebook_to_python(notebook_path)
            converted_files.append(output_path)
            logger.info(f"Converted {notebook_path.name} → {output_path.name}")
        except Exception as e:
            logger.error(f"Failed to convert {notebook_path.name}: {str(e)}")
            
    return converted_files

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    
    try:
        directory_path = sys.argv[1]
        converted_files = process_directory(directory_path)
        logger.info(f"Successfully converted {len(converted_files)} notebooks")
    except Exception as e:
        logger.error(f"Error processing directory: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()