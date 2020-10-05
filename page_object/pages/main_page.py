# 第一步MainPage
from page_object.drivers.android_client import install_app
from page_object.pages.selected_page import SelectedPage


class MainPage():
    def __init__(self):
        pass
    # 第二步，选了一个要测试的页面
    def gotoSelect(self):
        # 返回一个page对象
        install_app().find_element_by_xpath("//*[@text='行情']").click()
        # self.driver.find_element_by_xpath("//*[@text='自选']")

        return SelectedPage()