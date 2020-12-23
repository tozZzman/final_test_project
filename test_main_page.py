from .pages.main_page import MainPage as mp
from .pages.login_page import LoginPage as lp

def test_quest_can_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = mp(browser, link)
    page.open()
    page.go_to_login_page()
    link = browser.current_url
    login_page = lp(browser, link)
    login_page.should_be_login_page()