from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import os
from catch_trace import catch_launch_trace
import datetime
import time

class AppTest:
    CONST_WAIT_TIME = 1 # in sec
    capabilities = dict (
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        language='zh',
        locale='CN',
        localeScript='Hans',
        # autoGrantPermissions = True, # work only if noReset = false
        noReset = True
    )
    appium_server_url = 'http://localhost:4723'

    def __init__(self, raw_data):
        self.app_name = raw_data['app_name']
        self.pkg_name = raw_data['pkg_name']
        self.screen_record_path = raw_data['screen_record_path']
        self.abnormal_check = raw_data['abnormal_check']
        self.driver = webdriver.Remote(self.appium_server_url,
                                  options=UiAutomator2Options().load_capabilities(self.capabilities))
        pass

    def remove_abnormal_windows(self):
        pass

    def launch_test(self , app_name):
        # TODO
        for i in range(3): 
            # 模拟按下 home key
            self.driver.terminate_app(self.pkg_name)
            self.driver.press_keycode(3)
            self.enter_home_app_list()
            self.find_text_and_click(app_name)
            self.is_test_valid()
        pass

    def enter_home_app_list(self):
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        start_x = width // 2
        start_y = height // 2
        end_y = height //4
        self.driver.swipe(start_x, start_y, start_x, end_y, 200)
        # items = self.driver.find_elements(by=AppiumBy.XPATH, value='//*[@text=\" \"]')
        # if len(items) > 0:
        #     items[0].click()
        #     self.record_status("home_list")
        
    def record_status(self, section_name, status="ok"):
        if status == "error":
            section_name = "error_"+section_name
        file_name = section_name + ".png"
        file_name = os.path.join(self.screen_record_path, file_name)
        self.driver.get_screenshot_as_file(file_name)
        
    def find_text_and_click(self, appName):
        items = self.driver.find_elements(by=AppiumBy.XPATH, value="//*[@text=\"{0}\"]".format(appName))
        if len(items) > 0:
            current_time = datetime.datetime.now().isoformat().replace(":","-").replace(".","-")
            filename = f"{appName}_{current_time}.perfetto-trace"
            process = catch_launch_trace(filename)
            time.sleep(8)
            items[0].click()
            process.wait()
        else:
            # self.record_status(info['window_name'], status= "error")
            # self.driver.get_screenshot_as_file()
            # self.driver.quit()
            pass
    
    def is_test_valid(self):
        is_valid = True
        for checker in self.abnormal_check:
            print(checker)
            items = self.driver.find_elements(by=AppiumBy.XPATH, value=checker['pattern'])
            if len(items) > 0:
                self.record_status(checker['window_name'], status= "error")
                items[0].click()
                is_valid = False
        return is_valid
            # else:
            #     self.record_status(info['window_name'], status= "error")