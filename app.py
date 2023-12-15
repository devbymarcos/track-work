from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.linkedin.com/")

sleep(2)
email = browser.find_element(By.XPATH,"//input[@id='session_key']")
password = browser.find_element(By.XPATH,"//input[@id='session_password']")
btn_entrar = browser.find_element(By.XPATH,"//button[normalize-space(text())='Entrar']")
sleep(2)
email.send_keys("marcoslopes.cwb@gmail.com")
sleep(2)
password.send_keys("sepol7840")
sleep(2)
btn_entrar.click()
sleep(5)
browser.get("https://www.linkedin.com/jobs/")
sleep(5)
input_jobs_search = browser.find_element(By.XPATH,"//input[@id='jobs-search-box-keyword-id-ember23']")
sleep(5)
input_jobs_search.send_keys("Desenvolvedor python")
sleep(5)
input_jobs_search.send_keys(Keys.ENTER)
sleep(5)
sleep(20)