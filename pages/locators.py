from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")