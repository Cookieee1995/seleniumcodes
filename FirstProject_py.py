from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://localhost:63342/seleniumcodes/FirstProject_html.html?_ijt=vl64ab6jjefgtpj5qfpt3r8asc&_ij_reload=RELOAD_ON_SAVE'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

driver.find_element(by=By.ID,value='email').send_keys('**********@qq.com')
driver.find_element(by=By.NAME,value='password').send_keys('*********')
driver.find_element(by=By.ID,value='btn-login').click()

time.sleep(10)
driver.quit()