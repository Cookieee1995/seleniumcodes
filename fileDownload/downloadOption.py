from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()

prefs = {
    "download.prompt_for_download":False,# 弹窗
    "download.default_directory":""     # 下载目录
}

chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

url = ''
driver.get(url)
time.sleep(3)
driver.find_element(by=By.ID,value='').click()