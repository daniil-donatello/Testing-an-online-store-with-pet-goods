from selenium.webdriver.common.by import By


class GoodPageLocators:
    in_cart_button = (By.XPATH, '(//button[contains(text(), "корзину")])[1]')
