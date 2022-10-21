import requests
from bs4 import BeautifulSoup
import csv

# function
from function.CsvEditor import CsvEditor

linksCategory = []
linksBook = []
sample_csv = "./sample.csv"

print("Start")

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

# Remove the first link because it's not a category
linksCategory.pop(0)

# Write the header of csv file
with open(sample_csv, "w", newline="", encoding="utf-8") as csvfile:
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

# for each link in linksCategory get all links of books
for url in linksCategory:
    response = requests.get(url)
    categoryLink = url[:-10]
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
            url = f"{categoryLink}{link}"
            response = requests.get(url)
        else:
            break
