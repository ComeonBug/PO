from appium import webdriver
from appium.webdriver import WebElement

from page_object.drivers.android_client import AndroidClient


class BasePage():
    def __init__(self):
        self.driver = AndroidClient.driver

    def find(self, kv) -> WebElement:
        return self.driver.find_element(*kv)