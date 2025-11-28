import openpyxl
import time

import pyautogui
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException
import allure
from pages.desktop import XLUtils

path = "C:\\Users\\Dinesh\\Documents\\datadriventestinglogin.xlsx"
rows = XLUtils.getRowCount(path, 'payment')


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, "emailOrPhoneNum")
        self.nextbutton_locator = (By.XPATH, '//button[@data-testid="sign-in-verify"]')
        self.password_locator = (By.XPATH, '//input[@id="password"]')
        self.login_button_locator = (By.XPATH, '//button[normalize-space(text())="Sign In"]')
        self.kittab_image = (
            By.XPATH,
            '//*[@class="c-sidebar-brand-full mobile-logo-width img-fluid inside-logo-full normal-theme-logo"]')
        self.avatar_image = (By.XPATH, '//*[@class="avatar-rounded-img"]')
        self.logout_button = (By.XPATH, '//*[@class="btn btn-link text-danger"]')
        self.click_on_sign_up_page = (By.XPATH, '//span[@class="text-primary"]')
        self.click_on_sign_in_page = (By.XPATH, '//span[@class="text-primary"]')

    def login(self):
        global username, password, r
        for r in range(2, rows + 1):
            username = XLUtils.readData(path, 'sheet1', r, 1)
            password = XLUtils.readData(path, 'sheet1', r, 2)
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                enter_username = wait.until(
                    EC.presence_of_element_located(self.username_locator))
                enter_username.send_keys(username)

                # wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                # Click_next_button = wait.until(
                #     EC.element_to_be_clickable(self.nextbutton_locator))
                # Click_next_button.click()

                enter_password = wait.until(
                    EC.presence_of_element_located(self.password_locator))
                enter_password.send_keys(password)
                try:
                    Click_login_button = wait.until(
                        EC.element_to_be_clickable(self.login_button_locator))
                    self.driver.execute_script("arguments[0].click();", Click_login_button)
                except (AttributeError, TimeoutException):
                    pass
                kittab_image = wait.until(
                    EC.presence_of_element_located(self.kittab_image))
                if kittab_image.is_displayed():
                    print("test is passed")
                    XLUtils.writeData(path, 'sheet1', r, 3, 'test passed')
                else:
                    print("test is failed")
                    XLUtils.writeData(path, 'sheet1', r, 3, 'test failed')
                    time.sleep(4)
                    # # sign up
                    # click_on_sign_up_page_locator = wait.until(
                    #     EC.element_to_be_clickable(self.click_on_sign_up_page))
                    # actions = ActionChains(self.driver)
                    # actions.move_to_element(click_on_sign_up_page_locator).click().perform()
                    # time.sleep(2)
                    # click_on_sign_in_page_locator = wait.until(
                    #     EC.element_to_be_clickable(self.click_on_sign_in_page))
                    # actions = ActionChains(self.driver)
                    # actions.move_to_element(click_on_sign_in_page_locator).click().perform()
                    # time.sleep(2)
            except TimeoutException:
                print("test is failed - kittab_image not found within the timeout period.")
                XLUtils.writeData(path, 'sheet1', r, 3, 'test failed - timeout')
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                avatar_image_locator = wait.until(
                    EC.element_to_be_clickable(self.avatar_image))
                actions = ActionChains(self.driver)
                actions.move_to_element(avatar_image_locator).click().perform()

                logout_button_locator = wait.until(
                    EC.element_to_be_clickable(self.logout_button))
                actions = ActionChains(self.driver)
                actions.move_to_element(logout_button_locator).click().perform()
            except (TimeoutException, AttributeError):
                print("Logout elements not found. Manual intervention may be required.")


rows_ledger = XLUtils.getRowCount(path, 'payment')


class Ledger:
    def __init__(self, driver):
        self.driver = driver
        self.ledger_name_feild = (By.XPATH, '//input[@name="name"]')
        self.click_on_create_button = (By.XPATH, '//*[@class="fi fi-br-plus l-h-1 v-align-middle font-size-12"]')
        self.click_on_ledgers = (
            By.XPATH, '(//button[@class="btn btn-link btn-sm font-size-14 text-dark text-start text-color-3"])[1]')
        self.validation_error = (By.XPATH, '//i[@class="fi fi-br-info font-size-14"]')

    # def ledger_all(self):
    #     # create button
    #     wait = WebDriverWait(self.driver, 50, poll_frequency=3,
    #                          ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
    #     click_on_create_button_locator = wait.until(
    #         EC.element_to_be_clickable(self.click_on_create_button))
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(click_on_create_button_locator).click().perform()
    #     time.sleep(2)
    #     # click on ledger button
    #     wait = WebDriverWait(self.driver, 50, poll_frequency=3,
    #                          ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
    #     click_on_ledgers_locator = wait.until(
    #         EC.element_to_be_clickable(self.click_on_ledgers))
    #     click_on_ledgers_locator.click()
    #
    #     time.sleep(2)
    #     for r in range(2, rows_ledger + 1):
    #         ledgerinput = XLUtils.readData(path, 'dinesh1', r, 1)
    #         # password = XLUtils.readData(path, 'sheet1', r, 2)
    #         try:
    #             wait = WebDriverWait(self.driver, 50, poll_frequency=3,
    #                                  ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
    #             ledger_name_feild_locator = wait.until(
    #                 EC.presence_of_element_located(self.ledger_name_feild))
    #             ledger_name_feild_locator.send_keys(ledgerinput)
    #             attribute_value = ledger_name_feild_locator.get_attribute("value")
    #             for _ in attribute_value:
    #                 ledger_name_feild_locator.send_keys(Keys.BACKSPACE)
    #             time.sleep(3)
    #             print("test is passed")
    #             XLUtils.writeData(path, 'dinesh1', r, 2, 'test passed')
    #             # wait = WebDriverWait(self.driver, 50, poll_frequency=3,
    #             #                      ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
    #             # validation_error_locator = wait.until(
    #             #     EC.presence_of_element_located(self.validation_error))
    #             # if validation_error_locator.is_displayed():
    #             #     actions.move_to_element(validation_error_locator).perform()
    #             #     text = validation_error_locator.text
    #             #     print(text)
    #             #     print("validation error displayed")
    #         except (StaleElementReferenceException,TypeError):
    #             pass

    

