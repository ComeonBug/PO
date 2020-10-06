from appium import webdriver
from appium.webdriver import WebElement
from selenium.webdriver.common.by import By


from page_object.drivers.android_client import AndroidClient


class BasePage():
    def __init__(self):
        self.driver = AndroidClient.driver

    def find(self, kv) -> WebElement:
        # todo 处理弹框
        return self.driver.find_element(*kv)

    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='{}']".format(text)))