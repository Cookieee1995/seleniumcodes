
from selenium import webdriver

# 屏蔽浏览器对Selenium的检测
options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches',['enable-automation'])
# driver = webdriver.Chrome(options=options)

# 禁止图片和视频加载
# prefs = {"profile.managed_default_content_settings.images":2}
# options.add_experimental_option('prefs',prefs)
# driver = webdriver.Chrome(options=options)

# 添加扩展插件
# 在添加插件时，需要将插件下载到本地，然后在启动浏览器时在ChromeOptions类中添加：
options.add_extension('xxx.crx')

# 设置编码
options.add_argument('lang=zh_CN.UTF-8')
driver = webdriver.Chrome(chrome_options=options)