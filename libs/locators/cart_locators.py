from selenium.webdriver.common.by import By


class CartLocators:
    about_me_text = (By.XPATH, '//h1[text()="Обо мне"]')
    goods_in_cart = (By.XPATH, '//h1[contains(text(), "Товары в корзине")]')
    sum = (By.XPATH, '//*[contains(@id, "summa")]')
    full_sum = (By.XPATH, '//*[@class="cart-full-summa"]')
