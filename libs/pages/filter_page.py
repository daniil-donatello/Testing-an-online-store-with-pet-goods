from selenium.common import TimeoutException

from libs.base_page import BasePage
from libs.locators.filter_page_locators import FilterPageLocators


class FilterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = FilterPageLocators

    def click_feed_parameter(self, text: str):
        """
        Метод клика по параметру корма.
        :param text: название параметра корма.
        :return:
        """
        self.find_clickable_element(self.locator.select_feed_parameter(text)).click()

    def click_show_extended_button(self, number: int):
        """
        Метод клика по кнопке 'Показать еще'.
        :param number: номер кнопки 'Показать еще'.
        :return:
        """
        self.find_clickable_element(self.locator.select_show_extended_button(number)).click()
