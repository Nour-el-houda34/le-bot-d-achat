#install Selenium (pip install selenium et installer selenium-stealth)
#pip install selenium-stealth :
import re
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random  # pour generer des nbs aleatoires
#importer the fonctionnalities de la gestion du temps
import time
from selenium import webdriver #pouvoir creer une instance de navigateur webdriver pour interagir avec le navigateur
from bs4 import BeautifulSoup
import random
from selenium.webdriver.support.wait import WebDriverWait 
#pour attendre qu'une condition soit satisfaite avant de poursuivre l'execution du script Selenium
from selenium.webdriver.support.ui import Select #afin d'interagir avec <select>
from selenium.common.exceptions import NoSuchElementException #si Selenium ne trouve pas un element sur lw website
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys #cette classe fournit une serie de cst pour les cle du clavier

def buy_from_jumia(produit):
 chrome_options = webdriver.ChromeOptions() #to create an instace of ChromeOptions in Selenium
 chrome_options.add_argument("--profile-directory=Nourelhouda")
 chrome_options.add_experimental_option('useAutomationExtension', False) #to mask that we're using automating tools
 chrome_options.add_argument("disable-popup-blocking")
 chrome_options.add_argument('--ignore-ssl-errors=yes')
 chrome_options.add_argument('--ignore-certificate-errors')
 chrome_options.add_argument("--enable-javascript")
 chrome_options.add_argument("--disable-popup-blocking") #désactiver le blocage des pop-ups
 
 chrome_options.add_argument('log-level=3')
 driver = webdriver.Chrome('\\Users\\NourElhouda\\Desktop\\chromedriver-win64\\chromedriver')
 stealth(driver,
        languages=["en-US", "en","fr"],
        vendor="Google Inc.",
        platform="Win64",   #wind+R ->msinfo32+enter ->if System-type x64-based PC ?64 version of win: 32..
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True, 
        )
 
 driver.get("https://www.jumia.ma/")
 time.sleep(3)
 bouton_fermeture = driver.find_element(By.CSS_SELECTOR, "#pop > div > section > button > svg > use")
 bouton_fermeture.click()
 time.sleep(2)
 driver.find_element(By.CSS_SELECTOR, "#jm > div.banner-pop > button > span > svg").click()
 time.sleep(2)
 search=driver.find_element(By.CSS_SELECTOR, "[placeholder='Cherchez un produit, une marque ou une catégorie']")

 time.sleep(3)
 search.click()  #pour selectionner
 search.clear() #si on a deja an existing text 
 time.sleep(2)
 for i in produit :
    search.send_keys(i)
    time.sleep(random.uniform(0,0.5)) #slight delay entre chaque keystroke

 time.sleep(2)
 rechercher = driver.find_element(By.CSS_SELECTOR, ".btn._prim._md.-mls.-fsh0")
 rechercher.click()
 time.sleep(5)
 
 while True:
     html_content=driver.page_source
     soup=BeautifulSoup(html_content,'lxml')
     les_produits=soup.find_all("div",class_="-paxs row _no-g _4cl-3cm-shs")
     cheapest_nom=None
     cheapest_prix=float('inf') #thsi means that no price is cheaper than this
     produit_trouve = False
     for article in les_produits:
       try:
        nom_produit=article.find("h3",class_="name").get_text().strip()
        prix_produit=article.find("div",class_="prc").get_text().strip()
        prix_produit=float(re.sub(r'[^\d.]', '',prix_produit))
        if prix_produit<cheapest_prix:
            cheapest_nom=nom_produit
            cheapest_prix=prix_produit
            produit_trouve=True   #pour que le code ne passe pas a la page suivante
       except AttributeError:            # if an attribute reference or assignment fails
        continue
     
     if not produit_trouve:
        next_page = driver.find_element(By.CSS_SELECTOR, "a.pg[aria-label='Page suivante']")
        next_page_URL = next_page.get_attribute("href")

        if not next_page_URL:
            break
        # Go to the next page
        driver.get(next_page_URL)
        time.sleep(5)
     else:
        # If the product is found on the current page, exit the loop
        break
 return driver,cheapest_nom,cheapest_prix


 

  
# element=driver.find_element(By.XPATH,f"//h3[contains(text(), '{cheapest_nom}')]")

 