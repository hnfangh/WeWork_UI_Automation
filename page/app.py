from appium import webdriver
from page.base_page import BasePage
from page.main import Main


class App(BasePage):

    def start(self):
        if self._driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.WwMainActivity'
            desired_caps['noReset'] = True

            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(5)

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        return Main(self._driver)




