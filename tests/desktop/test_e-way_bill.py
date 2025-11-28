from pages.desktop.e_waybill import LoginPage, enter_organisation_check_e_way_bill


def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)

    # Navigate to the login page
    login_page.enter_username()
    login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()


def test_create_organisation(browser):
    create_e_way_bill = enter_organisation_check_e_way_bill(browser)
    create_e_way_bill.click_create_organisation_button_after_login()
    create_e_way_bill.e_way_bill_testing_organisation()
    create_e_way_bill.enter_into_gst_module_and_click_e_way_bill()
    create_e_way_bill.from_date_and_to_date()
    # create_e_way_bill.click_on_add_credentials()
    create_e_way_bill.click_all_check_boxes()
    create_e_way_bill.check_filters()
    create_e_way_bill.vouchers_opening_or_not()
    create_e_way_bill.taxable_value_calculation()
    create_e_way_bill.insights()


