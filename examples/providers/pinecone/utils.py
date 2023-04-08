from bs4 import BeautifulSoup
import html2text

def html_to_md(local_path, output_folder):
    with open(local_path, 'r') as html_file:
        index = html_file.read()
        text = html2text.html2text(index)
        with open(f"{output_folder}/{local_path.replace('/', '_')}.md", 'w') as md_file:
            md_file.write(text)
    return

def truncate_mulesoft_site_md_pages(local_path):
    with open(local_path, "r+") as f:
        text = f.read()
        f.seek(0)
        try:
            start = text.index("(C)2022 MuleSoft, LLC")+len("(C)2022 MuleSoft, LLC")
        except:
            start = 0
        try:
            end = text.index("## See Also")
        except:
            try: 
                end = text.index("Submit your feedback!")
            except:
                end = len(text)
        f.write(text[start:end], )
        f.truncate()