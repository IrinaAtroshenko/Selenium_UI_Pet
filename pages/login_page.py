from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def enter_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('qwerty_we@gmail.com')
    def enter_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_password.send_keys('@Psw2023@')
    def submit_login(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_button.submit()
