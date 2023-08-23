from pages.profile_page import ProfilePage
from conftest import test_go_to_login
import time
import pytest


@pytest.mark.pet_action
def test_add_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.plus_btn()
    time.sleep(1)
    page.name_field()
    time.sleep(1)
    page.age_field()
    time.sleep(1)
    page.type_ddl()
    time.sleep(1)
    page.type_ddl_select()
    time.sleep(1)
    page.gender_ddl()
    time.sleep(1)
    page.gender_ddl_select()
    time.sleep(1)
    page.create_pet_btn()
    time.sleep(1)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(1)
    browser.save_screenshot('result_pet_created.png')


@pytest.mark.pet_action
def test_edit_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.edit_pet_btn()
    time.sleep(1)
    page.edit_name_field()
    time.sleep(1)
    page.edit_age_field()
    time.sleep(1)
    page.edit_type_ddl()
    time.sleep(1)
    page.edit_type_ddl_select()
    time.sleep(1)
    page.save_edit()
    time.sleep(1)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(1)
    browser.save_screenshot('result_pet_edited.png')


@pytest.mark.pet_action
def test_delete_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.pet_delete()
    time.sleep(1)
    page.yes_pop_up_delete()
    time.sleep(1)
    browser.save_screenshot('result_pet_delete.png')

