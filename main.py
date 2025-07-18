                        # BLOCO DE IMPORTAÇÃO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

                        # BLOCO DE PUSH
navegador = webdriver.Chrome()
navegador.get('https://demoqa.com/')
navegador.maximize_window()
espera = WebDriverWait(navegador, 20)

def abrir_site(navegador):
     navegador.get('https://demoqa.com/')


                                         # BLOCO PRINCIPAL


                        # FUNÇÃO DE CLICAR NO FORMULÁRIO
def forms(navegador):

    clicar_forms = espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card.mt-4')))
    for opcao in clicar_forms:
        if 'Forms' in opcao.text:
            opcao.click()
            break
        
forms(navegador)

                        # FUNÇÃO DE COMEÇAR O FORMULÁRIO
con_forms = espera.until(EC.presence_of_all_elements_located((By.ID, 'item-0')))
for opcao in con_forms:
        if 'Practice Form' in opcao.text:
            opcao.click()
            break


                        # FUNÇÃO DE PREENCHER FORMULÁRIO
def preencher_form(navegador):

                             # CITAÇÕES DE VARIÁVEIS 
     nome = espera.until(EC.presence_of_element_located((By.ID, 'firstName')))
     sobrenome = espera.until(EC.presence_of_element_located((By.ID, 'lastName')))
     email = espera.until(EC.presence_of_element_located((By.ID, 'userEmail')))
     genero = espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'custom-control')))
     numero = espera.until(EC.presence_of_element_located((By.ID, 'userNumber')))
     calendario = espera.until(EC.presence_of_element_located((By.ID, 'dateOfBirthInput')))
     hobbies = espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'custom-control')))
     endereco = espera.until(EC.presence_of_element_located((By.ID, 'currentAddress')))
     submit = espera.until(EC.presence_of_element_located((By.ID, 'submit')))

                        # PREENCHIMENTO DE FORMULÁRIO

     # campo de preenchimento de dados pessoais
     nome.send_keys('Manoel')
     sobrenome.send_keys('Neto')
     email.send_keys('manoel@gmail.com')

     # scroll até a parte de gênero
     time.sleep(0.5)
     navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit)
     for opcao in genero:
          if 'Male' in opcao.text:
               opcao.click()
               break
          
     numero.send_keys('9999999999')

     # campo de preenchimento de calendário
     calendario.click()
     seletor_ano = espera.until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__year-select')))
     seletor_ano.click()
     seletor_ano.find_element(By.XPATH, f"//option[@value='{2005}']").click()
     seletor_dia = espera.until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__day.react-datepicker__day--015')))
     seletor_dia.click()

     # campo de preenchimento de assunto
     assunto_container = espera.until(EC.presence_of_element_located((By.ID, 'subjectsContainer')))
     input_assunto = assunto_container.find_element(By.CSS_SELECTOR, 'input')
     assunto_container.click()
     input_assunto.send_keys('Maths')
     input_assunto.send_keys(Keys.ENTER)

     # campo de preenchimento de hobbies
     for opcao in hobbies:
          if 'Sports' in opcao.text:
               opcao.click()
               break
     
     # campo de upload de algum documento
     picture = espera.until(EC.presence_of_element_located((By.ID, 'uploadPicture')))
     picture.send_keys(r"C:\Users\manoel.rodrigues\Pictures\Screenshots\Captura de tela 2025-07-15 142954.png")

     endereco.send_keys('TESTE TESTETESTE TESTETESTE TESTETESTE TESTETESTE TESTETESTE TESTETESTE TESTETESTE TESTETESTE TESTE')

     # campo de preenchimento de estado e cidade
     estado = espera.until(EC.element_to_be_clickable((By.ID, "state")))
     navegador.execute_script("arguments[0].click();", estado)

     estado_input = espera.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#state input")))
     estado_input.send_keys("Haryana")
     estado_input.send_keys(Keys.ENTER)

     cidade = espera.until(EC.element_to_be_clickable((By.ID, 'city')))
     navegador.execute_script("arguments[0].click();", cidade)

     cidade_input = espera.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#city input")))
     cidade_input.send_keys("Panipat")
     cidade_input.send_keys(Keys.ENTER)

     submit.click()

preencher_form(navegador)

abrir_site(navegador)

def elementos(navegador):
     
    clicar_elementos = espera.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card.mt-4')))
    for opcao in clicar_elementos:
        if 'Elements' in opcao.text:
            opcao.click()
            break
        
elementos(navegador)

web_tabela = espera.until(EC.presence_of_element_located((By.ID, 'item-3')))
web_tabela.click()

def tabela(navegador):

     add = espera.until(EC.presence_of_element_located((By.ID, 'addNewRecordButton')))
     add.click()

     nome = espera.until(EC.presence_of_element_located((By.ID, 'firstName')))
     sobrenome = espera.until(EC.presence_of_element_located((By.ID, 'lastName')))
     email = espera.until(EC.presence_of_element_located((By.ID, 'userEmail')))
     idade = espera.until(EC.presence_of_element_located((By.ID, 'age')))
     salario = espera.until(EC.presence_of_element_located((By.ID, 'salary')))
     departamento = espera.until(EC.presence_of_element_located((By.ID, 'department')))
     submit_add = espera.until(EC.presence_of_element_located((By.ID, 'submit')))

     nome.send_keys('Manoel')
     sobrenome.send_keys('Neto')
     email.send_keys('manoel@gmail.com')
     idade.send_keys('20')
     salario.send_keys('10000')
     departamento.send_keys('Automation')
     submit_add.click()

     add = espera.until(EC.presence_of_element_located((By.ID, 'addNewRecordButton')))
     add.click()

     nome = espera.until(EC.presence_of_element_located((By.ID, 'firstName')))
     sobrenome = espera.until(EC.presence_of_element_located((By.ID, 'lastName')))
     email = espera.until(EC.presence_of_element_located((By.ID, 'userEmail')))
     idade = espera.until(EC.presence_of_element_located((By.ID, 'age')))
     salario = espera.until(EC.presence_of_element_located((By.ID, 'salary')))
     departamento = espera.until(EC.presence_of_element_located((By.ID, 'department')))
     submit_add = espera.until(EC.presence_of_element_located((By.ID, 'submit')))

     nome.send_keys('Andressa')
     sobrenome.send_keys('Calaça')
     email.send_keys('andressa@gmail.com')
     idade.send_keys('20')
     salario.send_keys('2000')
     departamento.send_keys('RH')
     submit_add.click()

     scroll = espera.until(EC.presence_of_element_located((By.ID, 'item-8')))
     time.sleep(0.5)
     navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", scroll )


     edit = espera.until(EC.presence_of_element_located((By.ID, 'edit-record-4')))
     edit.click()
     salario = espera.until(EC.presence_of_element_located((By.ID, 'salary')))
     salario.clear()
     salario.send_keys('20000')
     submit_add = espera.until(EC.presence_of_element_located((By.ID, 'submit')))
     submit_add.click()






tabela(navegador)





time.sleep(10000)