# 第五部，创建测试用例
import pytest

from page_object.pages.app import App
from page_object.pages.main_page import MainPage


class TestSelected():

    def test_price(self):
        assert App.main().gotoSelect().getPriceByName("中芯国际") == 17.40

    def test_add_stock(self):
        search_page = App.main().gotoSearch().search("阿里巴巴")
        assert search_page.is_selected("BABA") == True
        assert search_page.is_selected("09988") == False

    def teardown_class(self):
        App.main().driver.quit()