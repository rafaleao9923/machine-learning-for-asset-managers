import requests
from bs4 import BeautifulSoup
import html2text

# Step 1: Fetch the HTML content
url = 'https://example.com'
response = requests.get(url)
html_content = response.text

# Step 2: Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Convert HTML to Markdown
markdown_converter = html2text.HTML2Text()
markdown_converter.ignore_links = False
markdown_content = markdown_converter.handle(soup.prettify())

# Step 4: Save or use the Markdown content
with open('output.md', 'w') as md_file:
    md_file.write(markdown_content)

print("Markdown content saved to output.md")