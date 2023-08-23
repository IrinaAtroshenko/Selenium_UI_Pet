from .base_page import BasePage
from .locators import DetailsPageLocators
from .locators import MainPageLocators

class DetailsPage(BasePage):

    def ddl_open(self):
        self.browser.find_element(*MainPageLocators.DDL).click()

    def ddl_select(self):
        self.browser.find_element(*MainPageLocators.DDL_SELECT).click()

    def pet_details(self):
        self.browser.find_element(*DetailsPageLocators.PET_DETAILS).click()

    def pet_open_picture(self):
        self.browser.find_element(*DetailsPageLocators.PET_OPEN_PICTURE).click()

    def pet_picture_action_left(self):
        self.browser.find_element(*DetailsPageLocators.PET_PICTURE_ACTION_LEFT).click()

    def pet_picture_action_right(self):
        self.browser.find_element(*DetailsPageLocators.PET_PICTURE_ACTION_RIGHT).click()

    def pet_picture_zoom_in(self):
        self.browser.find_element(*DetailsPageLocators.PET_PICTURE_ZOOM_IN).click()

    def pet_picture_zoom_out(self):
        self.browser.find_element(*DetailsPageLocators.PET_PICTURE_ZOOM_OUT).click()

    def pet_picture_close(self):
        self.browser.find_element(*DetailsPageLocators.PET_PICTURE_CLOSE).click()