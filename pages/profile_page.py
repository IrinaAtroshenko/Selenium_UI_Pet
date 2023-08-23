from .locators import ProfilePageLocators
from .base_page import BasePage


class ProfilePage(BasePage):

    def plus_btn(self):
        self.browser.find_element(*ProfilePageLocators.PLUS_BTN).click()

    def name_field(self):
        self.browser.find_element(*ProfilePageLocators.NAME_FIELD).send_keys('Cherry')

    def age_field(self):
        self.browser.find_element(*ProfilePageLocators.AGE_FIELD).send_keys('2')

    def type_ddl(self):
        self.browser.find_element(*ProfilePageLocators.TYPE_DDL).click()

    def type_ddl_select(self):
        self.browser.find_element(*ProfilePageLocators.TYPE_DDL_SELECT).click()

    def gender_ddl(self):
        self.browser.find_element(*ProfilePageLocators.GENDER_DDL).click()

    def gender_ddl_select(self):
        self.browser.find_element(*ProfilePageLocators.GENDER_DDL_SELECT).click()

    def create_pet_btn(self):
        self.browser.find_element(*ProfilePageLocators.CREATE_PET_BTN).submit()

    def edit_pet_btn(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_PET_BTN).click()

    def edit_name_field(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_NAME_FIELD).clear()
        self.browser.find_element(*ProfilePageLocators.EDIT_NAME_FIELD).send_keys('Potato')

    def edit_age_field(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_AGE_FIELD).clear()
        self.browser.find_element(*ProfilePageLocators.EDIT_AGE_FIELD).send_keys('1')

    def edit_type_ddl(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_TYPE_DDL).click()

    def edit_type_ddl_select(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_TYPE_DDL_SELECT).click()

    def save_edit(self):
        self.browser.find_element(*ProfilePageLocators.SAVE_PET_BTN).click()

    def pet_delete(self):
        self.browser.find_element(*ProfilePageLocators.PET_DELETE).click()

    def yes_pop_up_delete(self):
        self.browser.find_element(*ProfilePageLocators.DELETE_POP_UP).click()


