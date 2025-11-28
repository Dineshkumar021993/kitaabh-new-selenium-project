import time

import pyautogui
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException
import allure


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, "emailOrPhoneNum")
        self.nextbutton_locator = (By.XPATH, '//button[@data-testid="sign-in-verify"]')
        self.password_locator = (By.XPATH, '//input[@id="password"]')
        self.login_button_locator = (By.XPATH, '//button[normalize-space(text())="Sign In"]')
        self.change_organisation_drop_down = (By.XPATH,
                                              '(//*[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"])[1]')
        self.select_organisation = (By.XPATH, '(//*[normalize-space(text())="advances testing new"])[1]')

    def enter_username(self):
        with allure.step("Enter username"):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            enter_username = wait.until(
                EC.presence_of_element_located(self.username_locator))
            enter_username.send_keys("venu.k@kitaab.biz")
            allure.attach(self.driver.get_screenshot_as_png(), name="EnterUserName",
                          attachment_type=allure.attachment_type.PNG)

    def click_NextButton(self):
        with allure.step("Click Next Button"):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            Click_next_button = wait.until(
                EC.element_to_be_clickable(self.nextbutton_locator))
            self.driver.execute_script("arguments[0].click();", Click_next_button)
            allure.attach(self.driver.get_screenshot_as_png(), name="ClickNextButton",
                          attachment_type=allure.attachment_type.PNG)

    def enter_password(self):
        with allure.step("Enter password"):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException,
                                                     TimeoutException])
            enter_password = wait.until(
                EC.presence_of_element_located(self.password_locator))
            enter_password.send_keys("Venu@123")
            allure.attach(self.driver.get_screenshot_as_png(), name="EnterPassword",
                          attachment_type=allure.attachment_type.PNG)

    def click_login_button(self):
        with allure.step("Click on Login Button"):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            Click_login_button = wait.until(
                EC.element_to_be_clickable(self.login_button_locator))
            self.driver.execute_script("arguments[0].click();", Click_login_button)
            allure.attach(self.driver.get_screenshot_as_png(), name="ClickLoginButton",
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(1)

        # change organisation
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        change_organisation_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.change_organisation_drop_down))
        actions = ActionChains(self.driver)
        actions.move_to_element(change_organisation_drop_down_locator).click().perform()
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickLoginButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(1)
        # select advances testing new
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        select_organisation_locator = wait.until(
            EC.element_to_be_clickable(self.select_organisation))
        actions = ActionChains(self.driver)
        actions.move_to_element(select_organisation_locator).click().perform()

        self.driver.get("https://d3ldvcrr82x82a.cloudfront.net/#/gst-app/gstr-9-filing")
        time.sleep(1.5)


class gstr:
    def __init__(self, driver):
        self.driver = driver
        self.year_date_toggle_l = (By.XPATH, '//*[@id="year-date-toggle"]')
        self.select_financial_year = (By.XPATH, '(//*[normalize-space(text())="2025-2026"])[1]')
        self.check_due_date = (By.XPATH, '//span[@class="text-color-3"]')
        self.click_gstin_drop_down = (By.XPATH,
                                      '//*[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-primary"]')
        self.check_all_child = (By.XPATH, '//tbody//tr//td[1]')
        self.first_item = (By.XPATH, '//*[normalize-space(text())="(A) Supplies made to un-registered persons (B2C)"]')
        self.child_items_values = (By.XPATH, '//tbody//tr')

    def year_date_toggle(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        year_date_toggle_l = wait.until(
            EC.element_to_be_clickable(self.year_date_toggle_l))
        year_date_toggle_l.click()
        time.sleep(1.5)

        # select financial year
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        select_financial_year_locator = wait.until(
            EC.element_to_be_clickable(self.select_financial_year))
        select_financial_year_locator.click()

        # check due date
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        check_due_date_locator = wait.until(
            EC.presence_of_element_located(self.check_due_date))
        Actual_due_date = check_due_date_locator.text

        Expected_due_date = "31/12/2026"

        if Actual_due_date == Expected_due_date:
            print(f"both {Actual_due_date} and {Expected_due_date} are equal")
        else:
            print(f"both {Actual_due_date} and {Expected_due_date} are not equal")

    def check_gst_in_dropdown(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_gstin_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_gstin_drop_down))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_gstin_drop_down_locator).click().perform()

        for _ in range(2):
            pyautogui.press('down')
            time.sleep(1)
        for _ in range(2):
            pyautogui.press('up')
            time.sleep(1)
        pyautogui.press('enter')

    def check_child_items_displaying(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        check_all_child = wait.until(
            EC.presence_of_all_elements_located(self.check_all_child))

        for i in check_all_child:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            check_all_child = wait.until(
                EC.presence_of_all_elements_located(self.check_all_child))
            actions = ActionChains(self.driver)
            actions.move_to_element(i).click().perform()
            time.sleep(1)

    def first_feild_and_its_items(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        first_item_locator = wait.until(
            EC.presence_of_element_located(self.first_item))
        first_item_text_actual = first_item_locator.text
        first_item_required = "(A) Supplies made to un-registered persons (B2C)"
        if first_item_required == first_item_text_actual:
            print(f"Both {first_item_required} and {first_item_text_actual} are equal")
        else:
            print(f"Both {first_item_required} and {first_item_text_actual} are not equal")

        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        child_items_values_locator = wait.until(
            EC.presence_of_all_elements_located(self.child_items_values))

        for row in child_items_values_locator:
            cols = row.find_elements(By.XPATH, "./td[position() >= 2]")
            data = [c.text for c in cols]
            print(data)



