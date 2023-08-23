import pytest
from selenium import webdriver
from pages.login_page import LoginPage
import time


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_email()
    page.enter_password()
    page.submit_login()
    time.sleep(3)


