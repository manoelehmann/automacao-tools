from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

navegador = webdriver.Chrome()
navegador.get('https://demoqa.com/')
navegador.maximize_window()
espera = WebDriverWait(navegador, 20)


def forms(navegador):

    # espera aparecer todos os elementos para ele fazer o FOR.
    clicar_forms = espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card.mt-4')))
    for opcao in clicar_forms:
        if 'Forms' in opcao.text:
            opcao.click()
            break

forms(navegador)





time.sleep(1000)