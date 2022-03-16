from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'http://localhost:63342/seleniumcodes/fileUpload/fileUpload.html?_ijt=fg4stngrn5i7lfkref3pv0e0c6&_ij_reload=RELOAD_ON_SAVE'
driver.get(url)
driver.implicitly_wait(10)

# 文件上传
# "\\"第一个为转义字符(windows)
driver.find_element(by=By.ID,value='uploadFile').send_keys('/home/cookieee/codes/seleniumcodes/fileUpload/testFileUpload')
time.sleep(4)
driver.quit()