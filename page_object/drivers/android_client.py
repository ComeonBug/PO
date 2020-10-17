from appium import webdriver


class AndroidClient():
    driver: webdriver

    def __init__(self):
        pass

    @classmethod
    def install_app(cls):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "lytest"
        # adb shell pm list packages | grep ***
        caps["appPackage"] = "com.xueqiu.android"
        # 如何找到activity名字：adb logcat | grep ***
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 解决第一次启动的权限问题
        caps["autoGrantPermissions"] = "true"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)


    def retart_app(self):
        pass

