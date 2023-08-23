from pages.details_page import DetailsPage
import time
import pytest


@pytest.mark.details
def test_details(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = DetailsPage(browser, link)
    page.open()
    page.ddl_open()
    time.sleep(1)
    page.ddl_select()
    time.sleep(1)
    page.pet_details()
    time.sleep(3)
    browser.save_screenshot('result_pet_details.png')


@pytest.mark.details
def test_picture(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = DetailsPage(browser, link)
    page.open()
    page.ddl_open()
    time.sleep(1)
    page.ddl_select()
    time.sleep(1)
    page.pet_details()
    time.sleep(1)
    page.pet_open_picture()
    time.sleep(2)
    page.pet_picture_action_left()
    time.sleep(1)
    page.pet_picture_action_right()
    time.sleep(1)
    page.pet_picture_zoom_in()
    time.sleep(1)
    page.pet_picture_zoom_out()
    time.sleep(1)
    page.pet_picture_close()
    time.sleep(1)
    browser.save_screenshot('result_test_picture.png')
