from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook


#abrir Credenciais para acessar o linkedin

def read_credentials(file_path):
    with open(file_path,"r") as file:
        lines = file.readlines()

        credentials ={}
        for line in lines:
            key, value = line.strip().split(":")
            credentials[key] = value
        return credentials

file_path_credentials = "credentials.txt"

credentials = read_credentials(file_path_credentials)


print("vamos começar a buscar suas vagas")
search = input("digite sua busca: ")


# inicia o navegador
browser = webdriver.Chrome()
browser.get("https://www.linkedin.com/")
sleep(2)
email = browser.find_element(By.XPATH, "//input[@id='session_key']")
password = browser.find_element(By.XPATH, "//input[@id='session_password']")
btn_entrar = browser.find_element(By.XPATH, "//button[normalize-space(text())='Entrar']")
sleep(2)
email.send_keys(credentials['user'])
sleep(2)
password.send_keys(credentials['senha'])
sleep(2)
btn_entrar.click()
input("resolva o enigma e volte aqui para pressionar ENTER")
sleep(5)
browser.get("https://www.linkedin.com/jobs/")
sleep(5)
input_jobs_search = browser.find_element(By.XPATH, "//header//input")
sleep(5)
input_jobs_search.send_keys(search)
sleep(5)
input_jobs_search.send_keys(Keys.ENTER)
sleep(5)
ul_element = browser.find_element(By.CSS_SELECTOR, "main div.jobs-search-results-list")
sleep(5)


def scroll_list(pixels):
    browser.execute_script(f"arguments[0].scrollTop += {pixels};", ul_element)
    sleep(2)


links = []
for _ in range(25):
    scroll_list(200)
    links = browser.find_elements(By.XPATH, "//main//div/div//ul//li//a[@data-control-id]")
    print(len(links))
    if len(links) >= 25:
        print(f'chegamos ao numero esperado de {len(links)}')
        break

spreadsheet = Workbook()

sheet = spreadsheet.active

sheet['A1'] = "NOME DA VAGA"
sheet['B1'] = "LINK DA VAGA"
next_line = sheet.max_row + 1

for link in links:
    text = link.text
    url_link = link.get_attribute("href")

    sheet[f'A{next_line}'] = text
    sheet[f'B{next_line}'] = url_link

    next_line += 1

spreadsheet.save("vagas_links-"+search+".xlsx")
print("planilha criada")

print("Encerrando busca")
sleep(3)
browser.quit()

