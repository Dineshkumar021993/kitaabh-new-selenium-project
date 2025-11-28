from pages.desktop.keyboard_navigation import select_organisation
from pages.desktop.new_ledgers_keyboard_navigation import LedgersListKeyBoardNavigation,Transcations,LoginPage

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

def test_ledgers_list(browser):
    ledgers_list_navigation = LedgersListKeyBoardNavigation(browser)
    ledgers_list_navigation.ledgers_list()
    # ledgers_list_navigation.ledgers_list_10_1()
    # ledgers_list_navigation.ledgers_list_20()
    # ledgers_list_navigation.ledgers_list_20_1_sec()
    # ledgers_list_navigation.ledgers_list_50()
    # ledgers_list_navigation.ledgers_list_50_1_sec()

def test_ledgers_list_side_panel(browser):
    transcations_side_panel_ledgers_list = Transcations(browser)
    transcations_side_panel_ledgers_list.transcations()





