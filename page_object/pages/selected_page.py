# 第三步，组织这个页面
from selenium.webdriver.common.by import By

from page_object.drivers.android_client import AndroidClient
from page_object.pages.base_page import BasePage


class SelectedPage(BasePage):
    # 第四部：写这个页面的可能的方法，实现
    def addDefault(self):
        return self

    # 第四部：写这个页面的可能的方法，实现
    def getPriceByName(self, name):
        location = (By.XPATH, '//*[@text="{}" ]/../../../..//*[contains(@resource-id,"item_layout")]'.format(name))
        price = self.find(location).text
        return float(price)