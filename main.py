import requests
from bs4 import BeautifulSoup

links = []

url = "http://books.toscrape.com/"
response = requests.get(url)

if response.ok:
    # Get all information of html page
    soup = BeautifulSoup(response.text, "lxml")
    # Get the only ul with the class "nav nav-list"
    ul = soup.find("ul", {"class": "nav nav-list"})
    # Get all tags in previous ul
    lis = ul.findAll("li")

    # Get all link in the tag
    for li in lis:
        a = li.find("a")
        link = a["href"]
        links.append(f"{url}{link}")

print(links[1])
