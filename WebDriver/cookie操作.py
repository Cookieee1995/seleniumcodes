from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com/')
# 清除所有的Cookie
driver.delete_all_cookies()
# 手动登录
time.sleep(50)
# 获取cookie
cookie = driver.get_cookies()
print(cookie)

driver.quit()