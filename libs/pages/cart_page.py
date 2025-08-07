from selenium.common import TimeoutException

from libs.base_page import BasePage
from libs.locators.cart_locators import CartLocators


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CartLocators

    def is_about_me_text_visible(self):
        """
        Метод проверки видимости текста 'Обо мне'.
        """
        try:
            return self.check_element_visibility(self.locator.about_me_text).is_displayed()
        except TimeoutException:
            return False

    def is_goods_in_cart_text_visible(self) -> bool:
        """
        Метод проверки видимости текств 'Товары в корзине'
        :return: bool
        """
        try:
            return self.check_element_visibility(self.locator.goods_in_cart).is_displayed()
        except TimeoutException:
            return False

    def extract_text_from_web_element_sum(self) -> str:
        """
        Метод извлечения текста из веб-элемента "Сумма"
        """
        return self.check_element_visibility(self.locator.sum).text

    def extract_text_from_web_element_full_sum(self) -> str:
        """
        Метод извлечения текста из веб-элемента "Сумма итого"
        """
        return self.check_element_visibility(self.locator.full_sum).text
