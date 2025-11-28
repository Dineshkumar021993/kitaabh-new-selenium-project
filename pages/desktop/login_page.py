import json
import os

import allure
from selenium.common.exceptions import (
    NoSuchElementException, TimeoutException, StaleElementReferenceException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.desktop.XLUtils import setup_logger

# Get absolute path to credentials.json (assuming it's in the same folder as this file)
credentials_path = os.path.join(os.path.dirname(__file__), "credentials.json")

# Load credentials once when the file is imported
with open(credentials_path, "r") as file:
    credentials = json.load(file)
logger = setup_logger()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, "emailOrPhoneNum")
        self.nextbutton_locator = (By.XPATH, '//button[@data-testid="sign-in-verify"]')
        self.password_locator = (By.XPATH, '//input[@id="password"]')
        self.login_button_locator = (By.XPATH, '//button[normalize-space(text())="Sign In"]')

    def enter_username(self):
        logger.info("Trying to enter username...")
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            username_input = wait.until(EC.presence_of_element_located(self.username_locator))
            username_input.send_keys(credentials[0]["username"])
            logger.info("Username entered successfully.")
            # logger.debug(f"Entered username: dineshkumar.pentakota@gmail.com")
            allure.attach(self.driver.get_screenshot_as_png(), name="EnterUserName",
                          attachment_type=allure.attachment_type.PNG)
        except TimeoutException as e:
            logger.error(f"Failed to enter username: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.critical(f"Unexpected error in enter_username: {e}", exc_info=True)
            raise

    def click_NextButton(self):
        logger.info("Trying to click Next button...")
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            next_button = wait.until(EC.element_to_be_clickable(self.nextbutton_locator))
            self.driver.execute_script("arguments[0].click();", next_button)
            logger.info("Next button clicked successfully.")
            allure.attach(self.driver.get_screenshot_as_png(), name="ClickNextButton",
                          attachment_type=allure.attachment_type.PNG)
        except TimeoutException as e:
            logger.error(f"\033[31mFailed to click Next button: {e}\033[0m", exc_info=True)
            raise
        except Exception as e:
            logger.critical(f"Unexpected error in click_NextButton: {e}", exc_info=True)
            raise

    def enter_password(self):
        logger.info("Trying to enter password...")
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException,
                                                     TimeoutException])
            password_input = wait.until(EC.presence_of_element_located(self.password_locator))
            password_input.send_keys(credentials[1]["passwordanother"])
            logger.info("Password entered successfully.")
            logger.debug("Entered password: [HIDDEN]")  # Don't log actual password!
            allure.attach(self.driver.get_screenshot_as_png(), name="EnterPassword",
                          attachment_type=allure.attachment_type.PNG)
        except TimeoutException as e:
            logger.error(f"Failed to enter password: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.critical(f"Unexpected error in enter_password: {e}", exc_info=True)
            raise

    def click_login_button(self):
        logger.info("Trying to click Login button...")
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            login_button = wait.until(EC.element_to_be_clickable(self.login_button_locator))
            self.driver.execute_script("arguments[0].click();", login_button)
            logger.info("Login button clicked successfully.")
            allure.attach(self.driver.get_screenshot_as_png(), name="ClickLoginButton",
                          attachment_type=allure.attachment_type.PNG)
            print("Dinesh.......success")
        except TimeoutException as e:
            logger.error(f"Failed to click Login button: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.critical(f"Unexpected error in click_login_button: {e}", exc_info=True)
            raise
