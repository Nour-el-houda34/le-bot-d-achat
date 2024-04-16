
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
from selenium.webdriver.common.keys import Keys




import threading
from Amazon import buy_from_Amazon
from Jumiaa import buy_from_jumia
produit=input("Veuillez saisir le produit: ")
def buy_jumia():
   try:
      global driver_Jumia, produit_Jumia, prix_Jumia
      driver_Jumia,produit_Jumia,prix_Jumia=buy_from_jumia(produit)
   except Exception as e:
       print(f"An error occurred: {e}")
def buy_amazon():  #global pour pouvoir utiliser les var dans if else..
   global driver_Amazon, produit_Amazon, prix_Amazon
   driver_Amazon,produit_Amazon, prix_Amazon=buy_from_Amazon(produit)

    
    

t1=threading.Thread(target=buy_jumia)
t2=threading.Thread(target=buy_amazon)

t1.start()
t2.start()

t1.join()
t2.join()

    # Comparer les and buy the cheapest product
if prix_Amazon >= prix_Jumia :
        driver_Amazon.quit()
        print('Depuis le site Jumia: ',prix_Jumia,produit_Jumia)
        
        element = WebDriverWait(driver_Jumia, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//h3[contains(text(), '{produit_Jumia}')]"))
        )
        driver_Jumia.execute_script("arguments[0].click();", element)
        time.sleep(5)
        bouton = driver_Jumia.find_element(By.CSS_SELECTOR, ".add.btn._prim.-pea._i.-fw")
        driver_Jumia.execute_script("arguments[0].click();", bouton)
        time.sleep(10)
        
        
        
else:   
        driver_Jumia.quit()
        print('Depuis le site Amazon',prix_Amazon,produit_Amazon)
        
        driver_Amazon.find_element(By.XPATH, f'//span[contains(text(), "{produit_Amazon}")]').click()
        time.sleep(2)
        driver_Amazon.find_element(By.ID,"buy-now-button").click()
        time.sleep(2)
        email = WebDriverWait(driver_Amazon, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ap_email"]')))
        for i in "Botl04796@gmail.com":
           email.send_keys(i)
           time.sleep(random.uniform(0,0.5)) #slight delay entre chaque keystroke
        driver_Amazon.find_element(By.XPATH,'//*[@id="continue"]').click()
        time.sleep(2)
        password = WebDriverWait(driver_Amazon, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ap_password"]')))
        for i in "HoudaRanya@12":
           password.send_keys(i)
           time.sleep(random.uniform(0,0.5)) 
        time.sleep(8)
        driver_Amazon.find_element(By.XPATH,'//*[@id="signInSubmit"]').click()
        dropdown = WebDriverWait(driver_Amazon, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "a-dropdown-prompt")))
        dropdown.click()
        morocco_option = WebDriverWait(driver_Amazon, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@id='address-ui-widgets-countryCode-dropdown-nativeId_148' and text()='Morocco']"))
        )
        morocco_option.click()
        time.sleep(2)
        nom = WebDriverWait(driver_Amazon, 10).until(EC.element_to_be_clickable((By.ID, "address-ui-widgets-enterAddressFullName")))
        nom.clear()
        for i in "Nourelhouda":
           nom.send_keys(i)
        time.sleep(random.uniform(0, 0.5))
        time.sleep(2)
        phone = WebDriverWait(driver_Amazon, 10).until(EC.element_to_be_clickable((By.ID, "address-ui-widgets-enterAddressPhoneNumber")))
        phone.clear()
        for i in "0944738292":
          phone.send_keys(i)
        time.sleep(random.uniform(0, 0.5))
        adrss = WebDriverWait(driver_Amazon, 10).until(EC.element_to_be_clickable((By.ID, "address-ui-widgets-enterAddressLine1")))
        adrss.clear()
        for i in "Dakhla":
          adrss.send_keys(i)
        time.sleep(random.uniform(0, 0.5))
        time.sleep(1)
        adrss2 = WebDriverWait(driver_Amazon, 10).until(EC.element_to_be_clickable((By.ID, "address-ui-widgets-enterAddressLine2")))
        adrss2.clear()
        for i in "Dakhla":
         adrss2.send_keys(i)
        time.sleep(random.uniform(0, 0.5))
        time.sleep(1)
        city = WebDriverWait(driver_Amazon, 10).until(EC.element_to_be_clickable((By.ID, "address-ui-widgets-enterAddressCity")))
        city.clear()
        for i in "Agadir":
          city.send_keys(i)
        time.sleep(random.uniform(0, 0.5))
        time.sleep(2)
        province = WebDriverWait(driver_Amazon, 10).until(EC.element_to_be_clickable((By.ID, "address-ui-widgets-enterAddressStateOrRegion")))
        province.clear()
        for i in "Agadir IDAoutanane":
          province.send_keys(i)
        time.sleep(random.uniform(0, 0.5))
        time.sleep(2)
        zip = WebDriverWait(driver_Amazon, 10).until(EC.element_to_be_clickable((By.ID, "address-ui-widgets-enterAddressPostalCode")))
        zip.clear()
        for i in "80000":
           zip.send_keys(i)
        time.sleep(random.uniform(0, 0.5))
        time.sleep(10)
        
    
        
