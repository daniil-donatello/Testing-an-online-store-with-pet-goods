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
