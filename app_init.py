from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
class AppInit:
    capabilities = dict (
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        # app='\\testApk\\news_article.apk'，
        noReset = True
    )
    appium_server_url = 'http://localhost:4723'
    def __init__(self, apk_path):
        self.capabilities['app'] = apk_path
        pass

    def first_run(self, steps_info):
        self.driver = webdriver.Remote(self.appium_server_url,
                                  options=UiAutomator2Options().load_capabilities(self.capabilities))
        for info in steps_info:
            self.find_and_click(info)
        
    def find_and_click(self, info):
        self.driver.implicitly_wait(1000)
        items = self.driver.find_elements(by=AppiumBy.XPATH, value=info['pattern'])
        if len(items) > 0:
            items[0].click()
        else:
            self.driver.get_screenshot_as_file("a.png")
            self.driver.quit()
        
    