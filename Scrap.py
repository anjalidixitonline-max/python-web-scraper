import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

title = soup.find("title")
print(title.text)
# --- Change these lines ---

# Find ALL the tags that hold the author names
author_tags = soup.find_all("small", class_="author")

# Loop through the list and print the text of each one
for author in author_tags:
    print(author.text)

