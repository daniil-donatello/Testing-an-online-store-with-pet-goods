from selenium.common import TimeoutException

from libs.base_page import BasePage
from libs.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = MainPageLocators

    def is_main_logo_visible(self) -> bool:
        """
        Метод проверки видимости логотипа сайта.
        :return: bool
        """
        try:
            return self.check_element_visibility(self.locator.main_logo).is_displayed()
        except TimeoutException:
            return False

    def click_account_logo(self):
        self.find_clickable_element(self.locator.account_logo).click()

    def click_drop_menu_btn(self):
        """
        Метод клика по кнопке раскрывающегося меню.
        """
        self.find_clickable_element(self.locator.drop_menu_btn).click()

    def click_fly_food_menu_item(self):
        """
        Метод клика по пункту меню 'Сухие корма'.
        """
        self.find_clickable_element(self.locator.fly_food).click()

    def click_wet_food_menu_item(self):
        """
        Метод клика по пункту меню 'Влажный корм, паучи, консервы'.
        """
        self.find_clickable_element(self.locator.wet_food).click()
