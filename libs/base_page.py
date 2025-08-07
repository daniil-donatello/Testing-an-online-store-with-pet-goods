from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def check_element_visibility(self, locator: tuple[str, str]):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def find_clickable_element(self, locator: tuple[str, str]):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def fill_input_field(self, locator: tuple[str, str], text: str):
        self.find_clickable_element(locator).send_keys(text)

    def move_to_element_by_offset(self, x: int, y: int):
        self.driver.execute_script(f"window.scrollTo({x}, {y});")

    def move_to_element(self, locator: tuple[str, str]):
        web_element = self.check_element_visibility(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(web_element).perform()

    def click_and_hold_element(self, locator: tuple[str, str], x: int, y: int):
        web_element = self.check_element_visibility(locator)
        actions = ActionChains(self.driver)
        actions.click_and_hold(web_element).move_by_offset(x, y).release().perform()

