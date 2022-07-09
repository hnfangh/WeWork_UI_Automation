import logging

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:

    # 弹框处理的定位列表
    logging.basicConfig(level=logging.INFO)

    _black_list = [(By.XPATH, "//*[@text='确认']"),(By.XPATH, "//*[@text='确定']"),(By.XPATH, "//*[@text='下次再说']")]
    _max_num = 3
    _error_num = 0


    def __init__(self, driver: WebDriver=None):
        self._driver = driver


    def find(self, locator, value:str=None):
        logging.info(locator)
        logging.info(value)
        element:WebElement

        try:
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)
            # 找到之前 _erro_num归零
            self._error_num = 0
            # 还原会之前的隐式等待
            self._driver.implicitly_wait(5)
            return element
        except Exception as e:
            # 出现异常，将隐式等待设置小一点，快速处理弹框
            self._driver.implicitly_wait(1)
            # 判断异常处理次数
            if self._error_num > self._max_num:
                raise e
            else:
                self._error_num += 1
            # 处理黑名单里面的弹框
            for ele in self._black_list:
                elelist = self._driver.find_element(*ele)
                if len(elelist)>0:
                    elelist[0].click()
                    #处理完成，再去查找目标元素
                    return self.find(locator, value)
            raise e


    def find_and_text(self, locator, value:str=None):
        element:WebElement
        try:
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator).text
            else:
                element = self._driver.find_element(locator, value).text
            # 找到之前 _erro_num归零
            self._error_num = 0
            # 还原会之前的隐式等待
            self._driver.implicitly_wait(5)
            return element.text
        except Exception as e:
            # 出现异常，将隐式等待设置小一点，快速处理弹框
            self._driver.implicitly_wait(1)
            # 判断异常处理次数
            if self._error_num > self._max_num:
                raise e
            else:
                self._error_num += 1
            # 处理黑名单里面的弹框
            for ele in self._black_list:
                elelist = self._driver.find_element(*ele)
                if len(elelist)>0:
                    elelist[0].click()
                    #处理完成，再去查找目标元素
                    return self.find(locator, value)
            raise e
