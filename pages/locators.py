from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR,".btn-group>a.btn.btn-default")

class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    ALLERT_SUCCES = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success .alertinner strong")
    NAME_GOODS = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    ALLERT_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info .alertinner p:nth-child(1) strong")
    PRICE_GOODS = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alert.alert-safe.alert-noicon.alert-success.fade.in")

class BasketPageLocators():
    MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    GOODS = (By.CSS_SELECTOR, "#basket_formset .basket-items")