from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time


import pytest

# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
link_list = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
             pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                          marks=pytest.mark.xfail),
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.link_login = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        self.link_product = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = LoginPage(browser, self.link_login)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, 'fakepas999')

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link_product)
        page.open()
        page.checking_an_authorized_user()
        page.add_item_to_cart()
        #page.should_not_be_success_message()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link_product)
        page.open()
        page.checking_an_authorized_user()
        page.should_not_be_success_message()




@pytest.mark.skip
@pytest.mark.parametrize('link', link_list)
def test_checking_the_price_of_goods(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    page.checking_the_message_about_adding_goods()
    page.checking_the_price_of_goods()

@pytest.mark.skip
def test_message_disappearance(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    page.element_disappeared()


def test_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
