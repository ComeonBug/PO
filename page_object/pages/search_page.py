import time

from selenium.webdriver.common.by import By

from page_object.drivers.android_client import AndroidClient
from page_object.pages.base_page import BasePage


class SearchPage(BasePage):

    _edit_location = (By.ID, "search_input_text")

    def search(self, key, code=''):
        # 搜索框输入内容
        self.find(self._edit_location).send_keys(key)
        time.sleep(3)
        # 点击搜索联动list中的第一条
        if code:
            search_result = (By.XPATH, "//*[contains(@resource-id,'code') and @text='{}']".format(code))
        else:
            search_result = (By.XPATH, "//*[contains(@resource-id,'code') and @text='{}']".format(key))
        self.find(search_result).click()
        return self

    def add_selected(self, code):
        follow_button = (By.XPATH,
                        "//*[contains(@resource-id,'stockCode') and @text='{}']/../../..//*[contains(@resource-id, 'follow_btn')]".format(code))
        self.find(follow_button).click()
        return self

    def is_selected(self, code):
        follow_button = (By.XPATH,
                        "//*[contains(@resource-id,'stockCode') and @text='{}']/../../..//*[contains(@resource-id, 'follow')]".format(code))
        resourceid = self.find(follow_button).get_attribute("resource-id")
        return "followed_btn" in resourceid

    def searchByName(self, username):
        switch_to_usertab = (By.XPATH, "//*[contains(@resource-id,'title_text') and @text='用户']")
        time.sleep(5)
        self.search(username).find(switch_to_usertab).click()
        return self

    def is_followed(self, username):
        user_follow_button = (By.XPATH, "//*[contains(@resource-id,'user_name') and @text={}]/../..//*[contains(@resource-id, 'follow')]".format(username))
        return "followed" in user_follow_button

    def cancel(self):
        self.find((By.XPATH, "//*[@text='取消']")).click()

    def remove_select(self, code):
        followed_button = (By.XPATH,
                        "//*[contains(@resource-id,'stockCode') and @text='{}']/../../..//*[contains(@resource-id, 'followed_btn')]".format(
                            code))
        self.find(followed_button).click()
        return self