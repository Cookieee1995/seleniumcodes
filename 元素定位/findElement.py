from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'http://localhost:63342/seleniumcodes/%E5%85%83%E7%B4%A0%E5%AE%9A%E4%BD%8D/findElement.html?_ijt=v9kl2809nkfb8l1668v8dg9i33&_ij_reload=RELOAD_ON_SAVE'
driver.get(url)
time.sleep(6)

# id 定位
# id_maxlength = driver.find_element(by=By.ID,value='search').get_attribute('maxlength')
# assert id_maxlength == '10'

# class 定位
# class_value = driver.find_element(by=By.CLASS_NAME,value='btn-search').get_attribute('value')
# assert class_value == '检索'

# name 定位
# name_value = driver.find_element(by=By.NAME,value='language').get_attribute('type')
# assert name_value == 'checkbox'

# tag 定位
# tag_text = driver.find_element(by=By.TAG_NAME,value='h4').text
# assert tag_text == 'tag 定位'

# xPath 定位
# 绝对路径定位：从页面的最初位置开始定位，以一个单斜杠“/”开头。      '/html/body/div/p'
# 相对路径定位：从页面中可以确定唯一性的一个节点开始定位，以双斜杠“//”开头。       "//div[@id='search']/input"
# 使用@特殊符号进行属性匹配定位：@用来选择某节点的属性。语法：“//标签名[@属性='属性值']”         "//input[@name='firstName']"
# contains()：模糊定位。语法：“//标签名[contains(@属性名,'属性值')]”              "//a[contains(@href,'news')]"
# xPath_text = driver.find_element(by=By.XPATH,value='/html/body/div/p').text
# assert xPath_text == 'xPath 定位'

# link 定位
# link_href = driver.find_element(by=By.LINK_TEXT,value='Tynam').get_attribute('href')
# assert link_href == 'https://www.bing.com/'

# Partial link 定位
# partial_link_text = driver.find_element(by=By.PARTIAL_LINK_TEXT,value='link 定位').text
# assert partial_link_text == "Partial link 定位"

# CSS 选择器定位
# css_text = driver.find_element(by=By.CSS_SELECTOR,value='button.css').text
# assert css_text == "CSS 定位"


time.sleep(10)
driver.quit()

# 元素定位是通过在HTML代码中查找元素属性，从而确定需要的元素位置，进而对其进行操作。

# 在元素定位中定位一个元素，需要确认定位的元素是唯一的。