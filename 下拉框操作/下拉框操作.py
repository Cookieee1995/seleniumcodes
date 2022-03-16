from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'http://localhost:63342/seleniumcodes/%E4%B8%8B%E6%8B%89%E6%A1%86%E6%93%8D%E4%BD%9C.html?_ijt=u6g70thqcb5e9rcr1nrodfepfh&_ij_reload=RELOAD_ON_SAVE'
driver.get(url)
driver.implicitly_wait(10)

# 定位下拉框
sel = driver.find_element(by=By.NAME,value='language')
# 根据索引选择css
Select(sel).select_by_index('2')
time.sleep(3)
# 根据文本值选择Html
Select(sel).select_by_visible_text('Html')

time.sleep(3)
driver.quit()