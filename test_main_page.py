from .pages.main_page import MainPage as mp

def test_quest_can_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = mp(browser, link)
    page.open()
    page.go_to_login_page()
