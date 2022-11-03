import csv
import requests
from bs4 import BeautifulSoup

# function
from function.CsvEditor import CsvEditor

links_category = []
links_book = []
SAPLE_CSV = "./sample.csv"

print("Start")

URL = "http://books.toscrape.com/"
response = requests.get(URL)

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
        links_category.append(f"{URL}{link}")

print("Links category ok !")

# Remove the first link because it's not a category
links_category.pop(0)

# Write the header of csv file
with open(SAPLE_CSV, "w", newline="", encoding="utf-8") as csvfile:
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

print("Header ok !")

print("Start scraping...")

# for each link in linksCategory get all links of books
for URL in links_category:
    response = requests.get(URL)
    category_link = URL[:-10]
    # Get all books in the category and check if next page is available if yes => loop
    while response.ok:
        soup = BeautifulSoup(response.text, "lxml")
        ol = soup.find("ol", {"class": "row"})
        h3s = ol.findAll("h3")

        for h3 in h3s:
            a = h3.find("a")
            link = a["href"]
            CsvEditor(link)

        next = soup.find("li", {"class": "next"})
        if next:
            a = next.find("a")
            link = a["href"]
            URL = f"{category_link}{link}"
            response = requests.get(URL)
        else:
            break

print("End")
