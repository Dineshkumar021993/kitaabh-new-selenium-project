import pytest

from pages.desktop.login_page import LoginPage
from pages.desktop.attachments import PraticeAttachments,auto_update

# def test_tooltip_click(browser):
#     auto_update1 = auto_update(browser)
#     auto_update1.auto_update_tool_tip()

def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)
    # Navigate to the login page

    login_page.enter_username()
    login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()

def test_attachments(browser):
    pratice = PraticeAttachments(browser)
    pratice.Click_CreateButton_On_MainPage()
    pratice.Click_masters_in_create_ledger()
    pratice.Click_ledgers_button()
    pratice.click_attachments()
    # pratice.sales_voucher(pratice.click_on_accounting_vouchers)
    # pratice.click_on_sales_vouchers()





