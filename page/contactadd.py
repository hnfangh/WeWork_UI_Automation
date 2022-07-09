from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class ContactAdd(BasePage):


    def send_message(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/b7m").send_keys("alis")
        self.find(MobileBy.ID, "com.tencent.wework:id/fwi").send_keys("18018001800")
        return self

    def click_save(self):
        from page.memberinvite import MemberInviteMenu
        self.find(MobileBy.ID, "com.tencent.wework:id/aj_").click()
        return MemberInviteMenu(self._driver)
