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
            print("Dinesh..success")
        # -----------------------------------------------
        # with allure.step("Click on Login Button"):
        #     login_button = wait.until(EC.element_to_be_clickable(self.login_button_locator))
        #     # Using JS click to avoid stale or overlay issues
        #     self.driver.execute_script("arguments[0].click();", login_button)
        #
        #     # Attach screenshot to Allure report
        #     allure.attach(
        #         self.driver.get_screenshot_as_png(),
        #         name="LoginButton_Clicked",
        #         attachment_type=allure.attachment_type.PNG
        #     )
        #     print("Dinesh..success")


class enter_organisation_check_e_way_bill:
    def __init__(self, driver):
        self.driver = driver
        self.create_organisation_dropdown = (
            By.XPATH, '//*[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"]')
        self.search_box = By.XPATH, '//*[@placeholder="Search"]'
        self.click_gst_module = (By.XPATH,
                                 '(//*[@class="btn btn-link text-color-2 text-start l-h-15 p-20-total  "])[5]')
        self.click_on_e_way_bill = (By.XPATH, '//div[normalize-space(text())="E-Way Bill"]')
        self.from_date_feild = (By.XPATH, '//*[@placeholder="From Date"]')
        self.to_date_feild = (By.XPATH, '//*[@placeholder="To Date"]')
        self.click_fetch_button = (By.XPATH, '//*[@id="d3"]')
        self.add_api_credentials = (By.XPATH, '//*[normalize-space(text())="Add API Credentials"]')
        self.click_on_login_credentials = (By.XPATH,
                                           '//*[@class="btn btn-link btn-sm text-primary active ps-0 pe-0 me-24"]')
        self.add_api_credentials_button = (By.XPATH, '//* [normalize-space(text())="Add API Credentials"]')
        self.click_all_check_boxes_locator = (By.XPATH, '//tbody//tr//td[1]//div[@class="p-checkbox p-component"]')
        self.click_on_paginator = (By.XPATH, '//*[@class="p-paginator-pages"]//button')
        self.click_on_filters = (By.XPATH, '//*[@class="p-column-filter-menu-button p-link"]')
        self.click_all_vouchers = (By.XPATH, '//tbody//tr//td[4]//div')
        self.supply_type = (By.XPATH, '//*[normalize-space(text())="Supply Type"]')
        self.click_on_edit = (By.XPATH, '//*[@class="btn btn-outline-primary btn-sm me-2"]')
        self.click_on_update = (By.XPATH, '//*[@id="mainSave"]')
        self.e_way_bill_histories_in_voucher = (By.XPATH, '//*[@id="tab_4"]')
        self.click_on_elipses = (By.XPATH, '//*[@class="fi fi-br-menu-dots v-middle l-h-0"]')
        self.click_on_preview = (By.XPATH, '//*[normalize-space(text())="Preview"]')
        self.come_back_from_preview_page = (By.XPATH, '(//*[@class="btn btn-link text-color-1 btn-sm"])[1]')
        self.click_on_insights = (By.XPATH,
                                  '//*[@class="btn btn-outline-light figma-bg text-color-1 table-vch-card p-l-r-20 me-2 font-size-14"]')
        self.taxable_value_in_voucher = (By.XPATH,'(//*[@class="table igst-table items-new-table mb-0"]//tbody)[1]//td[6]')

    def click_create_organisation_button_after_login(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        create_organisation_dropdown_locator = wait.until(
            EC.element_to_be_clickable(self.create_organisation_dropdown))
        actions = ActionChains(self.driver)
        actions.move_to_element(create_organisation_dropdown_locator).click().perform()
        time.sleep(3)

    def e_way_bill_testing_organisation(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        search_box_feild = wait.until(
            EC.presence_of_element_located(self.search_box))
        search_box_feild.send_keys("Eway Bill Testing")
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(5)

    def enter_into_gst_module_and_click_e_way_bill(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException,
                                                 ElementClickInterceptedException])
        click_gst_module_locator = wait.until(
            EC.element_to_be_clickable(self.click_gst_module))
        # click_gst_module_locator.click()
        actions = ActionChains(self.driver)
        actions.move_to_element(click_gst_module_locator).click().perform()
        time.sleep(5)
        # click e-way bill module
        # check shortcut
        pyautogui.press('w')
        time.sleep(0.3)
        pyautogui.press('esc')
        # again click on e-way bill
        click_on_e_way_bill_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_e_way_bill))
        # click_gst_module_locator.click()
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_e_way_bill_locator).click().perform()

    def from_date_and_to_date(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException,
                                                 ElementClickInterceptedException])
        click_gst_module_locator = wait.until(
            EC.visibility_of_element_located(self.from_date_feild))
        click_gst_module_locator.send_keys("01/04/2025")
        time.sleep(3)
        # to-date feild
        To_date_feild_locator = wait.until(
            EC.visibility_of_element_located(self.to_date_feild))
        To_date_feild_locator.send_keys("04/11/2025")

        # click fetch button
        click_fetch_button_locator = wait.until(
            EC.element_to_be_clickable(self.click_fetch_button))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_fetch_button_locator).click().perform()
        time.sleep(0.3)

    def click_on_add_credentials(self):
        # click on login credentials
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException,
                                                 ElementClickInterceptedException])
        click_on_login_credentials_locator = wait.until(
            EC.visibility_of_element_located(self.click_on_login_credentials))
        # click_on_login_credentials_locator.click()
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_login_credentials_locator).click().perform()
        time.sleep(5)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException,
                                                 ElementClickInterceptedException])
        add_api_credentials_button_locator = wait.until(
            EC.element_to_be_clickable(self.add_api_credentials_button))
        actions = ActionChains(self.driver)
        actions.move_to_element(add_api_credentials_button_locator).click().perform()
        time.sleep(5)

    def click_all_check_boxes(self):
        # click on paginator
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_paginator_locator = wait.until(
            EC.presence_of_all_elements_located(self.click_on_paginator))
        for j in click_on_paginator_locator:
            click_on_paginator_locator = wait.until(
                EC.presence_of_all_elements_located(self.click_on_paginator))
            actions = ActionChains(self.driver)
            actions.move_to_element(j).click().perform()
            time.sleep(0.1)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_all_check_boxes_locators = wait.until(
                EC.presence_of_all_elements_located(self.click_all_check_boxes_locator))
            for i in click_all_check_boxes_locators:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_all_check_boxes_locators = wait.until(
                    EC.presence_of_all_elements_located(self.click_all_check_boxes_locator))
                actions = ActionChains(self.driver)
                actions.move_to_element(i).click().perform()
                time.sleep(0.1)
                actions.move_to_element(i).click().perform()
                time.sleep(0.1)

    def check_filters(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_filters_locators = wait.until(
            EC.presence_of_all_elements_located(self.click_on_filters))
        for i in click_on_filters_locators:
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_filters_locators = wait.until(
                    EC.presence_of_all_elements_located(self.click_on_filters))
                actions = ActionChains(self.driver)
                actions.move_to_element(i).click().perform()
                time.sleep(0.5)
            except StaleElementReferenceException:
                pass
        time.sleep(4)

    # check vouchers are opening or not
    def vouchers_opening_or_not(self):
        # scroll left side
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        document_no_locator = wait.until(
            EC.visibility_of_element_located(self.supply_type))
        self.driver.execute_script("arguments[0].scrollIntoView();", document_no_locator)

        time.sleep(2)
        try:
            click_on_paginator_locator = wait.until(
                EC.presence_of_all_elements_located(self.click_on_paginator))
            for j in click_on_paginator_locator:
                click_on_paginator_locator = wait.until(
                    EC.presence_of_all_elements_located(self.click_on_paginator))
                actions = ActionChains(self.driver)
                actions.move_to_element(j).click().perform()
                time.sleep(0.1)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_all_vouchers_locators = wait.until(
                    EC.presence_of_all_elements_located(self.click_all_vouchers))
                for i in range(len(click_all_vouchers_locators)):
                    click_all_vouchers_locators = wait.until(
                        EC.presence_of_all_elements_located(self.click_all_vouchers))
                    element = click_all_vouchers_locators[i]
                    actions = ActionChains(self.driver)
                    actions.move_to_element(element).click().perform()
                    time.sleep(1)
                    # click ALT+Enter
                    pyautogui.hotkey('alt', 'enter')
                    # click on preview
                    click_on_elipses_locator = wait.until(
                        EC.presence_of_element_located(self.click_on_elipses))
                    actions = ActionChains(self.driver)
                    actions.move_to_element(click_on_elipses_locator).click().perform()
                    # click on actual preview
                    click_on_preview_locator = wait.until(
                        EC.presence_of_element_located(self.click_on_preview))
                    actions = ActionChains(self.driver)
                    actions.move_to_element(click_on_preview_locator).click().perform()
                    time.sleep(2)
                    come_back_from_preview_page_locator = wait.until(
                        EC.presence_of_element_located(self.come_back_from_preview_page))
                    actions = ActionChains(self.driver)
                    actions.move_to_element(come_back_from_preview_page_locator).click().perform()
                    time.sleep(2)
                    # click on edit
                    click_on_edit_locator = wait.until(
                        EC.presence_of_element_located(self.click_on_edit))
                    actions = ActionChains(self.driver)
                    actions.move_to_element(click_on_edit_locator).click().perform()
                    time.sleep(3)
                    # click on e-way bill histories
                    pyautogui.hotkey('alt', 'w')
                    time.sleep(2)
                    # click on e-way bill histories
                    e_way_bill_histories_in_voucher_locator = wait.until(
                        EC.presence_of_element_located(self.e_way_bill_histories_in_voucher))
                    actions = ActionChains(self.driver)
                    actions.move_to_element(e_way_bill_histories_in_voucher_locator).click().perform()
                    time.sleep(2)
                    pyautogui.press('esc')
                    click_on_update_locator = wait.until(
                        EC.presence_of_element_located(self.click_on_update))
                    actions = ActionChains(self.driver)
                    actions.move_to_element(click_on_update_locator).click().perform()
                    time.sleep(1)
                    pyautogui.press('esc')
                    time.sleep(0.3)
        except (StaleElementReferenceException, TimeoutException):
            pass

    def taxable_value_calculation(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_paginator_locator = wait.until(
            EC.presence_of_all_elements_located(self.click_on_paginator))
        for j in click_on_paginator_locator:
            click_on_paginator_locator = wait.until(
                EC.presence_of_all_elements_located(self.click_on_paginator))
            actions = ActionChains(self.driver)
            actions.move_to_element(j).click().perform()
            time.sleep(0.1)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_all_vouchers_locators = wait.until(
                EC.presence_of_all_elements_located(self.click_all_vouchers))
            for i in range(len(click_all_vouchers_locators)):
                click_all_vouchers_locators = wait.until(
                    EC.presence_of_all_elements_located(self.click_all_vouchers))
                element = click_all_vouchers_locators[i]
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                time.sleep(1)
                taxable_value_in_voucher_locator = wait.until(
                    EC.presence_of_element_located(self.taxable_value_in_voucher))
                text = taxable_value_in_voucher_locator.text
                print(text)




    def insights(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_insights_locator = wait.until(
            EC.presence_of_element_located(self.click_on_insights))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_insights_locator).click().perform()
        time.sleep(5)
