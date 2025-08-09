from selenium.webdriver.common.by import By


class FeedPageLocators:
    feed_purina = (By.XPATH, '(//img[contains(@alt, "Сухой корм для кошек Royal Canin Indoor Long Hair")])[1]')
    wet_feed_purina = (By.XPATH, '(//img[contains(@alt, "Влажный корм Pro Plan Sterilised")])[1]')
