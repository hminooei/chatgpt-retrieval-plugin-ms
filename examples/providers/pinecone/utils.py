from bs4 import BeautifulSoup
import html2text

def html_to_md(local_link, output_folder):
    with open(local_link, 'r') as html_file:
        index = html_file.read()
        text = html2text.html2text(index)
        with open(f"{output_folder}/{local_link.replace('/', '_')}.md", 'w') as md_file:
            md_file.write(text)
    return
        