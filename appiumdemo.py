# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestWeilaiAndroid():

    def setup_class(self):
        print("set up class")
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "cn.com.weilaihui3"
        caps["appActivity"] = ".ui.activity.SplashActivity"
        caps["autoGrantPermissions"] = "true"
        caps["ensureWebviewsHavePages"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        caps["noReset"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 一般第一次比较满，所以放在setup_class比较好
        # 隐式等待implicitly
        self.driver.implicitly_wait(10)
        el3 = self.driver.find_element_by_xpath("//*[@resource-id='custom_tab_tv' and @text='爱车']")
        el3.click()

    def setup_method(self):
        el4 = self.driver.find_element_by_link_text("了解EC6详情")
        el4.click()

    def test_buyES6(self):
        #   隐式等待
        WebDriverWait(self.driver, 10, 1)
        el5 = self.driver.find_element_by_id("other_login")
        el5.click()
        self.driver.get_screenshot_as_file(time.strftime('%Y-%m-%d %H:%M:%S')+'.png')

    def teardown_class(self):
        print('tear dowm')
        self.driver.quit()


class Testlogin():
    def setup_class(self):
        print("set up class")
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "cn.com.weilaihui3"
        caps["appActivity"] = ".ui.activity.SplashActivity"
        caps["autoGrantPermissions"] = "true"
        caps["ensureWebviewsHavePages"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        caps["noReset"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def teardown_class(self):
        print('tear dowm')
        self.driver.quit()

    def test_login(self):
         pass