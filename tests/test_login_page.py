import time
from pages.login_page import LoginPage
import pytest


@pytest.mark.login
def test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_email()
    page.enter_password()
    page.submit_login()
    time.sleep(5)
    browser.save_screenshot("./Selenium_UI_Pet/result_login.png")
