import pytest
from selenium import webdriver


@pytest.fixture
def browser_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    driver = webdriver.Chrome(options)
    driver.set_window_size(1920, 1080)

    driver.get('https://www.zootovar-spb.ru/')

    return driver
