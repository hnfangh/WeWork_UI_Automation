


from appium import webdriver
from selenium.webdriver.common.by import By


class TestWeiXin:


    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardowm(self):
        self.driver.quit()


    def test_weixin_add_contacts(self):
        """
        1. 点击通讯录
        2. 滑动到底部，点击添加成员
        3. 点击手动输入添加
        4. 输入姓名，手机
        5. 点击保存
        :return:
        """

        self.driver.find_element(By.XPATH, "//*[@text='通讯录']").click()
        # 滚动查询，并点击
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        self.driver.find_element(By.ID, "com.tencent.wework:id/ipb").click()
        self.driver.find_element(By.ID, "com.tencent.wework:id/b7m").send_keys("alis")
        self.driver.find_element(By.ID, "com.tencent.wework:id/fwi").send_keys("18018001800")
        self.driver.find_element(By.ID, "com.tencent.wework:id/aj_").click()

        print('**************')








