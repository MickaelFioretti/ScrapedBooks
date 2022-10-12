import requests
from bs4 import BeautifulSoup

linksCategory = []
linksBook = []

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
        linksCategory.append(f"{url}{link}")

url = linksCategory[1]
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, "lxml")
    ol = soup.find("ol")
    lis = ol.findAll("li")

    for li in lis:
        a = li.find("a")
        link = a["href"]
        linksBook.append(f"{link}")


url = f"http://books.toscrape.com/catalogue/{linksBook[0][9:]}"
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, "lxml")
    article = soup.find("article", {"class": "product_page"})
    h1 = article.find("h1")
    p = article.find("p", {"class": ""})
    allInfo = f"page_url : {url} \ntitle : {str(h1)[4:-5]} \nprice : \ndescription : {str(p)[3:-4]}"

# function pour get les data du site
# print(len(linksCategory))
# print(linksBook[0][9:])
print(allInfo)
