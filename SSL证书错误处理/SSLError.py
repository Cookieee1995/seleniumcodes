from selenium import  webdriver

options = webdriver.ChromeOptions()
# 添加忽视证书错误选项
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(chrome_options=options)
url = ''
driver.get(url)

# Firefox
profile = webdriver.FirefoxProfile()
# 添加接受不信任证书选项
profile.accept_untrusted_certs = True
driver = webdriver.Firefox(firefox_profile=profile)

# 转到此网页（不推荐）
driver = webdriver.Ie()
url = ''
driver.get(url)
# 选择继续访问URL
js = "javascript:document.getElementById('overridelink').click();"
driver.get(js)
driver.execute_script(js)