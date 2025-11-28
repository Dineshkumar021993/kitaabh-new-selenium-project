from pages.desktop.keyboard_navigation import LoginPage,select_organisation

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
    select_organisation_click.keyboard_navigation_ledgers_list()


