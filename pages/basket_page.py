from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def checking_an_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS), 'Корзина не пуста'

    def checking_empty_cart_messages(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY), 'Нет сообщения о том что корзина пуста'
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY).text
        assert message == 'Ваша корзина пуста Продолжить покупки', 'Ожидаемый текст сообщения "Ваша корзина пуста Продолжить покупки"'


