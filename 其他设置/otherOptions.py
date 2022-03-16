

# 限制页面加载时间
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException

# driver = webdriver.Chrome()
# 限制页面加载时间为30s
# driver.set_page_load_timeout(30)
# try:
#     driver.get('https://www.python.org/')
# except TimeoutException:
#     print('页面加载超过30秒，强制停止加载')
#     driver.execute_script('window.stop()')


# 获取环境信息
from selenium import webdriver

# driver = webdriver.Chrome()
# 打印浏览器Chrome的版本号
# print(driver.capabilities['browserVersion'])

# 非W3C标准命令
# options = webdriver.ChromeOptions()
# options.add_experimental_option('w3c',False)
# driver = webdriver.Chrome(options=options)