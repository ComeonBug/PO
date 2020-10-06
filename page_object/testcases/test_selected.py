# 第五部，创建测试用例
import time

import pytest

from page_object.pages.app import App
from page_object.pages.main_page import MainPage


class TestSelected():
    main_page: MainPage

    @classmethod
    def setup_class(cls):
        cls.main_page = App.main()

    def setup_method(self):
        self.main_page = TestSelected.main_page
        self.search_page = self.main_page.gotoSearch()

    def teardown_method(self):
        print("*****  tear down method  ******")
        self.search_page.cancel()
        time.sleep(5)

    def test_price(self):
        assert self.main_page.gotoSelect().getPriceByName("中芯国际") == 17.40

    def test_add_stock(self):
        search_reuslt = self.search_page.search("阿里巴巴")
        assert search_reuslt.is_selected("BABA") == True
        assert search_reuslt.is_selected("09988") == False

    def test_follow(self):
        username = "涨不停不停涨888"
        # 关注了返回True
        assert self.search_page.searchByName(username).is_followed(username) == True

    @pytest.mark.parametrize("key, code", [
        ("招商银行", "SH600036"),
        ("平安银行", "SZ000001"),
        ("pingan", "SH601318"),
    ])
    def test_is_selected_hs(self, key, code):
        search_page = self.search_page.search(key, code)
        assert search_page.is_selected(code) == True

    @pytest.mark.parametrize("key, code", [("招商银行", "SH600036")])
    def test_is_selected_hc(self, key, code):
        search_page = self.search_page.search(key, code)
        if not search_page.is_selected(code):
            search_page.add_selected(code)
        else:
            search_page.remove_select(code).add_selected(code)
        assert search_page.is_selected(code) == True

    def teardown_class(self):
        self.main_page.driver.quit()
