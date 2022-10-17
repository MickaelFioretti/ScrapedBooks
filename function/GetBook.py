from bs4 import BeautifulSoup
import requests


"""
Function for get all data from book
"""


def GetBooks(url):
    response = requests.get(url)
    # get all data from book page
    soup = BeautifulSoup(response.text, "lxml")

    product_page_url = url
    universal_product_code = soup.find("table", {"class": "table table-striped"})

    return print(universal_product_code)
