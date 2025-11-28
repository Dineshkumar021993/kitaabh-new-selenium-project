from pages.desktop.keyboard_navigation import select_organisation
from pages.desktop.create_payment_data_driven_testing import Payment,LoginPage

def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)

    # Navigate to the login page
    login_page.enter_username()
    # login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()

def test_select_organisation(browser):
    select_organisation_click = select_organisation(browser)
    select_organisation_click.select_organisation_element()

def test_search_feild(browser):
    payment_feild = Payment(browser)
    payment_feild.click_on_create_button_and_click_payment()
    payment_feild.search_feild()
    payment_feild.switch_transcation_type_button_in_search()
    payment_feild.click_on_new_button()
    payment_feild.create_new_alt_c()
    payment_feild.regular_draft()
    payment_feild.gst_in_values()
    payment_feild.single_double_slider()
    payment_feild.date_feild()
    payment_feild.transcation_no()
    payment_feild.payment_paid_to_data_driven_test_drop_down()
    payment_feild.payment_paid_to()
    payment_feild.ledger_details_cost_details_cost_details()
    payment_feild.click_on_us_dollar()





