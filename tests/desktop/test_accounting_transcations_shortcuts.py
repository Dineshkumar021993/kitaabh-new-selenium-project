from pages.desktop.accounting_transcations_shortcuts import AllAccountingTranscations
from pages.desktop.login_page import LoginPage


def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)

    # Navigate to the login page
    login_page.enter_username()
    login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()


def test_transcations_all(browser):
    all_accounting_transcations = AllAccountingTranscations(browser)
    all_accounting_transcations.all_transcations_list()
    all_accounting_transcations.sales()
    all_accounting_transcations.payments()
    all_accounting_transcations.journals()
    all_accounting_transcations.receipt()
    all_accounting_transcations.contra()
    all_accounting_transcations.debit_note()
    all_accounting_transcations.credit_note()


