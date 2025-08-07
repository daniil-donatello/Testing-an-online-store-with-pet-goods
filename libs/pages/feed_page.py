from libs.base_page import BasePage
from libs.locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = FeedPageLocators

    def click_on_cat_feed(self):
        """
        Метод клика по кошачьему корму на странице с кормами.
        """
        self.find_clickable_element(self.locator.feed_purina).click()
