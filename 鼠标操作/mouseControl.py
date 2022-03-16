from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'http://localhost:63342/seleniumcodes/%E9%BC%A0%E6%A0%87%E6%93%8D%E4%BD%9C/FirstProject_html.html?_ijt=bskb4ffaq4m001e41mqcfdaimm&_ij_reload=RELOAD_ON_SAVE'
driver.get(url)
time.sleep(5)

# 定位到需要右击的元素
# right_element = driver.find_element(by=By.ID,value='btn-login')
# 对元素进行右击操作
# ActionChains(driver).context_click(right_element).perform()

# double_element = driver.find_element(by=By.ID,value='id')
# 鼠标双击
# ActionChains(driver).double_click(double_element).perform()

# 定位到需要悬停的元素
# move_wait_element = driver.find_element(by=By.LINK_TEXT,value='设置')
# 鼠标悬停
# ActionChains(driver).move_to_element(move_wait_element).perform()

# 定位源对象
# source = driver.find_element(by=By.ID,value='id')
# 定位目标对象
# target = driver.find_element(by=By.ID,value='id')
# 将源对象拖放到目标对象的位置
# ActionChains(driver).drag_and_drop(source,target).perform()

time.sleep(5)
driver.quit()