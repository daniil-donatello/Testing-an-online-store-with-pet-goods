from selenium.common import TimeoutException

from libs.base_page import BasePage
from libs.locators.authorize_page_locators import AuthorizePageLocators


class AuthorizePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = AuthorizePageLocators

    def is_account_logo_visible(self) -> bool:
        """
        Метод проверяющий видимость текста 'Вход в лиичный кабинет'.
        :return: bool
        """
        try:
            return self.check_element_visibility(self.locator.account_logo_text).is_displayed()
        except TimeoutException:
            return False

    def fill_login_field(self, text: str):
        """
        Метод заполнения поля 'Email'.
        :param text: текст заполнени поля.
        """
        self.fill_input_field(self.locator.login_field, text)

    def fill_password_field(self, text: str):
        """
        Метод заполнения поля 'Пароль'.
        :param text: текст заполнени поля.
        """
        self.fill_input_field(self.locator.password_field, text)

    def click_log_in_button(self):
        """
        Метод клика по кнопке 'Войти'.
        :return:
        """
        self.find_clickable_element(self.locator.log_in_button).click()
