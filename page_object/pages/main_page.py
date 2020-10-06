# 第一步MainPage
from selenium.webdriver.common.by import By
from page_object.pages.base_page import BasePage
from page_object.pages.search_page import SearchPage
from page_object.pages.selected_page import SelectedPage


class MainPage(BasePage):
    # 第二步，选了一个要测试的页面
    def gotoSelect(self):
        # 返回一个page对象
        # hangqing = (By.XPATH, "//*[@text='行情']")
        hangqing = self.findByText("行情")
        self.find(hangqing).click()
        # self.driver.find_element_by_xpath("//*[@text='行情']").click()
        return SelectedPage()

    def gotoSearch(self):
        searchbutton = (By.ID, "home_search")
        self.find(searchbutton).click()
        return SearchPage()