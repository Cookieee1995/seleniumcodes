import time

# 强制等待
time.sleep(5)

# 隐式等待是全局的针对所有元素设置的等待时间，可以使用 implicitly_wait(time)方法来实现。
from selenium import webdriver

driver = webdriver.Chrome()
url = ''
driver.get(url)
driver.implicitly_wait(10)

# 显式等待是针对某个元素设置一个等待时间，可以使用WebDriverWait()方法来实现。
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
# 显示等待10s，每隔0.5s尝试一次。默认为0.5s，所以也可以不用赋值
WebDriverWait(driver,10,0.5).until(expected_conditions.presence_of_element_located(By.ID,'search'))
# class WebDriverWait(object):
    # def __init__(self,driver,timeout,poll_frequency=POLL_FREQUENCY,ignored_exceptions=None):

