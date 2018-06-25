"""functional_tests.py
On import 'webdriver' depuis selenium
On crée un instance du navigateur web Firefox
On cherche à obtenir une page web à l'adresse '127.0.0.1:8000'
On contrôle ensuite que le mot "Django" est bien présent dans le titre de la page"
"""

from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://127.0.0.1:8000')

assert 'Django' in browser.title
