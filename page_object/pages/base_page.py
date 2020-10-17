from appium import webdriver
from appium.webdriver import WebElement
from selenium.webdriver.common.by import By

from page_object.drivers.android_client import AndroidClient


class BasePage():
    driver: webdriver

    def __init__(self):
        self.get_driver()

    @classmethod
    def get_driver(cls):
        AndroidClient.install_app()
        cls.driver = AndroidClient.driver


    @classmethod
    def get_client(cls):
        return AndroidClient

    def find(self, kv) -> WebElement:
        print("*****self.driver"*20)
        print(self.driver)
        print("*"*20)
        return self.driver.find_element(*kv)

    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='{}']".format(text)))
