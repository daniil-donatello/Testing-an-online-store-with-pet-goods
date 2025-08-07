from selenium.webdriver.common.by import By


class AuthorizePageLocators:
    login_field = (By.XPATH, '//input[@name="email"]')
    password_field = (By.XPATH, '//input[@name="password"]')
    log_in_button = (By.XPATH, '//input[@value="Войти"]')
    account_logo_text = (By.XPATH, '//h1[@class="text-center"]')