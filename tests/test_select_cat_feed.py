import time

from libs.checks.checks import Checks
from libs.enums.emails import Emails
from libs.enums.food_purpose import FoodPurpose
from libs.enums.good_type import GoodType
from libs.enums.food_brand import FoodBrand
from libs.enums.country import Country
from libs.enums.age import Age
from libs.enums.feed_class import FeedClass
from libs.enums.passwords import Passwords
from libs.pages.filter_page import FilterPage
from libs.pages.feed_page import FeedPage
from libs.pages.good_page import GoodPage
from libs.locators.filter_page_locators import FilterPageLocators
from libs.pages.cart_page import CartPage
from libs.pages.main_page import MainPage
from libs.pages.authorize_page import AuthorizePage


def test_select_feed_for_cat(browser_chrome):

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

    # Выбор в главном меню 'Сухого корма для кошек'
    Checks.is_true(cart_page.is_about_me_text_visible())
    main_page.click_drop_menu_btn()
    main_page.click_fly_food_menu_item()

    # Настройка фиильтра для кормов
    filter_page.click_and_hold_element(filter_page_locators.slider_price, -60, 0)
    filter_page.click_and_hold_element(filter_page_locators.slider_weight, -50, 0)
    filter_page.move_to_element_by_offset(0, 300)
    filter_page.click_feed_parameter(FoodPurpose.FOR_SKIN.value)

    filter_page.move_to_element_by_offset(0, 400)
    filter_page.click_show_extended_button(1)
    filter_page.click_feed_parameter(FoodPurpose.ALLERGY.value)
    filter_page.click_feed_parameter(FoodPurpose.HAIR_REMOVAL.value)

    filter_page.move_to_element_by_offset(0, 600)
    time.sleep(2)
    filter_page.click_feed_parameter(GoodType.FLY_FEED.value)
    filter_page.move_to_element_by_offset(0, 600)

    filter_page.click_feed_parameter(FoodBrand.ROYAL_CANIN.value)
    filter_page.move_to_element_by_offset(0, 900)

    filter_page.click_feed_parameter(Country.RUSSIA.value)
    filter_page.move_to_element_by_offset(0, 1000)
    time.sleep(2)
    filter_page.click_feed_parameter(Age.ADULTS.value)
    filter_page.click_feed_parameter(FeedClass.SUPER_PREMIUM.value)
    filter_page.move_to_element_by_offset(0, -1000)

    # Переход на страницу корма
    time.sleep(1)
    feed_page.click_on_cat_feed()

    good_page.move_to_element_by_offset(0, 500)
    time.sleep(1)
    good_page.click_in_cart_button()
    browser_chrome.get('https://www.zootovar-spb.ru/cart.html')
    Checks.is_true(cart_page.is_goods_in_cart_text_visible())

    # Сравнение итоговой суммы корма и суммы корма в корзине
    Checks.equality(
        cart_page.extract_text_from_web_element_full_sum(),
        cart_page.extract_text_from_web_element_sum()
    )

    time.sleep(5)
