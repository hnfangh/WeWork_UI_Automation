# coding=utf-8

from appium.webdriver.common.mobileby import MobileBy
from page.base_page import BasePage
from page.contacts import Contacts


class Main(BasePage):


    def goto_messege(self):
        pass

    def goto_contacts(self):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return Contacts(self._driver)


    def goto_workbench(self):
        pass

    def goto_myinfo(self):
        pass

