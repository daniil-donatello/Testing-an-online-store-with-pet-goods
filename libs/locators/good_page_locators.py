from selenium.webdriver.common.by import By


class GoodPageLocators:
    in_cart_button = (By.XPATH, '(//button[contains(text(), "корзину")])[1]')
    not_available_text = (By.XPATH, '//div[contains(text(), "Нет в наличии")]')
    notify_me_btn = (By.XPATH, '//a[contains(text(), "Оповестить меня")]')
