import time

from libs.checks.checks import Checks
from libs.enums.emails import Emails
from libs.enums.food_purpose import FoodPurpose
from libs.enums.food_brand import FoodBrand
from libs.enums.age import Age
from libs.enums.feed_class import FeedClass
from libs.enums.passwords import Passwords
from libs.pages.filter_page import FilterPage
from libs.pages.feed_page import FeedPage
from libs.pages.good_page import GoodPage
from libs.enums.packaging_type import PackagingType
from libs.locators.filter_page_locators import FilterPageLocators
from libs.pages.cart_page import CartPage
from libs.pages.main_page import MainPage
from libs.pages.authorize_page import AuthorizePage


def test_select_cat_wet_feed(browser_chrome):

    main_page = MainPage(browser_chrome)
    auth_page = AuthorizePage(browser_chrome)
    cart_page = CartPage(browser_chrome)
    filter_page = FilterPage(browser_chrome)
    filter_page_locators = FilterPageLocators()
    feed_page = FeedPage(browser_chrome)
    good_page = GoodPage(browser_chrome)

    # Авторизациия
    Checks.is_true(main_page.is_main_logo_visible())
    main_page.click_account_logo()
    Checks.is_true(auth_page.is_account_logo_visible())
    time.sleep(1)
    auth_page.fill_login_field(Emails.main_user.value)
    time.sleep(1)
    auth_page.fill_password_field(Passwords.main_user_password.value)
    auth_page.click_log_in_button()

    # Выбор в главном меню 'Влажного корма для кошек'
    Checks.is_true(cart_page.is_about_me_text_visible())
    main_page.click_drop_menu_btn()
    main_page.click_wet_food_menu_item()

    # Настройка фиильтра для кормов
    filter_page.click_and_hold_element(filter_page_locators.slider_price, -40, 0)
    time.sleep(2)
    filter_page.move_to_element_by_offset(0, 300)
    filter_page.click_feed_parameter(FoodPurpose.STERILIZED.value)
    filter_page.click_feed_parameter(FoodPurpose.CASTRATES.value)

    filter_page.move_to_element_by_offset(0, 600)
    filter_page.click_feed_parameter(FoodBrand.PURINA_PRO_PLAN.value)

    filter_page.move_to_element_by_offset(0, 600)
    time.sleep(2)
    filter_page.click_feed_parameter(Age.ADULTS.value)
    time.sleep(2)
    filter_page.move_to_element_by_offset(0, 600)
    time.sleep(2)
    filter_page.click_feed_parameter(FeedClass.SUPER_PREMIUM.value)
    time.sleep(2)
    filter_page.move_to_element_by_offset(0, 600)
    time.sleep(2)
    filter_page.click_feed_parameter(PackagingType.PAUCH.value)

    # Переход на страницу корма
    time.sleep(2)
    feed_page.click_on_cat_wet_feed()

    good_page.move_to_element_by_offset(0, 500)
    time.sleep(1)
    Checks.is_true(good_page.is_not_available_text_visible())
    Checks.is_true(good_page.is_notify_me_button_visible())

    time.sleep(5)