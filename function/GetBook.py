from bs4 import BeautifulSoup
import requests


"""
Function for get all data from book
"""


def GetBooks(url):
    response = requests.get(url)
    # get all data from book page
    soup = BeautifulSoup(response.text, "lxml")

    book = {
        "product_page_url": url,
        "universal_product_code": (
            soup.find("table", {"class": "table table-striped"})
            .findAll("td")[0]
            .contents[0]
        ),
        "title": soup.find("h1").contents[0],
        "price_including_tax": (
            soup.find("table", {"class": "table table-striped"})
            .findAll("td")[3]
            .contents[0]
        ),
        "price_excluding_tax": (
            soup.find("table", {"class": "table table-striped"})
            .findAll("td")[2]
            .contents[0]
        ),
        "number_available": (
            soup.find("table", {"class": "table table-striped"})
            .findAll("td")[5]
            .contents[0]
        ),
        "product_description": soup.findAll("p")[3].contents[0],
        "category": soup.findAll("a")[3].contents[0],
        "review_rating": (
            soup.find("div", {"class": "col-sm-6 product_main"})
            .find("p", {"class": "star-rating"})
            .attrs["class"][1]
        ),
        "image_url": soup.find("div", {"class": "item active"})
        .find("img")
        .attrs["src"][6:],
    }

    return book
