from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'http://localhost:63342/seleniumcodes/%E7%89%B9%E6%AE%8ADOM%E7%BB%93%E6%9E%84%E6%93%8D%E4%BD%9C/windowsAlert.html?_ijt=g6eepv1tlup04n4u8fke2r37ik&_ij_reload=RELOAD_ON_SAVE'
driver.get(url)
driver.implicitly_wait(7)

# driver.find_element(by=By.ID,value='windows').find_element(by=By.TAG_NAME,value='input').click()
# time.sleep(5)
# 等待弹窗的出现
# WebDriverWait(driver,20).until(EC.alert_is_present())

# 切换进alert弹窗
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()

# 单击弹窗按钮
driver.find_element(by=By.ID,value='noWindows').find_element(by=By.TAG_NAME,value='input').click()
time.sleep(1)
# 关闭弹窗
driver.find_element(by=By.ID,value='header-right').click()
time.sleep(5)
driver.quit()