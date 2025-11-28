from pages.desktop.datadriventestingpart1 import LoginPage


def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)
    login_page.login()
