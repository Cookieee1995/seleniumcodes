from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# url = 'https://www.baidu.com/'
# url = 'https://www.bing.com/'
# driver.get(url)
# time.sleep(5)

# 不能频繁测试同一个网站或多个功能同时测试

# 浏览器最大化
# driver.maximize_window()
# time.sleep(5)

# 设置浏览器大小
# driver.set_window_size(500,900)
# time.sleep(5)
# driver.find_element(by=By.ID,value='kw').send_keys('腾讯')
# driver.find_element(by=By.ID,value='su').click()
# time.sleep(5)

# 浏览器后退
# driver.back()
# time.sleep(5)
# 浏览器前进
# driver.forward()
# time.sleep(5)
# 刷新页面
# driver.refresh()
# time.sleep(5)
# 关闭浏览器当前窗口
# driver.close()

# 结束进程
# driver.quit()

# 获取页面title
# print(driver.title)
# time.sleep(5)

# driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/div[3]/a[4]").click()
# time.sleep(10)
# 获得单机之后的url
# cur_url = driver.current_url
# print(cur_url)
# 获取页面源码
# print(driver.page_source)
# time.sleep(5)


# 切换浏览器窗口
driver = webdriver.Chrome()
url = 'http://localhost:63342/seleniumcodes/%E6%B5%8F%E8%A7%88%E5%99%A8%E6%93%8D%E4%BD%9C/changePage1.html?_ijt=21t3frhl0198be7vlb3hvp4of4&_ij_reload=RELOAD_ON_SAVE'
driver.get(url)
time.sleep(5)

# 获得当前页面句柄
page_handle = driver.current_window_handle
# 单击a标签进入第二个页面
driver.find_element(by=By.TAG_NAME,value='a').click()
time.sleep(5)
# 此时driver还停留在第一个页面，需要转换到第二个页面
# 获得所有窗口的句柄
handles = driver.window_handles
# 切换到第二个页面
for handle in handles:
    if handle != page_handle:
        driver.switch_to.window(handle)
print(driver.title)
driver.quit()