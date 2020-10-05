# 第五部，创建测试用例
import pytest
from page_object.pages.main_page import MainPage


class TestSelected():
    def setup_class(self):
        self.main = MainPage()

    def test_price(self):
        assert self.main.gotoSelect().getPriceByName("中芯国际") == 17.28

    def test_add_stock(self):
        pass