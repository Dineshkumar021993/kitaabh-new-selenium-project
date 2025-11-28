from pages.desktop.login_page import LoginPage
from pages.desktop.Receiptvoucher import ReceiptVoucher


def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)

    # Navigate to the login page
    login_page.enter_username()
    login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()


def test_select_organisation_and_enter_gst(browser):
    receipt_voucher = ReceiptVoucher(browser)
    receipt_voucher.organisation_selection()
    receipt_voucher.click_on_alpha_adarsh()
    receipt_voucher.click_on_create_button_element()
    receipt_voucher.select_on_receipt_transcation_type()
    receipt_voucher.click_on_Amount_received_from()

