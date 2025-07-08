#Proyecto para books toscrape, se consigue: título, precio, stock y valoración.
import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
book_list = []

for page in range(1, 6):  # páginas 1 a 5
    url = base_url.format(page)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one("p.price_color").text
        stock = book.select_one("p.instock.availability").text.strip()
        star_rating_class = book.select_one("p.star-rating")["class"]
        rating_word = [c for c in star_rating_class if c != "star-rating"][0]
        ratings_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
        rating = ratings_map.get(rating_word, 0)

        book_list.append({
            "Título": title,
            "Precio": price,
            "Disponibilidad": stock,
            "Valoración": rating
        })

df = pd.DataFrame(book_list)
df.to_excel("books_100.xlsx", index=False, engine="openpyxl")

print("Datos guardados en books_100.xlsx")