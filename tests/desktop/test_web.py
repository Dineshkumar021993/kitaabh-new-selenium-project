from pages.desktop.login_page import LoginPage
from pages.desktop.web import Ledgers

def test_successful_login(browser):
    login_page = LoginPage(browser)
    # Navigate to the login page

    login_page.enter_username()
    login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()

def test_ledgers(browser):
    ledgers_page = Ledgers(browser)
    # ledgers_page.click_on_ledgers()
    ledgers_page.check_underline()
    # ledgers_page.voucher_date_transcations()

