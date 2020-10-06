import pytest

from page_object.pages.app import App


class TestLogin():
    @classmethod
    def setup_class(cls):
        cls.profile_page = App.main().gotoProfile()

    def setup_method(self):
        self.login_page = self.profile_page.gotologin()

    @pytest.mark.parametrize("username, password", [("ly", "123456"),("test","000000")])
    def test_error_username_login(self, username, password):
        self.login_page.login_error_by_userinfo(username, password)
        assert "错误" in self.login_page.get_error_msg()

    def teardown_method(self):
        self.login_page.back()