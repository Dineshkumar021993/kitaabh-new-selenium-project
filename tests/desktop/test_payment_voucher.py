from pages.desktop.login_page import LoginPage
from pages.desktop.payment_voucher import PaymentVoucher


def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)
    # Navigate to the login page

    login_page.enter_username()
    login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()


def test_click_payment_voucher(browser):
    Payment_voucher_pratice = PaymentVoucher(browser)
    Payment_voucher_pratice.Click_on_payment_voucher()
    Payment_voucher_pratice.create_payment()
    Payment_voucher_pratice.payment_number_series_click()
    Payment_voucher_pratice.create_button_in_create_payment()
    Payment_voucher_pratice.save_new_voucher_type()
    Payment_voucher_pratice.delete_saved_voucher_type()
    Payment_voucher_pratice.check_cancel_button_in_new_derict_page()
    Payment_voucher_pratice.saving_in_regular_mode()
    Payment_voucher_pratice.exchange_button()
    Payment_voucher_pratice.voucher_currency_list_create()
    Payment_voucher_pratice.switch_locator()
    Payment_voucher_pratice.transcation_date()
    Payment_voucher_pratice.transcation_no()
    Payment_voucher_pratice.check_single_double()

