from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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

con_forms = espera.until(EC.presence_of_all_elements_located((By.ID, 'item-0')))
for opcao in con_forms:
        if 'Practice Form' in opcao.text:
            opcao.click()
            break

def preencher_form(navegador):
     nome = espera.until(EC.presence_of_element_located((By.ID, 'firstName')))
     sobrenome = espera.until(EC.presence_of_element_located((By.ID, 'lastName')))
     email = espera.until(EC.presence_of_element_located((By.ID, 'userEmail')))
     genero = espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'custom-control')))
     numero = espera.until(EC.presence_of_element_located((By.ID, 'userNumber')))
     calendario = espera.until(EC.presence_of_element_located((By.ID, 'dateOfBirthInput')))
     hobbies = espera.until(EC.presence_of_element_located((By.CLASS_NAME, 'custom-control-label')))

     navegador.execute_script("window.scrollTo(0, 0);")
     time.sleep(0.5)

     # Tenta scroll até o elemento
     navegador.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", calendario)
     time.sleep(0.5)

     nome.send_keys('Manoel')
     sobrenome.send_keys('Neto')
     email.send_keys('manoel@gmail.com')
     for opcao in genero:
          if 'Male' in opcao.text:
               opcao.click()
               break
     numero.send_keys('9999999999')

     calendario.click()
     seletor_ano = espera.until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__year-select')))
     seletor_ano.click()
     seletor_ano.find_element(By.XPATH, f"//option[@value='{2005}']").click()
     seletor_dia = espera.until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__day.react-datepicker__day--015')))
     seletor_dia.click()

     assunto_container = espera.until(EC.presence_of_element_located((By.ID, 'subjectsContainer')))
     input_assunto = assunto_container.find_element(By.CSS_SELECTOR, 'input')
     assunto_container.click()
     input_assunto.send_keys('ASSUNTO TESTE')

     navegador.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", hobbies)
     time.sleep(0.5)
     for opcao in hobbies:
          if 'Sports' in opcao.text:
               opcao.click()
               break
     

preencher_form(navegador)





time.sleep(1000)