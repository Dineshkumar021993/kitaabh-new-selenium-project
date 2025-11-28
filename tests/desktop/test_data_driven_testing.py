from pages.desktop.datadriventest import LoginPage
from pages.desktop.datadriventest import Ledger
from pages.desktop.login_page import LoginPage

def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)
    login_page.login()

def test_successful_login1(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)

    # Navigate to the login page
    login_page.enter_username()
    login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()

def test_ledger_all(browser):
    ledger = Ledger(browser)
    # ledger.ledger_all()
