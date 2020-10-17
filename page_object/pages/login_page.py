from selenium.webdriver.common.by import By
from page_object.pages.base_page import BasePage


class LoginPage(BasePage):
    _close_locator = (By.ID, "iv_action_back")
    _other_locator = (By.ID, "login_without_password")
    _register_phone_num = (By.ID, "register_phone_number")
    _register_code = (By.ID, "register_code")
    _login_button = (By.ID, "button_next")
    _login_account = (By.ID, "login_account")
    _login_password = (By.ID, "login_password")
    _error_msg = (By.ID, "md_content")


    def login_by_WX(self):
        pass

    def login_by_WB(self):
        pass

    def login_by_QQ(self):
        pass

    def login_error_by_userinfo_old(self, username, password):
        self.find(self._login_account).send_keys(username)
        self.find(self._login_password).send_keys(password)
        self.find(self._login_button).click()
        return self

    def login_error_by_userinfo(self, username, password):
        self.load_step('../data/login_page.yaml','LoginByPassword',var1 = username, var2=password)
        return self

    def login_error_by_password(self):
        #todo
        pass

    def login_by_phone(self,phone, code):
        # todo
        return self

    def back(self):
        self.find(self._close_locator).click()
        return self

    def get_error_msg(self):
        msg = self.find(self._error_msg).text
        print("*** {} ****".format(msg))
        confire_button = (By.XPATH, "//*[contains(@resource-id,'md_buttonDefaultPositive') and @text='确定']")
        self.find(confire_button).click()
        return msg