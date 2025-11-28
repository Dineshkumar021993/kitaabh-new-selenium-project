from pages.desktop.gstr_9 import LoginPage,gstr

def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)

    # Navigate to the login page
    login_page.enter_username()
    # login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()

def test_year_toggle_button(browser):
    gstr_9 = gstr(browser)
    gstr_9.year_date_toggle()
    gstr_9.check_gst_in_dropdown()
    gstr_9.check_child_items_displaying()
    gstr_9.first_feild_and_its_items()


