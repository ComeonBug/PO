from selenium.webdriver.common.by import By

from page_object.pages.base_page import BasePage
from page_object.pages.login_page import LoginPage


class ProfilePage(BasePage):
    _goto_login_button = (By.XPATH, "//*[contains(@text,'登录')]")

    def gotologin(self) -> LoginPage:
        self.find(self._goto_login_button).click()
        return LoginPage()