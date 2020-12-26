from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_item_to_cart(self):
        basket = self.is_element_present(*ProductPageLocators.ADD_TO_BASKET)
        assert basket == True, 'Кнопка добавления в корзину не отбражается\n' + self.browser.current_url
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def checking_the_message_about_adding_goods(self):
        name_goods = self.browser.find_element(*ProductPageLocators.NAME_GOODS).text
        message = self.browser.find_element(*ProductPageLocators.ALLERT_SUCCES).text
        assert name_goods == message, 'Название товара не совпадает с названием в сообщении\n' + self.browser.current_url

    def checking_the_price_of_goods(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_GOODS).text
        message_basket = self.browser.find_element(*ProductPageLocators.ALLERT_BASKET).text
        assert price == message_basket, 'Цена товара не совпадает с ценой в сообщении\n' + self.browser.current_url

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be\n" + self.browser.current_url

    def element_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear\n" + self.browser.current_url

