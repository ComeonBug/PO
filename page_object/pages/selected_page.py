# 第三步，组织这个页面
from page_object.drivers.android_client import AndroidClient


class SelectedPage():
    # 第四部：写这个页面的可能的方法，实现
    def addDefault(self):
        return self

    # 第四部：写这个页面的可能的方法，实现
    def getPriceByName(self, name):
        #todo
        print(name)
        price = install_app().find_element_by_xpath('//*[@text="' + name + '" ]/../../../..//*[contains(@resource-id,"item_layout")]').text
        return float(price)
