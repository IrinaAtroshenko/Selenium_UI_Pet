from pages.main_page import MainPage
import time


def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(3)
    browser.save_screenshot('result_login_page.png')


def test_ddl(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.ddl_open()
    time.sleep(1)
    page.ddl_select()
    time.sleep(3)
    browser.save_screenshot('result_ddl_select.png')


def test_filter_by_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_name()
    time.sleep(3)
    browser.save_screenshot('result_filter_by_name.png')
