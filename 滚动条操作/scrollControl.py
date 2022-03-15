from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'http://localhost:63342/seleniumcodes/%E6%BB%9A%E5%8A%A8%E6%9D%A1%E6%93%8D%E4%BD%9C/scrollControl.html?_ijt=9b85a40o0cuqmult0ucbhg8bln&_ij_reload=RELOAD_ON_SAVE'
driver.get(url)
time.sleep(8)

# 移动到页面底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)
# 移动到页面顶部
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
time.sleep(5)
# 移动到使“滚动条操作第二部分”顶部与窗口的顶部对齐位
element2 = driver.find_element(by=By.CLASS_NAME,value='part2')
driver.execute_script("arguments[0].scrollIntoView();",element2)
time.sleep(5)
# 移动到使“滚动条操作第三部分”底部与窗口的底部对齐位
element3 = driver.find_element(by=By.CLASS_NAME,value='part3')
driver.execute_script("arguments[0].scrollIntoView(false);",element3)
time.sleep(5)
