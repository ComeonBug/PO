import time
import yaml
from appium import webdriver


class AndroidClient():
    driver: webdriver
    platform='android'

    def __init__(self):
        pass

    @classmethod
    def install_app(cls):

        # 没有参数化的写法
        # caps = {}
        # caps["platformName"] = "Android"
        # caps["deviceName"] = "lytest"
        # # adb shell pm list packages | grep ***
        # caps["appPackage"] = "com.xueqiu.android"
        # # 如何找到activity名字：adb logcat | grep ***
        # caps["appActivity"] = ".view.WelcomeActivityAlias"
        # # 解决第一次启动的权限问题
        # caps["autoGrantPermissions"] = "true"
        # webdriver.Remote('http://localhost:4723/wd/hub', caps)
        # 参数化的写法参考 def init_driver(cls, key):

        return cls.init_driver('install_app')

    def retart_app(self):
        pass

    @classmethod
    def init_driver(cls, key):
        driver_data = yaml.load(open('../data/driver.yaml', 'r'))
        server = driver_data[key]['server']
        implicitly_wait = driver_data[key]['implicitly_wait']
        platform = driver_data['platform']
        cls.platform = platform
        caps = driver_data[key]['caps'][platform]

        cls.driver = webdriver.Remote(server, caps)
        cls.driver.implicitly_wait(implicitly_wait)
        # 下面这句是临时用来处理弹框的，后续要优化
        cls.driver.find_element_by_id('tv_agree').click()

        return cls.driver
