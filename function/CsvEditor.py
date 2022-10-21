import csv

# function
from function.GetBook import GetBooks

# csv file
sample_csv = "./sample.csv"

# Pour chaque url dans linksBook execute GetBooks et rajoute les data dans un fichier csv
def CsvEditor(link):
    with open(sample_csv, "+a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
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
