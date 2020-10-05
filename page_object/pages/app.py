from page_object.drivers.android_client import AndroidClient
from page_object.pages.main_page import MainPage


class App():
    #负责初始化
    @classmethod
    def main(self):
        AndroidClient.install_app()
        return MainPage()

