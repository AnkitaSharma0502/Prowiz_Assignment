
# A html parser

html_doc = """
<html><head><title>The Dormouse's story</title></head><body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their
names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# parsing html text as string
from bs4 import BeautifulSoup as bs

soup = bs(html_doc, "html.parser")

# B 1) all href links

for i in soup.find_all("a"):
    print("Link ",i.get("href"))

#   2) all class values for <a> tag

for i in soup.find_all("a"):
    print("Class ",i.get("class"))

#   3) using regex and recurion to get href links and <a> tag

import re 

pattern_1=r'<a[^>]*href="(.*?)"' # for href

pattern_2=r'<a[^>]*class="(.*?)"' # for a tag

def extract_content(text,pattern):

    match=re.search(pattern,text)

    if not match:
        return[]

    value=match.group(1)

    remaining=text[match.end():]

    return[value]+extract_content(remaining,pattern)

links = extract_content(html_doc, pattern_1)
classes = extract_content(html_doc, pattern_2)

print("Links:", links)
print("Classes:", classes)