from selenium.webdriver.common.by import By
from page_object.pages.base_page import BasePage
from page_object.pages.profile_page import ProfilePage
from page_object.pages.search_page import SearchPage
from page_object.pages.selected_page import SelectedPage


class MainPage(BasePage):
    # 在实际中，可以现在appium desktop中把元素都确认好，先摘除这样的私有变量，后面在补方法
    _hangqing = (By.XPATH, "//*[@text='行情']")
    _searchbutton = (By.ID, "home_search")
    _profilebutton = (By.XPATH, "//*[contains(@resource-id,'tab_name') and @text='我的']")

    def gotoSelect(self):
        self.find(self._hangqing).click()
        return SelectedPage()

    def gotoSearch(self) -> SearchPage:
        self.find(self._searchbutton).click()
        return SearchPage()

    def gotoProfile(self) -> ProfilePage:
        # self.find(self._profilebutton).click()
        # yaml改造
        self.load_step('../data/main_page.yaml', 'gotoProfile')
        return ProfilePage()