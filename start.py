from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    app='\\testApk\\news_article.apk'
)

appium_server_url = 'http://localhost:4723'
capabilities['app'] = os.path.join(os.getcwd(),"testApk\\news_article.apk")
print(capabilities)

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
driver.quit()