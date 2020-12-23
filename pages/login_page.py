from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in str(self.browser.current_url), 'Login is not in the link'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN), "Login not found"
        assert self.is_element_present(*LoginPageLocators.PASSWORD), "Login password not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.EMAIL), "Login for registration not found"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD), "Registration password not found"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_2), "Repeated registration password not found"