# 第五部，创建测试用例
import pytest

from page_object.pages.app import App
from page_object.pages.main_page import MainPage


class TestSelected():

    def test_price(self):
        assert App.main().gotoSelect().getPriceByName("中芯国际") == 17.40

    def test_add_stock(self):
        pass