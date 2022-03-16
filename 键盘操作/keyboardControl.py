from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
url = 'http://localhost:63342/seleniumcodes/%E9%94%AE%E7%9B%98%E6%93%8D%E4%BD%9C/keyboardControl.html?_ijt=uacc2325vhjnmrhgtj7ki5p5f3&_ij_reload=RELOAD_ON_SAVE'
driver.get(url)
time.sleep(5)

# 利用组合键Ctrl+A全选内容
driver.find_element(by=By.CLASS_NAME,value='ctrl-c').send_keys(Keys.CONTROL,'a')
# 利用组合键Ctrl+C复制内容
driver.find_element(by=By.CLASS_NAME,value='ctrl-c').send_keys(Keys.CONTROL,'c')
# 利用组合键Ctrl+V粘贴内容
driver.find_element(by=By.CLASS_NAME,value='ctrl-v').send_keys(Keys.CONTROL,'v')
# 同时按住Alt、Shift和I键
ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ALT).send_keys('i')
time.sleep(5)
driver.quit()