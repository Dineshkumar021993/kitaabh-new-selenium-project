from pages.desktop.create_organisation_and_organisation_settings import LoginPage,CreateOrganisation

def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)

    # Navigate to the login page
    login_page.enter_username()
    login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()

# def test_create_organisation(browser):
    # create_organisation = CreateOrganisation(browser)
    # create_organisation.click_create_organisation_button_after_login()
    # create_organisation.legal_name_element()
    # create_organisation.legal_name_attribute()
    # create_organisation.alias_name_feild()
    # create_organisation.alias_feild_attribute_value()
    # create_organisation.country_feild()
    # create_organisation.country_feild_attribute_value()
    # create_organisation.currency()
    # # create_organisation.alias_comparsion_from_main_page_to_alias_in_primary()
    # # create_organisation.country_and_currency_to_main_to_feilds_in_primary_details()
    # create_organisation.configuration_in_primary_details()
    # create_organisation.Features_all_feilds()
    # create_organisation.click_on_inventory_elements()
    # create_organisation.GST_feild_in_primary_details()
    # create_organisation.GST_remaining_feilds()
    # create_organisation.Default_rates_all()
    # create_organisation.E_way_bill()
    # create_organisation.tds_in_organisation_settings()
    # create_organisation.click_on_tcs()
    # create_organisation.other_statutory()
    # create_organisation.MSME()
    # create_organisation.branding()
    # create_organisation.Address_all_feilds()


