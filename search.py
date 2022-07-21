from bs4 import BeautifulSoup

import requests

import re

query = input("What is your query? ")

url = requests.get("https://www.ncbi.nlm.nih.gov/pmc/?term=" + query)

soup = BeautifulSoup(url.content, "html.parser")

title = soup.prettify()

with open(f"./search_results/{query}.html", "w") as f:
    for line in title:
        f.write(line)
