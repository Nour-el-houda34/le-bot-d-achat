from bs4 import BeautifulSoup
import requests
import re 

def buy_from_ultraPC(produit):
    URL = 'https://www.ultrapc.ma/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    produits = soup.find_all("div", class_="product-card")
    cheapest_nom = None
    cheapest_prix = float('inf')  
    produit_trouve = False  

    for product in produits:
        nom_produit = product.find("div", class_="product-name").get_text().strip()
        prix_produit = product.find("div", class_="price").get_text().strip()
        prix_produit = float(re.sub(r'[^\d.]', '', prix_produit))
        if prix_produit < cheapest_prix:
            cheapest_nom = nom_produit
            cheapest_prix = prix_produit
            produit_trouve = True

    return cheapest_nom, cheapest_prix
