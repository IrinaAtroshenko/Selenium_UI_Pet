from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def ddl_open(self):
        self.browser.find_element(*MainPageLocators.DDL).click()

    def ddl_select(self):
        self.browser.find_element(*MainPageLocators.DDL_SELECT).click()

    def filter_by_name(self):
        self.browser.find_element(*MainPageLocators.PET_FILTER_BY_NAME).send_keys('Tomato', Keys.ENTER)

