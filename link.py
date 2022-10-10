import httplib2
import requests
from bs4 import BeautifulSoup, SoupStrainer

array_links = []
pagenumber = 1


def linkcall(pagenumber):
    http = httplib2.Http()
    status, response = http.request(
        "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page="
        + str(pagenumber)
    )

    for link in BeautifulSoup(
        response, parse_only=SoupStrainer("a"), features="html.parser"
    ):
        if link.has_attr("href") and "product" in link["href"]:
            array_links.append("https://webscraper.io" + link["href"])


for x in range(1, 21):
    linkcall(x)
for x in array_links:
    print(x)
    print("\n")
