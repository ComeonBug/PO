from page_object.drivers.client import AndroidClient
from page_object.pages.base_page import BasePage
from page_object.pages.main_page import MainPage


class App(BasePage):
    #负责初始化
    @classmethod
    def main(cls) -> MainPage:
        cls.get_client().install_app()
        return MainPage()

