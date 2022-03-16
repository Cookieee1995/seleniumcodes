from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'http://localhost:63342/seleniumcodes/%E7%89%B9%E6%AE%8ADOM%E7%BB%93%E6%9E%84%E6%93%8D%E4%BD%9C/fram&iframe.html?_ijt=667je6d29chubtu614cm18c2vm&_ij_reload=RELOAD_ON_SAVE'
driver.get(url)
driver.implicitly_wait(10)

# 切换到iframe结构
driver.switch_to.frame('iframeContainer')
time.sleep(5)
driver.find_element(by=By.ID,value='noWindows').find_element(by=By.TAG_NAME,value='input').click()
time.sleep(5)
driver.quit()
