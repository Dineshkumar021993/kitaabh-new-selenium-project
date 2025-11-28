from pages.desktop.XLUtils import setup_logger
from pages.desktop.login_page import LoginPage
import pytest

logger = setup_logger()

def test_successful_login(browser):
    login_page = LoginPage(browser)
    try:
        login_page.enter_username()
        # login_page.click_NextButton()
        login_page.enter_password()
        login_page.click_login_button()
        logger.info("Test Passed: Login successful")
    except Exception as e:
        logger.error(f"Test Failed: Login failed due to {e}", exc_info=True)
        pytest.fail(f"Login test failed: {e}")
