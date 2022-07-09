from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.contactadd import ContactAdd


class MemberInviteMenu(BasePage):


    def goto_contactadd(self):
        self.find(By.ID, "com.tencent.wework:id/ipb").click()
        return ContactAdd(self._driver)

    def get_toast(self):
        return self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        # return "toast"
