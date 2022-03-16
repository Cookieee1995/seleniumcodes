from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'http://localhost:63342/seleniumcodes/%E5%AF%B9%E8%B1%A1%E6%93%8D%E4%BD%9C/FirstProject_html.html?_ijt=v1t3v644nub61hmjg2ceonrv21&_ij_reload=RELOAD_ON_SAVE'
driver.get(url)
time.sleep(5)

# 单击对象
# driver.find_element(by=By.ID,value='btn-login').click()

# 输入内容
# driver.find_element(by=By.ID,value='email').send_keys('1725855615@qq.com')

# 清空内容
# time.sleep(3)
# driver.find_element(by=By.ID,value='email').clear()

# 提交表单
# driver.find_element(by=By.ID,value='submit').submit()

# 获取文本内容
# login_text = driver.find_element(by=By.ID,value='btn-login').text
# print(login_text)

# 获取对象属性值
# email_name = driver.find_element(by=By.ID,value='email').get_attribute('name')
# print(email_name)

time.sleep(5)
driver.quit()