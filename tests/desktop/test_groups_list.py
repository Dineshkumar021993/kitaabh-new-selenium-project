from pages.desktop.keyboard_navigation import LoginPage,select_organisation
from pages.desktop.groups_list import GroupsKeyBoardNavigation,SidePanel

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

def test_ledgers_list(browser):
    GroupsKeyBoardNavigation_elements = GroupsKeyBoardNavigation(browser)
    GroupsKeyBoardNavigation_elements.groups_list_keyboard_navigation()
    GroupsKeyBoardNavigation_elements.groups_list_20()

def test_side_panel(browser):
    sidepanel = SidePanel(browser)
    sidepanel.subgroups_and_ledgers_and_group_transcations()


