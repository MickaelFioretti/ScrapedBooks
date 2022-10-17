import requests
from bs4 import BeautifulSoup
import csv

# function
from function.GetBook import GetBooks

linksCategory = []
linksBook = []
sample_csv = "./sample.csv"


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

GetBooks(url)

if response.ok:
    soup = BeautifulSoup(response.text, "lxml")
    article = soup.find("article", {"class": "product_page"})
    ul = soup.find("ul", {"class": "breadcrumb"})
    table = article.find("table", {"class": "table table-striped"})
    td = table.findAll("td")
    review_rating = (
        soup.find("div", {"class": "col-sm-6 product_main"})
        .find("p", {"class": "star-rating"})
        .attrs["class"][1]
    )

    universal_product_code = str(td[0])[4:-5]
    title = article.find("h1").contents
    price_including_tax = str(td[3])[4:-5]
    price_excluding_tax = str(td[2])[4:-5]
    number_available = str(td[5])[4:-5]
    product_description = article.find("p", {"class": ""}).contents
    category = ul.findAll("li")[2].find("a").contents[0]
    image_url = soup.find("div", {"class": "item active"}).find("img").attrs["src"][6:]

# function pour get les data du site
# print(len(linksCategory))
# print(linksBook[0][9:])


header = [
    "product_page_url",
    "universal_product_code",
    "title",
    "price_including_tax",
    "price_excluding_tax",
    "number_available",
    "product_description",
    "category",
    "review_rating",
    "image_url",
]


with open(sample_csv, "w", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(header)
    writer.writerow(
        [
            url,
            universal_product_code,
            title,
            price_including_tax,
            price_excluding_tax,
            number_available,
            product_description,
            category,
            review_rating,
            image_url,
        ]
    )

# with open(sample_csv, "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)
