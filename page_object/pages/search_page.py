from selenium.webdriver.common.by import By

from page_object.drivers.android_client import AndroidClient
from page_object.pages.base_page import BasePage


class SearchPage(BasePage):

    _edit_location = (By.ID, "search_input_text")

    def search(self, key):
        self.find(self._edit_location).send_keys(key)
        # self.find(self._edit_location).click()
        search_result = (By.XPATH, "//*[contains(@resource-id,'name') and @text='{}']".format(key))
        self.find(search_result).click()
        return self

    def add_selected(self, key):
        self.find(key).click()
        return self

    def is_selected(self, key):
        followbutton = (By.XPATH, "//*[contains(@resource-id,'stockCode') and @text='{}']/../../..//*[contains(@resource-id, 'follow')]".format(key))
        resourceid = self.find(followbutton).get_attribute("resource-id")
        print("%%% id %%%%", resourceid)
        return "followed_btn" in resourceid