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

print("Links category ok !")

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

print("Links book ok !")

# Pour chaque url dans linksBook execute GetBooks et rajoute les data dans un fichier csv
with open(sample_csv, "w", newline="") as csvfile:
    fieldnames = [
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
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(fieldnames)
    print("CSV file inprogress ...")
    for link in linksBook:
        url = f"http://books.toscrape.com/catalogue/{link[9:]}"
        book = GetBooks(url)
        writer.writerow(
            [
                book["product_page_url"],
                book["universal_product_code"],
                book["title"],
                book["price_including_tax"],
                book["price_excluding_tax"],
                book["number_available"],
                book["product_description"],
                book["category"],
                book["review_rating"],
                book["image_url"],
            ]
        )

print("CSV file ok !")
