from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'http://localhost:63342/seleniumcodes/%E5%AF%B9%E8%B1%A1%E6%93%8D%E4%BD%9C/%E5%85%83%E7%B4%A0%E7%8A%B6%E6%80%81.html?_ijt=hupetc0tlpaqfd1tqarb5po9iu&_ij_reload=RELOAD_ON_SAVE'
driver.get(url)
time.sleep(5)

# 内容显示
show_text = driver.find_element(by=By.CLASS_NAME,value='show-text').is_displayed()
print(show_text)

# 内容未显示
hidden_text = driver.find_element(by=By.CLASS_NAME,value='hidden-text').is_displayed()
print(hidden_text)

time.sleep(5)

# 输入框可编辑
enabled_text = driver.find_element(by=By.CLASS_NAME,value='enabled-text').is_enabled()
print(enabled_text)
# 输入框不可编辑
disabled_text = driver.find_element(by=By.CLASS_NAME,value='disabled-text').is_enabled()
print(disabled_text)
time.sleep(5)

# 元素被选中
selected_elm = driver.find_element(by=By.NAME,value='python').is_displayed()
print(selected_elm)
unselected_elm = driver.find_element(by=By.NAME,value='JavaScript').is_displayed()
print(unselected_elm)
# 元素未被选中
driver.quit()