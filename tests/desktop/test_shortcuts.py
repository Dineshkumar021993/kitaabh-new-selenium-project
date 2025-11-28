from pages.desktop.login_page import LoginPage
from pages.desktop.shortcuts import Dashboard
from pages.desktop.shortcuts import LedgersList




def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)

    # Navigate to the login page
    login_page.enter_username()
    login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()

def test_dashboard(browser):
    dashboard = Dashboard(browser)
    dashboard.click_on_kitaab_image()
    dashboard.check_masters()
    dashboard.click_on_Transcations()
    dashboard.click_on_Reports()
    dashboard.gst_highlighting_element()
    dashboard.other_statutory_element()
    dashboard.Audit_highliting()
    dashboard.record_keeping_highlighting()

def test_ledgers_list(browser):
    ledgerslist = LedgersList(browser)
    ledgerslist.click_on_kitaab_image()
    ledgerslist.ledgers_list_count()














