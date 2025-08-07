from selenium.webdriver.common.by import By


class FilterPageLocators:
    filter_panel = (By.XPATH, '//div[@id="lfWrap"]')
    slider_price = (By.XPATH, '//*[@id="slider-range"]')
    slider_weight = (By.XPATH, '//*[@id="slider-range_weight"]')
    feed_parameter = (By.XPATH, '//a[contains(text(), "супер")]')

    @staticmethod
    def select_feed_parameter(text: str) -> tuple[str, str]:
        return By.XPATH, f'//a[contains(text(), "{text}")]//ancestor::label'

    @staticmethod
    def select_show_extended_button(number: int) -> tuple[str, str]:
        return By.XPATH, f'(//a[contains(@class, "show-extended")])[{number}]'
