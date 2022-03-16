# 屏幕截图一般用于在自动化测试过程中程序运行失败时自动截取当前页面，保留记录，方便查看运行失败的原因。

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = ''
driver.get(url)
driver.implicitly_wait(10)

try:
    driver.find_element(by=By.ID,value='')
except NoSuchElementException:
    driver.save_screenshot('img/screen.png')