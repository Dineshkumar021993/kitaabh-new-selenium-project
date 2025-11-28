from pages.desktop.keyboard_navigation import LoginPage,select_organisation
from pages.desktop.costcentre import CostCentreKeyboardNavigationList

def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)

    # Navigate to the login page
    login_page.enter_username()
    login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()

def test_select_organisation(browser):
    select_organisation_click = select_organisation(browser)
    select_organisation_click.select_organisation_element()

def test_cost_center_list(browser):
    cost_centre_list = CostCentreKeyboardNavigationList(browser)
    cost_centre_list.cost_center_keyboard_navigation()
