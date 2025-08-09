from selenium.common import TimeoutException

from libs.base_page import BasePage
from libs.locators.good_page_locators import GoodPageLocators


class GoodPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = GoodPageLocators

    def click_in_cart_button(self):
        """
        Метод клика по кнопке 'В корзину'
        """
        self.find_clickable_element(self.locator.in_cart_button).click()

    def is_not_available_text_visible(self) -> bool:
        """
        Метод проверки видимости текста "Нет в наличии"
        :return: bool
        """
        try:
            return self.check_element_visibility(self.locator.not_available_text).is_displayed()
        except TimeoutException:
            return False

    def is_notify_me_button_visible(self) -> bool:
        """
        Метод проверки видимости кнопки "Оповестить меня"
        :return: bool
        """
        try:
            return self.check_element_visibility(self.locator.notify_me_btn).is_displayed()
        except TimeoutException:
            return False
