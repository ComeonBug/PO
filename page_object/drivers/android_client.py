from appium import webdriver


class AndroidClient():

    def __init__(self):
        pass

    def install_app(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "lytest"
        # adb shell pm list packages | grep ***
        caps["appPackage"] = "com.xueqiu.android"
        # 如何找到activity名字：adb logcat | grep ***
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 解决第一次启动的权限问题
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        return self.driver

    def retart_app(self):
        pass