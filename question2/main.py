from lxml import html
import requests
from lxml.html.soupparser import fromstring

response = requests.get("https://www.mg-cc.org/club-information/club-contacts")

html = fromstring(response.text)
a_tags = html.xpath("//a[starts-with(@href, 'mailto:')]")
a_tags = [ a.text_content().strip() for a in a_tags ]

print(a_tags)