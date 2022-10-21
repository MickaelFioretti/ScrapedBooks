import requests
import shutil
import re
import string


def GetImageBook(link, title):
    url = f"http://books.toscrape.com/{link}"
    # replace special character
    motif = r"[" + string.punctuation + "]"
    title = re.sub(motif, "", title)
    title = title.replace(" ", "_")
    title = title[:50]
    response = requests.get(url, stream=True)
    if response.ok:
        with open(f"./images/{title}.jpg", "wb") as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)
    else:
        print("Error in download")
