from selenium import webdriver
from selenium.webdriver.common.by import By
from amazoncaptcha import AmazonCaptcha
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
import random
from selenium.webdriver.support import expected_conditions as EC
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import re #to remove non digit characters
#new things
def buy_from_Amazon(produit):
  options = Options()
  options.add_argument("user-agent'='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
  webdriver_service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome('\\Users\\NourElhouda\\Desktop\\chromedriver-win64\\chromedriver')

#to solve captcha
#driver = webdriver.Chrome()
  driver.get("https://www.amazon.com/errors/validateCaptcha")
  image=driver.find_element(By.XPATH,"//div[@class= 'a-row a-text-center']//img").get_attribute('src')
  captcha =AmazonCaptcha.fromlink(image)

  valeur_de_captcha=AmazonCaptcha.solve(captcha)
  inserer=driver.find_element(By.ID,"captchacharacters").send_keys(valeur_de_captcha)
  continuer=driver.find_element(By.CLASS_NAME,"a-button-text").click()
  time.sleep(5)
  driver.find_element(By.CLASS_NAME, 'icp-nav-link-inner').click()
  time.sleep(5)
  wait = WebDriverWait(driver, 10)
  dropdown_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.a-button-text.a-declarative')))
  actions = ActionChains(driver)
  actions.move_to_element(dropdown_button).click().perform()
  time.sleep(2)
  desired_option = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@id="icp-currency-dropdown_52"]')))
  desired_option.click()
  time.sleep(3)
  save_button = driver.find_element(By.XPATH, "//input[@aria-labelledby='icp-save-button-announce']")
  actions = ActionChains(driver)
  actions.move_to_element(save_button).perform()
  save_button.click()
  #new for currency
  '''driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us.icp-nav-flag-lop').click()
  driver.find_element(By.CSS_SELECTOR, '.a-dropdown-prompt').click()
  wait = WebDriverWait(driver, 10)  #for the currency
  element3 = wait.until(EC.element_to_be_clickable((By.ID, 'icp-currency-dropdown_52')))
  element3.click()
  driver.find_element(By.CSS_SELECTOR, '.a-button-input[type="submit"]').click()
  driver.find_element(By.CSS_SELECTOR, '.nav-logo-link.nav-progressive-attribute').click()'''
  time.sleep(4)




  search=driver.find_element(By.ID,"twotabsearchtextbox")
  search.click()
  search.clear() #si on a deja an existing text 
  time.sleep(1)

  for i in produit:
     try:
        search.send_keys(i)
        time.sleep(random.uniform(0, 0.5))  # slight delay between each keystroke
     except StaleElementReferenceException:
        # If the element becomes stale, refresh the reference and retry sending keys
        search = driver.find_element(By.ID, "twotabsearchtextbox")
        search.send_keys(i)
        time.sleep(random.uniform(0, 0.5))  # slight delay between each keystroke

# Submit the search query
  search.submit()
  go=driver.find_element(By.ID,"nav-search-submit-button").click()
  time.sleep(10)

#beautifulsoup to get the data
# i think it's not necessary :  page_courrante=driver.current_url
  while True:
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'lxml')
    les_produits = soup.find_all("div", class_="sg-col-inner")
    cheapest_nom = None
    cheapest_prix = float('inf')  # this means that no price is cheaper than this
    produit_trouve = False  # Flag to indicate if the product is found on the page

    for article in les_produits:
        try:
            nom_produit = article.find("span", class_="a-size-base-plus a-color-base a-text-normal").get_text().strip()
            prix_produit = article.find("span", class_="a-price-whole").get_text().strip()
            prix_produit = float(re.sub(r'[^\d.]', '', prix_produit))
            if prix_produit < cheapest_prix:
                cheapest_nom = nom_produit
                cheapest_prix = prix_produit
                produit_trouve = True  # Set the flag to True if a product is found
        except AttributeError:  # if an attribute reference or assignment fails
            continue

    # If the product is found on the current page, exit the loop
    if produit_trouve:
        break
    else:
        # If the product is not found on the current page, proceed to the next page
        next_page = driver.find_element(By.CLASS_NAME, "s-pagination-next")
        next_page_URL = next_page.get_attribute("href")

        if not next_page_URL:
            break
        # Go to the next page
        driver.get(next_page_URL)
        time.sleep(5)

  return driver, cheapest_nom, cheapest_prix

  






































  '''
  while True:
    html_content=driver.page_source
    soup=BeautifulSoup(html_content,'lxml')
    les_produits=soup.find_all("div",class_="sg-col-inner")
    cheapest_nom=None
    cheapest_prix=float('inf') #thsi means that no price is cheaper than this
    produit_trouve = False  # Flag to indicate if the product is found on the page
    for article in les_produits:
        try:
            nom_produit=article.find("span",class_="a-size-base-plus a-color-base a-text-normal").get_text().strip()
            prix_produit=article.find("span",class_="a-price-whole").get_text().strip()
            prix_produit=float(re.sub(r'[^\d.]', '',prix_produit))
            if prix_produit<cheapest_prix:
               cheapest_nom=nom_produit
               cheapest_prix=prix_produit
        except AttributeError:            # if an attribute reference or assignment fails
           continue
# If the product is not found on the current page, proceed to the next page
    if not produit_trouve:
        next_page = driver.find_element(By.CLASS_NAME, "s-pagination-next")
        next_page_URL = next_page.get_attribute("href")

        if not next_page_URL:
            break
        # Go to the next page
        driver.get(next_page_URL)
        time.sleep(5)
    else:
        # If the product is found on the current page, exit the loop
        break

  return driver,cheapest_nom,cheapest_prix '''
                                                                            









