from selenium.webdriver.common.by import By


class MainPageLocators:
    main_logo = (By.XPATH, '//div[@id="topLogoBlock"]')
    account_logo = (By.XPATH, '(//*[contains(text(), "Войти")])[last()]')
    drop_menu_btn = (By.XPATH, '//a[@id="dropMainMenuBtn"]')
    fly_food = (By.XPATH, '(//a[contains(text(), "Сухие корма")])[1]')
    wet_food = (By.XPATH, '(//a[contains(text(), "Влажный корм, паучи, консервы")])[1]')
