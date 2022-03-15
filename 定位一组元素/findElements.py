from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'http://localhost:63342/seleniumcodes/%E5%AE%9A%E4%BD%8D%E4%B8%80%E7%BB%84%E5%85%83%E7%B4%A0/%E5%A4%9A%E9%80%89%E6%A1%86.html?_ijt=r2inhn7058sllvne3m1kde0u3e&_ij_reload=RELOAD_ON_SAVE'
driver.get(url)
time.sleep(6)

# 得到所有的多选框
checkboxs = driver.find_elements(by=By.TAG_NAME,value='input')

# 将所有的多选框勾选
for checkbox in checkboxs:
    # 取消已经被勾选的复选框
    if checkbox.get_attribute('checked') is None:
        checkbox.click()
        time.sleep(3)

# 取消第一个勾选，勾选第二个多选框
# checkboxs[0].click()
# time.sleep()
# checkboxs[1].click()

driver.close()