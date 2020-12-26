from .pages.main_page import MainPage as mp
from .pages.login_page import LoginPage as lp
from .pages.basket_page import BasketPage as bp
import  pytest

@pytest.mark.skip
def test_quest_can_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = mp(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = lp(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = mp(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket()
    basket_page = bp(browser, browser.current_url)
    basket_page.checking_an_empty_basket()
    basket_page.checking_empty_cart_messages()

def test_guest_cant_see_product_in_basket_opened_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    page = mp(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = bp(browser, browser.current_url)
    basket_page.checking_an_empty_basket()
    basket_page.checking_empty_cart_messages()


