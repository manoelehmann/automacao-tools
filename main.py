from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

navegador = webdriver.Chrome()
navegador.get('https://www.youtube.com/')
navegador.maximize_window()
