#!/usr/bin/env python3
import json
import sys
from pathlib import Path

def convert_notebook_to_python(notebook_path, output_path=None):
    notebook_path = Path(notebook_path).resolve()
    
    if output_path:
        output_path = notebook_path.parent / output_path
    else:
        output_path = notebook_path.parent / f"{notebook_path.stem}.py"
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    python_code = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if source.strip():
                python_code.append(source)
                python_code.append('\n')
        
        elif cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            if source.strip():
                commented_lines = [f'# {line}' if line.strip() else '#'
                                 for line in source.splitlines()]
                python_code.extend(commented_lines)
                python_code.append('\n')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(python_code))
    
    return output_path

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <notebook.ipynb> [output.py]")
        sys.exit(1)
    
    notebook_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        output_file = convert_notebook_to_python(notebook_path, output_path)
        print(f"Successfully converted {notebook_path} to {output_file}")
    except Exception as e:
        print(f"Error converting notebook: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()