from appium import webdriver
from appium.webdriver import WebElement
from selenium.webdriver.common.by import By
import yaml

from page_object.drivers.android_client import AndroidClient


class BasePage():
    # driver: webdriver
    #
    def __init__(self):
        self.driver = self.get_driver()

    # @classmethod
    # def get_driver(cls):
    #     AndroidClient.install_app()
    #     cls.driver: webdriver = AndroidClient.driver
    @classmethod
    def get_client(cls):
        return AndroidClient

    def get_driver(self):
        # AndroidClient.install_app()
        driver: webdriver = AndroidClient.driver
        return driver

    def find(self, kv) -> WebElement:
        print("*****self.driver"*20)
        print(self.driver)
        print("*"*20)
        return self.driver.find_element(*kv)

    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='{}']".format(text)))

    def load_step(self, po_path, key, **kwargs):
        file = open(po_path, 'r')
        po_data = yaml.load(file)
        print("*"*20)
        print(kwargs.items())
        print("*"*20)
        po_method = po_data[key]
        for step in po_method:
            element: WebElement = self.driver.find_element(by=step['by'], value=step['locator'])
            action = str(step['action']).lower()
            # todo :由于弹框定位失败，try-catch来处理
            if action == 'click':
                element.click()
            elif action == 'send_keys':
                text = str(step['text'])
                for k,v in kwargs.items():
                    text = text.replace("$%s"%k, v)
                    print("Update: {}".format(text))
                element.send_keys(text)
            else:
                print("ERROR,UNKNOW ACTION {}".format(action))