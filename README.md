# 🛒 Smart Buy Bot : Amazon vs Jumia

## 📌 Description
Ce projet implémente un **agent intelligent d'achat automatisé** capable de comparer en temps réel les prix d'un produit sur trois plateformes majeures de e-commerce : **Amazon** et **Jumia** et **UltraPC**. 

Le système optimise l'expérience d'achat grâce à :
* ⚡ **Multithreading** : Recherches simultanées sur les deux plateformes.
* 🤖 **Automation** : Identification de l'offre la moins chère et tunnel d'achat automatique.
* 🛡️ **Anti-Bot Bypass** : Utilisation de `selenium-stealth` et résolution de CAPTCHA.

---

## 🧠 Architecture du Projet
Le projet est structuré de manière modulaire pour faciliter la maintenance :

```text
project/
│
├── nouveau.py       # Script principal (logique de comparaison et multithreading)
├── Amazon.py         # Module d'extraction et d'automatisation pour Amazon
├── Jumiaa.py         # Module d'extraction et d'automatisation pour Jumia
├── Ultra.py          # Module d'extraction et d'automatisation pour UltraPC
├── README.md         # Documentation

# 🤖 Bot de Web Scraping & Automatisation

## ⚙️ Technologies Utilisées
Le bot s'appuie sur des technologies robustes pour le web scraping et l'automatisation :

- **Python 3.x** : Langage principal  
- **Selenium** : Pilotage du navigateur et interactions complexes  
- **BeautifulSoup4 (LXML)** : Analyse rapide du HTML  
- **Threading** : Pour la performance (recherche en parallèle)  
- **AmazonCaptcha** : Résolution intelligente des barrières de sécurité  
- **WebDriver Manager** : Installation automatique des drivers Chrome  

---

## 📦 Installation & Configuration

### 1. Prérequis
Assurez-vous d'avoir **Google Chrome** installé sur votre machine.

### 2. Installation des dépendances
Copiez et lancez la commande suivante dans votre terminal :

```bash
pip install selenium selenium-stealth beautifulsoup4 amazon-captcha-solver webdriver-manager requests lxml

# 🚀 Utilisation du Système

## Étape 1 : Lancement
Lancez le programme via la console :

```bash
python nouveau.py

# Étape 2 : Processus de décision

## Input
- Vous saisissez le nom du produit.

## Scan
- Le bot ouvre trois instances de navigation.

## Comparaison
- Il compare **prix_Amazon** , **prix_Jumia**et **UltraPC**

## Action
- Le navigateur du site le plus cher est immédiatement fermé.  
- Le bot procède à la commande sur le site le moins cher.

---



---


---

 

---

## ⚠️ Remarques Importantes
- **Sécurité des comptes** : Les identifiants de test *(Email/Mot de passe)* sont codés en dur dans les scripts.  
  👉 Pensez à utiliser des **variables d’environnement** pour vos comptes personnels.  
- **Vitesse** : Les `time.sleep` sont optimisés pour éviter d’être détecté comme un robot tout en restant rapide.  

---


