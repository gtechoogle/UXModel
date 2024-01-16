from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import os

class AppInit:
    CONST_WAIT_TIME = 1 # in sec
    capabilities = dict (
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        language='zh',
        locale='CN',
        localeScript='Hans',
        autoGrantPermissions = True, # work only if noReset = false
        # noReset = True
    )
    appium_server_url = 'http://localhost:4723'
    def __init__(self, raw_data):
        self.apk_path = raw_data['apk_path']
        self.root_path = raw_data['root_path']
        self.screen_record_path = raw_data['screen_record_path']
        full_path = os.path.join(os.getcwd(), self.apk_path)
        self.capabilities['app'] = full_path
        pass

    def first_run(self, steps_info):
        self.driver = webdriver.Remote(self.appium_server_url,
                                  options=UiAutomator2Options().load_capabilities(self.capabilities))
        self.driver.implicitly_wait(self.CONST_WAIT_TIME)
        for info in steps_info:
            print (info)
            self.find_and_click(info)
        self.record_status("complete_first_run")
        
    def record_status(self, section_name, status="ok"):
        if status == "error":
            section_name = "error_"+section_name
        file_name = section_name + ".png"
        file_name = os.path.join(self.screen_record_path, file_name)
        self.driver.get_screenshot_as_file(file_name)
        
    def find_and_click(self, info):
        items = self.driver.find_elements(by=AppiumBy.XPATH, value=info['pattern'])
        if len(items) > 0:
            self.record_status(info['window_name'])
            items[0].click()
        else:
            self.record_status(info['window_name'], status= "error")
            # self.driver.get_screenshot_as_file()
            # self.driver.quit()
        
    