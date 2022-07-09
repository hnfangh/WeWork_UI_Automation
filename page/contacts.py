from page.base_page import BasePage


class Contacts(BasePage):



    def goto_add_member(self):
        from page.memberinvite import MemberInviteMenu
        self._driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        return MemberInviteMenu(self._driver)


