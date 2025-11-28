import allure
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import time
from pages.desktop import XLUtils  # Importing the Excel utility file
from selenium.webdriver import ActionChains, Keys
from datetime import datetime

path = "C:\\Users\\Dinesh\\Documents\\datadriventestinglogin.xlsx"


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, "emailOrPhoneNum")
        self.nextbutton_locator = (By.XPATH, '//button[@data-testid="sign-in-verify"]')
        self.password_locator = (By.XPATH, '//input[@id="password"]')
        self.login_button_locator = (By.XPATH, '//button[normalize-space(text())="Sign In"]')

    def enter_username(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        enter_username = wait.until(
            EC.presence_of_element_located(self.username_locator))
        enter_username.send_keys("venu.k@kitaab.biz")

    def enter_password(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException,
                                                 TimeoutException])
        enter_password = wait.until(
            EC.presence_of_element_located(self.password_locator))
        enter_password.send_keys("Venu@123")

    def click_login_button(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        Click_login_button = wait.until(
            EC.element_to_be_clickable(self.login_button_locator))
        self.driver.execute_script("arguments[0].click();", Click_login_button)
        print("Dinesh..success")


class Payment:
    def __init__(self, driver):
        self.driver = driver
        self.search_button = (
            By.XPATH, '//*[@class="p-inputtext p-component form-control h-40px shadow-none select-filter-input"]')
        self.click_on_payment_drop_down = (
            By.XPATH, '(//*[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"])[2]')
        self.click_on_create_new_button = (By.XPATH, '//*[@class="fi fi-br-plus me-1 font-size-10"]')
        self.click_new_transcation_type_page = (By.XPATH, '//*[@class="font-size-18 f-600 mb-0"]')
        self.click_on_cancel_button = (By.XPATH, '//*[@id="voucherType_mainCancel"]')
        self.click_on_yes = (By.XPATH, '(//button[@class="btn btn-primary p-l-r-20 me-2"])[2]')
        self.click_on_us_dollar_locator = (By.XPATH, '//button[@id="EXCHANGEBTN"]')
        self.exchange_rate_text = (By.XPATH, '//div[@class="p-dialog-title"]')
        self.click_on_switch_transcation_type = (
            By.XPATH, '//*[normalize-space(text())="Switch Transaction Type"]')
        self.transcation_text_after_transcation_type = (By.XPATH, '(//p[@class="mb-0 pl-10-left"])[1]')
        self.click_on_cancel_button_in_transcations_page = (
            By.XPATH, '//*[@class="p-dialog-header-close-icon pi pi-times"]')
        self.saving_in_regular_default_value = (By.XPATH, '//*[@class="font-size-14 text-primary"]')
        self.saving_regular_drop_down_click = (
            By.XPATH, '(//*[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-primary"])[1]')
        self.draft_text = (By.XPATH, '(//div[@class="option-name overflow-elipsis"])[2]')
        self.click_on_draft = (By.XPATH, '(//div[@class="option-name overflow-elipsis"])[2]')
        self.saving_in_draft_text = (By.XPATH, '//*[@class="font-size-14 text-primary"]')
        self.click_on_regular = (By.XPATH, '(//div[@class="option-name overflow-elipsis"])[1]')
        self.gst_in_dropdown = (
            By.XPATH, '(//*[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-primary"])[2]')
        self.gst_block_first_element_text = (By.XPATH, '(//div[@class="option-name overflow-elipsis"])[1]')
        self.click_on_no_label_in_gst_in = (By.XPATH, '(//*[@class="option-name overflow-elipsis"])[1]')
        self.gst_in_default_value_after_click = (By.XPATH, '//span[@class="font-size-16 text-primary"]')
        self.single_in_slider = (
            By.XPATH,
            '//*[@id="VCHCSINGLE"]')
        self.double = (
            By.XPATH, '//*[@id="VCHCDOUBLE"]')
        self.date_feild_locators = (By.XPATH, '//input[@name="entryDate"]')
        self.empty_date_validation_error = (
            By.XPATH, '//div[@class="error-div-parent"]//i[@aria-label="Voucher date is required"]')
        self.validation_error_for_wrong_date = (By.XPATH, '//*[@aria-label="Please enter valid date"]')
        self.validation_date_to_books_beginning_date = (By.XPATH, '//*[@class="fi fi-br-info font-size-14"]')
        self.empty_validation_error_transcation_no = (By.XPATH, '//*[@aria-label="Transaction No. is required"]')
        self.transcation_no_search_feild = (By.XPATH, '//input[@name="voucherNo"]')
        self.payment_made_from_drop_down_click = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[1]')
        self.cash_text = (By.XPATH, '//*[normalize-space(text())="Cash"]')
        self.list_of_payment_made_from = (
            By.XPATH, '//ul[@class="MuiAutocomplete-listbox autocomplete-listbox css-ue1yok"]//li')
        self.pay_paid_to = (By.XPATH, '(//*[@class="d-flex align-items-center justify-content-between"])[3]')
        self.ledger_name_checking_for_payment_paid_drop_down = (By.XPATH, '//th[normalize-space(text())="Ledger Name"]')
        self.payment_paid_to_ledger_name_input_feild = (By.XPATH, '//*[@name="TopLedgers[0].ledgerId"]')
        self.add_amount_input_feild = (By.XPATH, '//*[@name="TopLedgers[0].amount"]')
        self.add_amount_after_enabling = (By.XPATH, '(//*[@class="btn btn-link text-danger btn-sm"])[1]')
        self.ledger_input_feild_in_payment_paid_to = (By.XPATH, '//*[@name="TopLedgers[0].ledgerId"]')
        self.ledger_details_input_feild = (By.XPATH, '//*[@class="btn btn-link text-primary btn-sm"]')
        self.ledger_details_text = (By.XPATH, '//*[@class="text-primary"]')
        self.add_ledger_feild = (By.XPATH, '(//*[@class="btn btn-link text-primary font-size-14"])[2]')
        self.add_ledger_details_in_after_enabling = (
        By.XPATH, '//button[@class="btn btn-link text-primary font-size-14"]')
        self.payment_paid_to_ledger_list = (
            By.XPATH, '//*[@class="MuiAutocomplete-listbox autocomplete-listbox css-ue1yok"]//li[position()  <=10]')
        # By.XPATH, '//*[@class="MuiAutocomplete-listbox autocomplete-listbox css-ue1yok"]//li')
        self.payment_paid_to_ledger_dropdown_click = (
            By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[2]')
        self.ledger_details_text = (By.XPATH, '//*[@class="font-size-18 f-500 mb-0 overflow-elipsis"]')

    def click_on_create_button_and_click_payment(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.F3).perform()
        time.sleep(1)
        actions.key_down(Keys.ALT).send_keys('T').key_up(Keys.ALT).perform()
        time.sleep(1)
        actions.send_keys(Keys.F6).perform()
        allure.attach(self.driver.get_screenshot_as_png(), name='payment page',
                      attachment_type=allure.attachment_type.PNG)

    def search_feild(self):
        start_row = 2
        end_row = 4
        column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column = XLUtils.column_letter_to_index('B')
        sheet_name = 'payment'
        passed_case = 'Test Passed'
        failed_case = 'Test failed'

        for r in range(start_row, end_row + 1):
            # click on search feild
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            click_on_payment_drop_down_locator = wait.until(
                EC.presence_of_element_located(self.click_on_payment_drop_down))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_payment_drop_down_locator).click().perform()
            allure.attach(self.driver.get_screenshot_as_png(), name='click on payment drop down',
                          attachment_type=allure.attachment_type.PNG)
            search_feild = XLUtils.readData(path, sheet_name, r, column_1)
            time.sleep(2)
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            search_button_locator = wait.until(EC.presence_of_element_located(self.search_button))
            search_button_locator.send_keys(search_feild)
            allure.attach(self.driver.get_screenshot_as_png(), name='multiple data',
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(5)
            actions.move_to_element(click_on_payment_drop_down_locator).click().perform()
            time.sleep(1)
            Attribute_value = search_button_locator.get_attribute("value")
            for _ in Attribute_value:
                search_button_locator.send_keys(Keys.BACKSPACE)
            if Attribute_value:
                XLUtils.writeData(path, sheet_name, r, result_column, passed_case)
            else:
                XLUtils.writeData(path, sheet_name, r, result_column, failed_case)
            time.sleep(4)

    def switch_transcation_type_button_in_search(self):
        start_row = 5
        # end_row = 4
        # column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column = XLUtils.column_letter_to_index('B')
        sheet_name = 'payment'
        passed_case = 'Test Passed'
        failed_case = 'Test failed'

        for r in range(start_row, start_row + 1):
            # click on search feild
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            click_on_switch_transcation_type_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_switch_transcation_type))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_switch_transcation_type_locator).click().perform()
            allure.attach(self.driver.get_screenshot_as_png(), name='click on switch transcation type',
                          attachment_type=allure.attachment_type.PNG)
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            transcation_text_after_transcation_type_locator = wait.until(
                EC.presence_of_element_located(self.transcation_text_after_transcation_type))

            if transcation_text_after_transcation_type_locator.is_displayed():
                XLUtils.writeData(path, sheet_name, r, result_column, passed_case)
            else:
                XLUtils.writeData(path, sheet_name, r, result_column, failed_case)
            # click on cancel button
            click_on_cancel_button_in_transcations_page_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_cancel_button_in_transcations_page))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_cancel_button_in_transcations_page_locator).click().perform()
            time.sleep(4)
            allure.attach(self.driver.get_screenshot_as_png(),
                          name='click on cancel button  after click on switch transcation type',
                          attachment_type=allure.attachment_type.PNG)

    def click_on_new_button(self):
        #  click on create  new button
        start_row = 6
        # end_row = 5
        column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column = XLUtils.column_letter_to_index('B')
        sheet_name = 'payment'
        passed_case = 'Test Passed'
        failed_case = 'Test failed'

        for r in range(start_row, start_row + 1):
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            # click_on_payment_drop_down_locator = wait.until(
            #     EC.presence_of_element_located(self.click_on_payment_drop_down))
            actions = ActionChains(self.driver)
            # actions.move_to_element(click_on_payment_drop_down_locator).click().perform()
            search_feild = XLUtils.readData(path, sheet_name, r, column_1)
            time.sleep(2)
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            search_button_locator = wait.until(EC.presence_of_element_located(self.search_button))
            search_button_locator.send_keys(search_feild)

            click_on_create_new_button_locator = wait.until(
                EC.presence_of_element_located(self.click_on_create_new_button))
            actions.move_to_element(click_on_create_new_button_locator).click().perform()
            allure.attach(self.driver.get_screenshot_as_png(),
                          name='click on create new button',
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(3)
            # create transcation type
            click_new_transcation_type_page_locator = wait.until(
                EC.presence_of_element_located(self.click_new_transcation_type_page))
            Text = click_new_transcation_type_page_locator.text
            print(Text)
            if click_new_transcation_type_page_locator.is_displayed():
                XLUtils.writeData(path, sheet_name, r, result_column, passed_case)
            else:
                XLUtils.writeData(path, sheet_name, r, result_column, failed_case)

        # click on cancel
        wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_cancel_button_locator = wait.until(
            EC.presence_of_element_located(self.click_on_cancel_button))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_cancel_button_locator).click().perform()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='click on cancel button  after redirected to create new page',
                      attachment_type=allure.attachment_type.PNG)

        wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_yes_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_yes))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_yes_locator).click().perform()
        time.sleep(2)

    def create_new_alt_c(self):
        # ALT + C
        global k
        start_row_alt_c = 7
        column_1_alt_c = XLUtils.column_letter_to_index('A')
        result_column_alt_c = XLUtils.column_letter_to_index('B')
        sheet_name_alt_c = 'payment'
        passed_case_alt_c = 'Test Passed'
        failed_case_alt_c = 'Test failed'
        try:
            for k in range(start_row_alt_c, start_row_alt_c + 1):
                wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                click_on_payment_drop_down_locator = wait.until(
                    EC.presence_of_element_located(self.click_on_payment_drop_down))
                actions = ActionChains(self.driver)
                actions.move_to_element(click_on_payment_drop_down_locator).click().perform()
                # actions.key_down(Keys.ALT).send_keys('c').key_up(Keys.ALT).perform()
                search_feild = XLUtils.readData(path, sheet_name_alt_c, k, column_1_alt_c)
                time.sleep(2)
                wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                search_button_locator = wait.until(EC.presence_of_element_located(self.search_button))
                search_button_locator.send_keys(search_feild)
                pyautogui.hotkey('alt', 'c')
                time.sleep(5)
                wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                click_new_transcation_type_page_locator = wait.until(
                    EC.presence_of_element_located(self.click_new_transcation_type_page))
                if click_new_transcation_type_page_locator.is_displayed():
                    XLUtils.writeData(path, sheet_name_alt_c, k, result_column_alt_c, passed_case_alt_c)
                else:
                    XLUtils.writeData(path, sheet_name_alt_c, k, result_column_alt_c, failed_case_alt_c)
                time.sleep(3)
                # click on cancel
                wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                click_on_cancel_button_locator = wait.until(
                    EC.presence_of_element_located(self.click_on_cancel_button))
                actions = ActionChains(self.driver)
                actions.move_to_element(click_on_cancel_button_locator).click().perform()

                # wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                #                      ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                # click_on_yes_locator = wait.until(
                #     EC.element_to_be_clickable(self.click_on_yes))
                # actions = ActionChains(self.driver)
                # actions.move_to_element(click_on_yes_locator).click().perform()
        except TimeoutException:
            XLUtils.writeData(path, sheet_name_alt_c, k, result_column_alt_c, failed_case_alt_c)
            pass

    def regular_draft(self):
        # saving in regular default value
        global k, s
        start_row = 8
        # end_row = 5
        # column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column = XLUtils.column_letter_to_index('B')
        sheet_name = 'payment'
        passed_case = 'Test Passed'
        failed_case = 'Test failed'
        for r in range(start_row, start_row + 1):
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            saving_in_regular_default_value_locator = wait.until(
                EC.presence_of_element_located(self.saving_in_regular_default_value))
            Text_saving_default_value = saving_in_regular_default_value_locator.text
            print(Text_saving_default_value)
            Expected_text = "Saving in Regular"
            if Text_saving_default_value == Expected_text:
                XLUtils.writeData(path, sheet_name, r, result_column, passed_case)
            else:
                XLUtils.writeData(path, sheet_name, r, result_column, failed_case)
        time.sleep(2)
        start_row_drop_down_click = 9
        # end_row = 5
        # column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_drop_down = XLUtils.column_letter_to_index('B')
        sheet_name_regular_drop_down = 'payment'
        passed_case_dropdown = 'Test Passed'
        failed_case_drop_down = 'Test failed'
        for k in range(start_row_drop_down_click, start_row_drop_down_click + 1):
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            saving_regular_drop_down_click_locator = wait.until(
                EC.element_to_be_clickable(self.saving_regular_drop_down_click))
            actions = ActionChains(self.driver)
            actions.move_to_element(saving_regular_drop_down_click_locator).click().perform()

        wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        draft_text_locator = wait.until(
            EC.visibility_of_element_located(self.draft_text))
        text = draft_text_locator.text
        print(text)
        if draft_text_locator.is_displayed():
            XLUtils.writeData(path, sheet_name_regular_drop_down, k, result_column_drop_down, passed_case_dropdown)
        else:
            XLUtils.writeData(path, sheet_name_regular_drop_down, k, result_column_drop_down, failed_case_drop_down)
        time.sleep(2)
        # click on draft
        start_row_drop_down_click_draft = 10
        # end_row = 5
        # column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_drop_down_draft = XLUtils.column_letter_to_index('B')
        sheet_name_regular_drop_down_draft = 'payment'
        passed_case_dropdown_draft = 'Test Passed'
        failed_case_drop_down_draft = 'Test failed'
        for s in range(start_row_drop_down_click_draft, start_row_drop_down_click_draft + 1):
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            click_on_draft_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_draft))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_draft_locator).click().perform()
            allure.attach(self.driver.get_screenshot_as_png(), name='click on draft',
                          attachment_type=allure.attachment_type.PNG)
        wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        saving_in_draft_text_locator = wait.until(
            EC.presence_of_element_located(self.saving_in_draft_text))
        text_saving_in_draft = saving_in_draft_text_locator.text
        print(text_saving_in_draft)
        Expected_text = "Saving in Draft"
        if text_saving_in_draft == Expected_text:
            XLUtils.writeData(path, sheet_name_regular_drop_down_draft, s, result_column_drop_down_draft,
                              passed_case_dropdown_draft)
        else:
            XLUtils.writeData(path, sheet_name_regular_drop_down_draft, s, result_column_drop_down_draft,
                              failed_case_drop_down_draft)
        time.sleep(3)
        # again click on regular
        wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        saving_regular_drop_down_click_locator = wait.until(
            EC.element_to_be_clickable(self.saving_regular_drop_down_click))
        actions = ActionChains(self.driver)
        actions.move_to_element(saving_regular_drop_down_click_locator).click().perform()
        # click on regular
        click_on_regular_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_regular))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_regular_locator).click().perform()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='click on regular',
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(2)

    def gst_in_values(self):
        start_row_gst_drop_down = 11
        # end_row = 5
        # column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_gst_drop_down_gst_drop_down = XLUtils.column_letter_to_index('B')
        sheet_name_gst_drop_down = 'payment'
        passed_case_gst_drop_down = 'Test Passed'
        failed_case_gst_drop_down = 'Test failed'
        for r in range(start_row_gst_drop_down, start_row_gst_drop_down + 1):
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            gst_in_dropdown_locator = wait.until(
                EC.presence_of_element_located(self.gst_in_dropdown))
            actions = ActionChains(self.driver)
            actions.move_to_element(gst_in_dropdown_locator).click().perform()

            gst_block_first_element_text_locator = wait.until(
                EC.presence_of_element_located(self.gst_block_first_element_text))

            gst_block_first_element_text_locator_text = gst_block_first_element_text_locator.text
            print(gst_block_first_element_text_locator_text)
            if gst_block_first_element_text_locator.is_displayed():
                XLUtils.writeData(path, sheet_name_gst_drop_down, r, result_column_gst_drop_down_gst_drop_down,
                                  passed_case_gst_drop_down)
            else:
                XLUtils.writeData(path, sheet_name_gst_drop_down, r, result_column_gst_drop_down_gst_drop_down,
                                  failed_case_gst_drop_down)
        # click on first element in gst-in
        start_row_gst_first_element_click = 12
        # end_row = 5
        # column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_gst_in_first_element = XLUtils.column_letter_to_index('B')
        sheet_name_gst_first_element = 'payment'
        passed_case_gst_first_element = 'Test Passed'
        failed_case_gst_first_element = 'Test failed'
        for p in range(start_row_gst_first_element_click, start_row_gst_first_element_click + 1):
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            click_on_no_label_in_gst_in_locator = wait.until(
                EC.presence_of_element_located(self.click_on_no_label_in_gst_in))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_no_label_in_gst_in_locator).click().perform()
            allure.attach(self.driver.get_screenshot_as_png(), name='click on gst element',
                          attachment_type=allure.attachment_type.PNG)

            gst_in_default_value_after_click_locator = wait.until(
                EC.presence_of_element_located(self.gst_in_default_value_after_click))
            gst_in_default_value_after_click_locator_text = gst_in_default_value_after_click_locator.text
            print(gst_in_default_value_after_click_locator_text)
            Expected_text = "No Label"
            if gst_in_default_value_after_click_locator_text == Expected_text:
                XLUtils.writeData(path, sheet_name_gst_first_element, p, result_column_gst_in_first_element,
                                  passed_case_gst_first_element)
            else:
                XLUtils.writeData(path, sheet_name_gst_first_element, p, result_column_gst_in_first_element,
                                  failed_case_gst_first_element)

            # mouse hover to check gst-in no.
            actions.move_to_element(gst_in_default_value_after_click_locator).perform()
            time.sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), name='mouse hover on gst element',
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(2)

    def single_double_slider(self):
        start_row_single_background_color = 13
        # end_row = 5
        # column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_single_background_color = XLUtils.column_letter_to_index('B')
        sheet_name_single_background_color = 'payment'
        passed_case_single_background_color = 'Test Passed'
        failed_case_single_background_color = 'Test failed'
        for r in range(start_row_single_background_color, start_row_single_background_color + 1):
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            single_in_slider_locator = wait.until(
                EC.presence_of_element_located(self.single_in_slider))
            color = single_in_slider_locator.value_of_css_property("color")
            print(color)
            border_color = single_in_slider_locator.value_of_css_property("border-color")
            print(border_color)
            background_color = single_in_slider_locator.value_of_css_property("background-color")
            print(background_color)
            Expected_color = "rgba(48, 95, 240, 1)"
            Expected_border_color = "rgb(211, 212, 214) rgb(48, 95, 240) rgb(211, 212, 214) rgb(211, 212, 214)"
            if color == Expected_color and border_color == Expected_border_color:
                XLUtils.writeData(path, sheet_name_single_background_color, r, result_column_single_background_color,
                                  passed_case_single_background_color)
            else:
                XLUtils.writeData(path, sheet_name_single_background_color, r, result_column_single_background_color,
                                  failed_case_single_background_color)
        # click on double
        start_row_click_on_double_in_slider = 14
        # end_row = 5
        # column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_click_on_double_in_slider = XLUtils.column_letter_to_index('B')
        sheet_name_click_on_double_in_slider = 'payment'
        passed_case_click_on_double_in_slider = 'Test Passed'
        failed_case_click_on_double_in_slider = 'Test failed'
        for z in range(start_row_click_on_double_in_slider, start_row_click_on_double_in_slider + 1):
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            double_locator = wait.until(
                EC.element_to_be_clickable(self.double))
            colour_previous_to_click = double_locator.value_of_css_property('color')
            actions = ActionChains(self.driver)
            actions.move_to_element(double_locator).click().perform()
            time.sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), name='click on double',
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(2)
            # click on yes
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            click_on_yes_locator_for_double = wait.until(
                EC.element_to_be_clickable(self.click_on_yes))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_yes_locator_for_double).click().perform()
            time.sleep(1)
            colour_after_to_click = double_locator.value_of_css_property('color')
            print(colour_after_to_click)
            if colour_previous_to_click != colour_after_to_click:
                XLUtils.writeData(path, sheet_name_click_on_double_in_slider, z,
                                  result_column_click_on_double_in_slider, passed_case_click_on_double_in_slider)
            else:
                XLUtils.writeData(path, sheet_name_click_on_double_in_slider, z,
                                  result_column_click_on_double_in_slider, failed_case_click_on_double_in_slider)
            time.sleep(3)
        # again switch to single
        wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        single_in_slider_locator = wait.until(
            EC.element_to_be_clickable(self.single_in_slider))
        actions = ActionChains(self.driver)
        actions.move_to_element(single_in_slider_locator).click().perform()
        time.sleep(2)

    def date_feild(self):
        start_row_check_current_date = 15
        # end_row = 5
        # column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_check_current_date = XLUtils.column_letter_to_index('B')
        sheet_name_check_current_date = 'payment'
        passed_case_check_current_date = 'Test Passed'
        failed_case_check_current_date = 'Test failed'

        for z in range(start_row_check_current_date, start_row_check_current_date + 1):
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            date_feild_locator = wait.until(
                EC.presence_of_element_located(self.date_feild_locators))
            actions = ActionChains(self.driver)
            actions.move_to_element(date_feild_locator).perform()
            Attribute_value = date_feild_locator.get_attribute("value")
            current_date = datetime.now().strftime('%d/%m/%Y')
            # Compare the attribute value with the current date
            if Attribute_value == current_date:
                XLUtils.writeData(path, sheet_name_check_current_date, z, result_column_check_current_date,
                                  passed_case_check_current_date)
            else:
                XLUtils.writeData(path, sheet_name_check_current_date, z, result_column_check_current_date,
                                  failed_case_check_current_date)

        wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        date_feild_locator = wait.until(
            EC.presence_of_element_located(self.date_feild_locators))
        Attribute_value = date_feild_locator.get_attribute("value")
        for _ in Attribute_value:
            date_feild_locator.send_keys(Keys.BACKSPACE)
        time.sleep(5)

        # date feild for multiple sets of data
        start_row_date_feild_with_multiple_sets = 16
        end_row = 21
        column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_with_multiple_sets = XLUtils.column_letter_to_index('B')
        sheet_name_with_multiple_sets = 'payment'
        passed_case_with_multiple_sets = 'Test Passed'
        failed_case_with_multiple_sets = 'Test failed'
        for z in range(start_row_date_feild_with_multiple_sets, end_row + 1):
            Date_search_feild = XLUtils.readData(path, sheet_name_with_multiple_sets, z, column_1)
            Date_search_feild = Date_search_feild.strftime('%d/%m/%Y')
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            date_feild_locator = wait.until(
                EC.presence_of_element_located(self.date_feild_locators))
            date_feild_locator.send_keys(Date_search_feild)
            allure.attach(self.driver.get_screenshot_as_png(), name='multiple data for date feilds',
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(1)
            Attribute_value = date_feild_locator.get_attribute("value")
            for _ in Attribute_value:
                date_feild_locator.send_keys(Keys.BACKSPACE)
            time.sleep(1)
            if Attribute_value:
                XLUtils.writeData(path, sheet_name_with_multiple_sets, z, result_column_with_multiple_sets,
                                  passed_case_with_multiple_sets)
            else:
                XLUtils.writeData(path, sheet_name_with_multiple_sets, z, result_column_with_multiple_sets,
                                  failed_case_with_multiple_sets)
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB).perform()
        # empty feild
        start_row_check_empty_feild_error = 22
        # end_row = 5
        # column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_empty_feild_error = XLUtils.column_letter_to_index('B')
        sheet_name_empty_feild_error = 'payment'
        passed_case_empty_feild_error = 'Test Passed'
        failed_case_empty_feild_error = 'Test failed'
        try:
            for g in range(start_row_check_empty_feild_error, start_row_check_empty_feild_error + 1):
                wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                empty_date_validation_error_locator = wait.until(
                    EC.visibility_of_element_located(self.empty_date_validation_error))
                actions = ActionChains(self.driver)
                actions.move_to_element(empty_date_validation_error_locator).perform()
                text = empty_date_validation_error_locator.get_attribute("aria-label")
                Expected_text = "Voucher date is required"
                if text == Expected_text:
                    print(f"both {text} and {Expected_text} are equal")
                else:
                    print(f"both {text} and {Expected_text} are not equal")
                if empty_date_validation_error_locator.is_displayed():
                    XLUtils.writeData(path, sheet_name_empty_feild_error, g, result_column_empty_feild_error,
                                      passed_case_empty_feild_error)
                else:
                    XLUtils.writeData(path, sheet_name_empty_feild_error, g, result_column_empty_feild_error,
                                      failed_case_empty_feild_error)
        except TimeoutException:
            XLUtils.writeData(path, sheet_name_empty_feild_error, g, result_column_empty_feild_error,
                              failed_case_empty_feild_error)
            pass

        # wrong date
        start_row_wrong_date = 23
        # end_row = 5
        column_1_wrong_date = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_wrong_date = XLUtils.column_letter_to_index('B')
        sheet_name_wrong_date = 'payment'
        passed_case_wrong_date = 'Test Passed'
        failed_case_wrong_date = 'Test failed'
        for p in range(start_row_wrong_date, start_row_wrong_date + 1):
            Date_search_feild = XLUtils.readData(path, sheet_name_wrong_date, p, column_1_wrong_date)
            Date_search_feild = datetime.strptime(Date_search_feild, '%d/%m/%Y')
            Date_search_feild = Date_search_feild.strftime('%d/%m/%Y')
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            date_feild_locator = wait.until(
                EC.presence_of_element_located(self.date_feild_locators))
            date_feild_locator.send_keys(Date_search_feild)
            # actions = ActionChains(self.driver)
            # actions.send_keys(Keys.TAB).perform()
            # time.sleep(2)

            # check validation message
            try:
                wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                validation_error_for_wrong_date_locator = wait.until(
                    EC.presence_of_element_located(self.validation_error_for_wrong_date))
                time.sleep(2)
                actions.move_to_element(validation_error_for_wrong_date_locator).perform()
                time.sleep(2)
                text = validation_error_for_wrong_date_locator.get_attribute("aria-label")
                Expected_text = "Please enter valid date"
                if text == Expected_text:
                    print(f"both {text} and {Expected_text} are equal")
                else:
                    print(f"both {text} and {Expected_text} are not equal")

                if validation_error_for_wrong_date_locator.is_displayed():
                    XLUtils.writeData(path, sheet_name_wrong_date, p, result_column_wrong_date,
                                      passed_case_wrong_date)
            except TimeoutException:
                XLUtils.writeData(path, sheet_name_wrong_date, p, result_column_wrong_date,
                                  failed_case_wrong_date)
                pass
        Attribute_value = date_feild_locator.get_attribute("value")
        for _ in Attribute_value:
            date_feild_locator.send_keys(Keys.BACKSPACE)

        # date prior to books beggining from
        start_row_date_prior_to_books_beginning_from = 24
        # end_row = 5
        column_1_date_prior_to_books_beginning_from = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_date_prior_to_books_beginning_from = XLUtils.column_letter_to_index('B')
        sheet_name_date_prior_to_books_beginning_from = 'payment'
        passed_case_date_prior_to_books_beginning_from = 'Test Passed'
        failed_case_date_prior_to_books_beginning_from = 'Test failed'
        try:
            for o in range(start_row_date_prior_to_books_beginning_from,
                           start_row_date_prior_to_books_beginning_from + 1):
                Date_search_feild = XLUtils.readData(path, sheet_name_date_prior_to_books_beginning_from, o,
                                                     column_1_date_prior_to_books_beginning_from)
                # Date_search_feild = datetime.strptime(Date_search_feild, '%d/%m/%Y')
                Date_search_feild = Date_search_feild.strftime('%d/%m/%Y')
                wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                date_feild_locator = wait.until(
                    EC.presence_of_element_located(self.date_feild_locators))
                date_feild_locator.send_keys(Date_search_feild)
                # check validation message
                wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                validation_date_to_books_beginning_date_locator = wait.until(
                    EC.presence_of_element_located(self.validation_date_to_books_beginning_date))
                actions = ActionChains(self.driver)
                actions.move_to_element(validation_date_to_books_beginning_date_locator).perform()
                time.sleep(2)
                text = validation_date_to_books_beginning_date_locator.get_attribute("aria-label")
                Expected_text = "Date should not be prior to books beginning from date 01-04-2022"
                if text == Expected_text:
                    print(f"both {text} and {Expected_text} are equal")
                else:
                    print(f"both {text} and {Expected_text} are not equal")
                if validation_date_to_books_beginning_date_locator.is_displayed():
                    XLUtils.writeData(path, sheet_name_date_prior_to_books_beginning_from, o,
                                      result_column_date_prior_to_books_beginning_from,
                                      passed_case_date_prior_to_books_beginning_from)
                else:
                    XLUtils.writeData(path, sheet_name_date_prior_to_books_beginning_from, o,
                                      result_column_date_prior_to_books_beginning_from,
                                      failed_case_date_prior_to_books_beginning_from)
        except TimeoutException:
            XLUtils.writeData(path, sheet_name_date_prior_to_books_beginning_from, o,
                              result_column_date_prior_to_books_beginning_from,
                              failed_case_date_prior_to_books_beginning_from)
            pass

        Attribute_value1 = date_feild_locator.get_attribute("value")
        for _ in Attribute_value1:
            date_feild_locator.send_keys(Keys.BACKSPACE)
        date_feild_locator.send_keys("10/12/2024")
        # ALT+F2

    def transcation_no(self):
        # empty feild
        start_row_check_empty_feild_error = 25
        # end_row = 5
        # column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_empty_feild_error = XLUtils.column_letter_to_index('B')
        sheet_name_empty_feild_error = 'payment'
        passed_case_empty_feild_error = 'Test Passed'
        failed_case_empty_feild_error = 'Test failed'
        try:
            for g in range(start_row_check_empty_feild_error, start_row_check_empty_feild_error + 1):
                wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                # transcation no.search feild
                transcation_no_search_feild_locator = wait.until(
                    EC.element_to_be_clickable(self.transcation_no_search_feild))
                actions = ActionChains(self.driver)
                time.sleep(1)
                actions.move_to_element(transcation_no_search_feild_locator).perform()
                time.sleep(1)
                actions.move_to_element(transcation_no_search_feild_locator).click().perform()
                actions.send_keys(Keys.TAB).perform()
                empty_validation_error_transcation_no_locator = wait.until(
                    EC.presence_of_element_located(self.empty_validation_error_transcation_no))
                actions = ActionChains(self.driver)
                actions.move_to_element(empty_validation_error_transcation_no_locator).perform()
                allure.attach(self.driver.get_screenshot_as_png(), name='empty transcation error',
                              attachment_type=allure.attachment_type.PNG)
                text = empty_validation_error_transcation_no_locator.get_attribute("aria-label")
                Expected_text = "Transcation No. is required"
                if text == Expected_text:
                    print(f"both {text} and {Expected_text} are equal")
                else:
                    print(f"both {text} and {Expected_text} are not equal")
                if empty_validation_error_transcation_no_locator.is_displayed():
                    XLUtils.writeData(path, sheet_name_empty_feild_error, g, result_column_empty_feild_error,
                                      passed_case_empty_feild_error)
                else:
                    XLUtils.writeData(path, sheet_name_empty_feild_error, g, result_column_empty_feild_error,
                                      failed_case_empty_feild_error)
        except TimeoutException:
            XLUtils.writeData(path, sheet_name_empty_feild_error, g, result_column_empty_feild_error,
                              failed_case_empty_feild_error)
            pass

        # for 25 characters
        start_row_25_char = 26
        # end_row = 5
        column_1_25_char = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_25_char = XLUtils.column_letter_to_index('B')
        sheet_name_25_char = 'payment'
        passed_case_25_char = 'Test Passed'
        failed_case_25_char = 'Test failed'

        for p in range(start_row_25_char, start_row_25_char + 1):
            Transcation_search_feild = XLUtils.readData(path, sheet_name_25_char, p,
                                                        column_1_25_char)
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            transcation_no_search_feild_locator = wait.until(
                EC.presence_of_element_located(self.transcation_no_search_feild))
            transcation_no_search_feild_locator.send_keys(Transcation_search_feild)
            Attribute_value = transcation_no_search_feild_locator.get_attribute("value")
            length = len(Attribute_value)
            print(length)
            if length == 25:
                XLUtils.writeData(path, sheet_name_25_char, p, result_column_25_char, passed_case_25_char)
            elif length > 25:
                XLUtils.writeData(path, sheet_name_25_char, p, result_column_25_char, failed_case_25_char)
            Attribute_value = transcation_no_search_feild_locator.get_attribute("value")
            for _ in Attribute_value:
                transcation_no_search_feild_locator.send_keys(Keys.BACKSPACE)
            transcation_no_search_feild_locator.send_keys('123')
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(1)
        actions.send_keys(Keys.BACKSPACE).perform()
        time.sleep(1)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        actions.send_keys(Keys.ESCAPE).perform()
        time.sleep(1)
        # payment made from drop down click
        start_row_payment_made_from_drop_down_click = 27
        # end_row = 5
        # column_1_25_char = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_payment_made_from_drop_down_click = XLUtils.column_letter_to_index('B')
        sheet_name_payment_made_from_drop_down_click = 'payment'
        passed_case_payment_made_from_drop_down_click = 'Test Passed'
        failed_case_payment_made_from_drop_down_click = 'Test failed'
        for b in range(start_row_payment_made_from_drop_down_click, start_row_payment_made_from_drop_down_click + 1):
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            payment_made_from_drop_down_click_locator = wait.until(
                EC.element_to_be_clickable(self.payment_made_from_drop_down_click))
            actions.move_to_element(payment_made_from_drop_down_click_locator).click().perform()
            allure.attach(self.driver.get_screenshot_as_png(), name='click on payment made from dropdown',
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(1)
            # cash text
            cash_text_locator = wait.until(
                EC.presence_of_element_located(self.cash_text))
            if cash_text_locator.is_displayed():
                XLUtils.writeData(path, sheet_name_payment_made_from_drop_down_click, b,
                                  result_column_payment_made_from_drop_down_click,
                                  passed_case_payment_made_from_drop_down_click)
            else:
                XLUtils.writeData(path, sheet_name_payment_made_from_drop_down_click, b,
                                  result_column_payment_made_from_drop_down_click,
                                  failed_case_payment_made_from_drop_down_click)

        # payment made from list
        wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        payment_made_from_drop_down_click_locator = wait.until(
            EC.element_to_be_clickable(self.payment_made_from_drop_down_click))
        actions.move_to_element(payment_made_from_drop_down_click_locator).click().perform()
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3, ignored_exceptions=[Exception])
            list_of_payment_made_from_locator = wait.until(
                EC.presence_of_all_elements_located(self.list_of_payment_made_from))
            print(len(list_of_payment_made_from_locator))

            Element_list = [element.text for element in list_of_payment_made_from_locator]
            length_of_element_list = len(Element_list)
            print("Element_list:", Element_list)

            for i in range(length_of_element_list):
                # Re-locate all elements in each iteration to avoid stale element reference
                wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                country_list_get_lists = wait.until(
                    EC.presence_of_all_elements_located(self.list_of_payment_made_from))
                element1 = country_list_get_lists[i]
                actions.move_to_element(element1).perform()
                time.sleep(1)
                actions.move_to_element(element1).click().perform()
                payment_made_from_drop_down_click_locator = wait.until(
                    EC.element_to_be_clickable(self.payment_made_from_drop_down_click))
                actions.move_to_element(payment_made_from_drop_down_click_locator).click().perform()
            time.sleep(5)
        except TimeoutException:
            pass

    def payment_paid_to_data_driven_test_drop_down(self):
        start_row_data_driven = 27
        end_row_data_driven = 35
        column_1_data_driven = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_data_driven = XLUtils.column_letter_to_index('B')
        sheet_name_data_driven = 'payment'
        passed_case_data_driven = 'Test Passed'
        failed_case_data_driven = 'Test failed'

        for p in range(start_row_data_driven, end_row_data_driven + 1):
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])

            payment_made_from_drop_down = XLUtils.readData(path, sheet_name_data_driven, p, column_1_data_driven)
            list_of_payment_made_from_locator = wait.until(
                EC.presence_of_all_elements_located(self.list_of_payment_made_from))
            Element_list = [element.text for element in list_of_payment_made_from_locator]

            if payment_made_from_drop_down in Element_list:
                XLUtils.writeData(path, sheet_name_data_driven, p, result_column_data_driven,
                                  passed_case_data_driven)
            else:
                XLUtils.writeData(path, sheet_name_data_driven, p, result_column_data_driven,
                                  failed_case_data_driven)
            time.sleep(0.5)

    def payment_paid_to(self):
        start_row_payment_paid_to = 36
        # end_row = 5
        # column_1_25_char = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_payment_paid_to = XLUtils.column_letter_to_index('B')
        sheet_name_payment_paid_to = 'payment'
        shrinked_payment_paid_to = 'Test Passed'
        failed_case_payment_paid_to = 'Test failed'

        # payment paid to
        for p in range(start_row_payment_paid_to, start_row_payment_paid_to + 1):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3, ignored_exceptions=[Exception])
            pay_paid_to_locator = wait.until(
                EC.element_to_be_clickable(self.pay_paid_to))
            actions = ActionChains(self.driver)
            actions.move_to_element(pay_paid_to_locator).click().perform()
            # ledger name
            try:
                ledger_name_checking_for_payment_paid_drop_down_locator = wait.until(
                    EC.visibility_of_element_located(self.ledger_name_checking_for_payment_paid_drop_down))
                if ledger_name_checking_for_payment_paid_drop_down_locator.is_displayed():
                    XLUtils.writeData(path, sheet_name_payment_paid_to, p, result_column_payment_paid_to,
                                      failed_case_payment_paid_to)
                else:
                    XLUtils.writeData(path, sheet_name_payment_paid_to, p, result_column_payment_paid_to,
                                      shrinked_payment_paid_to)
            except TimeoutException:
                XLUtils.writeData(path, sheet_name_payment_paid_to, p, result_column_payment_paid_to,
                                  shrinked_payment_paid_to)
                pass

        start_row_payment_paid_to_re = 37
        # end_row = 5
        # column_1_25_char = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_payment_paid_to_re = XLUtils.column_letter_to_index('B')
        sheet_name_payment_paid_to_re = 'payment'
        shrinked_payment_paid_to_re = 'Test Passed'
        failed_case_payment_paid_to_re = 'Test failed'
        for s in range(start_row_payment_paid_to_re, start_row_payment_paid_to_re + 1):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3, ignored_exceptions=[Exception])
            pay_paid_to_locator = wait.until(
                EC.element_to_be_clickable(self.pay_paid_to))
            actions = ActionChains(self.driver)
            actions.move_to_element(pay_paid_to_locator).click().perform()
            # ledger name
            ledger_name_checking_for_payment_paid_drop_down_locator = wait.until(
                EC.visibility_of_element_located(self.ledger_name_checking_for_payment_paid_drop_down))
            if ledger_name_checking_for_payment_paid_drop_down_locator.is_displayed():
                XLUtils.writeData(path, sheet_name_payment_paid_to_re, s, result_column_payment_paid_to_re,
                                  shrinked_payment_paid_to_re)
            else:
                XLUtils.writeData(path, sheet_name_payment_paid_to_re, s, result_column_payment_paid_to_re,
                                  failed_case_payment_paid_to_re)
        # check disabled feilds
        start_row_payment_disabled_feilds = 38
        # end_row = 5
        # column_1_25_char = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_disabled_feilds = XLUtils.column_letter_to_index('B')
        sheet_name_disabled_feilds = 'payment'
        passed_disabled_feilds = 'Test Passed'
        failed_case_disabled_feilds = 'Test failed'
        for t in range(start_row_payment_disabled_feilds, start_row_payment_disabled_feilds + 1):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3, ignored_exceptions=[Exception])
            payment_paid_to_ledger_name_input_feild_locator = wait.until(
                EC.presence_of_element_located(self.payment_paid_to_ledger_name_input_feild))
            Attribute_value = payment_paid_to_ledger_name_input_feild_locator.get_attribute("value")
            print(Attribute_value)
            if Attribute_value == '':
                add_amount_input_feild_locator = wait.until(
                    EC.presence_of_element_located(self.add_amount_input_feild))
                ledger_details_input_feild_locator = wait.until(
                    EC.presence_of_element_located(self.ledger_details_input_feild))
                add_ledger_feild_locator = wait.until(
                    EC.presence_of_element_located(self.add_ledger_feild))
                if add_amount_input_feild_locator.is_enabled() and ledger_details_input_feild_locator.is_enabled() and add_ledger_feild_locator.is_enabled():
                    XLUtils.writeData(path, sheet_name_disabled_feilds, t, result_column_disabled_feilds,
                                      failed_case_disabled_feilds)
                else:
                    XLUtils.writeData(path, sheet_name_disabled_feilds, t, result_column_disabled_feilds,
                                      passed_disabled_feilds)
            else:
                print("not empty")
        # click all payment paid to
        wait = WebDriverWait(self.driver, 50, poll_frequency=3, ignored_exceptions=[Exception])
        payment_paid_to_ledger_dropdown_click_locator = wait.until(
            EC.element_to_be_clickable(self.payment_paid_to_ledger_dropdown_click))
        actions = ActionChains(self.driver)
        actions.move_to_element(payment_paid_to_ledger_dropdown_click_locator).click().perform()

        payment_paid_to_ledger_list_locator = wait.until(
            EC.presence_of_all_elements_located(self.payment_paid_to_ledger_list))
        print(len(payment_paid_to_ledger_list_locator))

        Element_list = [element.text for element in payment_paid_to_ledger_list_locator]
        length_of_element_list = len(Element_list)
        print("Element_list:", Element_list)

        for i in range(length_of_element_list):
            # Re-locate all elements in each iteration to avoid stale element reference
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            payment_paid_to_ledger_list_locator = wait.until(
                EC.presence_of_all_elements_located(self.payment_paid_to_ledger_list))
            element1 = payment_paid_to_ledger_list_locator[i]
            actions.move_to_element(element1).perform()
            time.sleep(0.5)
            actions.move_to_element(element1).click().perform()
            try:
                ledger_details_text_locator = wait.until(
                    EC.presence_of_element_located(self.ledger_details_text))
                if ledger_details_text_locator.is_displayed():
                    text = ledger_details_text_locator.text
                    first_part = text.split('-')[0].strip()
                    if "Ledger Details" in first_part:
                        actions = ActionChains(self.driver)
                        actions.send_keys(Keys.ESCAPE).perform()
                    else:
                        continue
            except TimeoutException:
                pass
            time.sleep(0.5)
            payment_paid_to_ledger_dropdown_click_locator = wait.until(
                EC.element_to_be_clickable(self.payment_paid_to_ledger_dropdown_click))
            actions = ActionChains(self.driver)
            actions.move_to_element(payment_paid_to_ledger_dropdown_click_locator).click().perform()
            time.sleep(0.5)
        time.sleep(2)

    def ledger_details_cost_details_cost_details(self):
        # check feilds are enabled
        start_row_payment_disabled_feilds = 39
        # end_row = 5
        # column_1_25_char = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_disabled_feilds = XLUtils.column_letter_to_index('B')
        sheet_name_disabled_feilds = 'payment'
        passed_disabled_feilds = 'Test Passed'
        failed_case_disabled_feilds = 'Test failed'
        for t in range(start_row_payment_disabled_feilds, start_row_payment_disabled_feilds + 1):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3, ignored_exceptions=[Exception])
            payment_paid_to_ledger_name_input_feild_locator = wait.until(
                EC.presence_of_element_located(self.payment_paid_to_ledger_name_input_feild))
            Attribute_value = payment_paid_to_ledger_name_input_feild_locator.get_attribute("value")
            if Attribute_value != '':
                add_amount_after_enabling_locator = wait.until(
                    EC.presence_of_element_located(self.add_amount_after_enabling))
                ledger_details_input_feild_locator = wait.until(
                    EC.presence_of_element_located(self.ledger_details_input_feild))
                add_ledger_feild_locator = wait.until(
                    EC.presence_of_element_located(self.add_ledger_details_in_after_enabling))
                if add_amount_after_enabling_locator.is_enabled() and ledger_details_input_feild_locator.is_enabled() and add_ledger_feild_locator.get_attribute(
                        "disabled") is not None:
                    XLUtils.writeData(path, sheet_name_disabled_feilds, t, result_column_disabled_feilds,
                                      passed_disabled_feilds)
                else:
                    XLUtils.writeData(path, sheet_name_disabled_feilds, t, result_column_disabled_feilds,
                                      failed_case_disabled_feilds)
            else:
                print("not empty")
        wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        payment_paid_to_ledger_dropdown_click_locator = wait.until(
            EC.element_to_be_clickable(self.payment_paid_to_ledger_dropdown_click))
        actions = ActionChains(self.driver)
        actions.move_to_element(payment_paid_to_ledger_dropdown_click_locator).click().perform()
        time.sleep(1)
        # click on suspense
        actions = ActionChains(self.driver)
        for _ in range(5):
            actions.send_keys(Keys.ARROW_UP).perform()
            time.sleep(0.3)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(0.5)
        actions.send_keys(Keys.ESCAPE).perform()
        # input feild of ledger name in payment paid to
        start_row_ledger_name_to_ledger_name_in_side_page = 40
        # end_row = 5
        # column_1_25_char = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column_ledger_name_to_ledger_name_in_side_page = XLUtils.column_letter_to_index('B')
        sheet_name_ledger_name_to_ledger_name_in_side_page = 'payment'
        passed_ledger_name_to_ledger_name_in_side_page = 'Test Passed'
        failed_case_ledger_name_to_ledger_name_in_side_page = 'Test failed'
        for r in range(start_row_ledger_name_to_ledger_name_in_side_page,
                       start_row_ledger_name_to_ledger_name_in_side_page + 1):
            ledger_input_feild_in_payment_paid_to_locator = wait.until(
                EC.presence_of_element_located(self.ledger_input_feild_in_payment_paid_to))
            Attribute_value_of_ledger_name = ledger_input_feild_in_payment_paid_to_locator.get_attribute("value")
            print("Attribute_value_of_ledger_name", Attribute_value_of_ledger_name)
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(1)
            ledger_details_text_locator = wait.until(
                EC.presence_of_element_located(self.ledger_details_text))
            text_after_opening_ledger_details = ledger_details_text_locator.text
            text_after_opening_ledger_details_after_split = text_after_opening_ledger_details.split('-')[1].strip()
            print("text_after_opening_ledger_details:", text_after_opening_ledger_details_after_split)
            if Attribute_value_of_ledger_name == text_after_opening_ledger_details_after_split:
                print("equal")
                XLUtils.writeData(path, sheet_name_ledger_name_to_ledger_name_in_side_page, r,
                                  result_column_ledger_name_to_ledger_name_in_side_page,
                                  passed_ledger_name_to_ledger_name_in_side_page)
            else:
                XLUtils.writeData(path, sheet_name_ledger_name_to_ledger_name_in_side_page, r,
                                  result_column_ledger_name_to_ledger_name_in_side_page,
                                  failed_case_ledger_name_to_ledger_name_in_side_page)
                print("unequal")
        actions.send_keys(Keys.ESCAPE).perform()

    def click_on_us_dollar(self):
        start_row = 41
        # end_row = 5
        # column_1 = XLUtils.column_letter_to_index('A')
        # column_2 = XLUtils.column_letter_to_index('H')
        result_column = XLUtils.column_letter_to_index('B')
        sheet_name = 'payment'
        passed_case = 'Test Passed'
        failed_case = 'Test failed'
        for r in range(start_row, start_row + 1):
            # click on us dollar
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            click_on_us_dollar_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_us_dollar_locator))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_us_dollar_locator).click().perform()

            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            exchange_rate_text = wait.until(
                EC.visibility_of_element_located(self.exchange_rate_text))
            text = exchange_rate_text.text
            time.sleep(5)
            if exchange_rate_text.is_displayed():
                XLUtils.writeData(path, sheet_name, r, result_column, passed_case)
            else:
                XLUtils.writeData(path, sheet_name, r, result_column, failed_case)
