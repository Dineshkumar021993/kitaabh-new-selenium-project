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
            enter_username.send_keys("dinesh@kitaab.biz")
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
            enter_password.send_keys("Dinesh@4")
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


class CreateOrganisation:
    def __init__(self, driver):
        self.driver = driver
        self.create_organisation_dropdown = (
            By.XPATH, '//*[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"]')
        self.click_on_create_organisation = (By.XPATH, '//button[normalize-space(text())="Create Organisation"]')
        self.legal_name = (By.NAME, 'legalName')
        self.alias_feild = (By.ID, 'o2')
        self.country_drop_down_click = (By.XPATH, '(//i[@class="fi fi-ss-angle-small-down font-size-18"])[1]')
        self.currency_drop_down_click = (By.XPATH, '(//i[@class="fi fi-ss-angle-small-down font-size-18"])[2]')
        self.gst_in = (By.ID, 'o6')
        self.click_on_gst_active = (By.XPATH, '//i[@class="fi fi-br-eye font-size-14 text-success"]')
        self.state = (By.ID, 'o7')
        self.pan_value = (By.ID, 'o8')
        self.save_button = (By.ID, 'o9')
        self.click_on_organisation_settings_after_save = (
            By.XPATH, '//*[@class="btn btn-outline-primary font-size-14 b-r-8 me-2"]')
        self.click_on_view_all = (By.XPATH, '//button[normalize-space(text())="View all"]')
        self.click_on_vertical_dots = (By.XPATH, '(//*[@class="fi fi-br-menu-dots-vertical l-h-1 v-align-middle"])[2]')
        self.click_on_organisation_settings = (By.XPATH, '//*[@class="fi fi-rr-settings"]')
        self.organisation_settings_inside = (By.XPATH, '//button[normalize-space(text())="Organisation Settings"]')
        self.legal_name_in_primary_details = (By.ID, 'pm1')
        self.alias_name_in_primary_details = (By.ID, 'pm2')
        self.country_feild_in_primary_feild = (By.ID, 'pm3')
        self.country_input_feild_in_create_organisation = (By.ID, 'o3')
        self.currency_feild_in_primary_details = (By.ID, 'pm4')
        self.Gst_in_in_primary_details = (By.ID, 'pm6')
        self.click_on_configuration = (By.NAME, 'Configuration')
        self.books_begining_from_input_feild = (By.XPATH, '//input[@name="booksBeginningFrom"]')
        self.click_on_yes_button_for_books_begginning_from_date = (By.XPATH, '//button[@id="ACCEPCONFIRM"]')
        self.accounting_drop_down_click = (By.XPATH, '(//i[@class="fi fi-ss-angle-small-down font-size-18"])[1]')
        self.default_accounting_period_in_configuration = (
            By.XPATH, '//div[normalize-space(text())="Financial Year (Apr - Mar)"]')
        self.click_on_currency_drop_down = (By.XPATH, '(//i[@class="fi fi-ss-angle-small-down font-size-18"])[2]')
        self.click_on_indian_rupee = (By.XPATH, '(//div[@title="Indian Rupee (₹)"])[2]')
        self.ISO_code = (By.XPATH, '//input[@name="currencyISOCode"]')
        self.date_format = (By.XPATH, '//div[@class="p-radiobutton-box p-highlight"]')
        self.click_on_features = (By.XPATH, '//*[normalize-space(text())="Features"]')
        self.edit_log_check_box = (By.XPATH, '//*[normalize-space(text())="Edit Log"]//parent::div//div[2]')
        self.enable_bill_wise_entries_check_box = (
            By.XPATH, '//label[normalize-space(text())="Enable Bill wise Entries"]//parent::div//child::div[2]')
        self.Enable_cost_centers = (
            By.XPATH, '//label[normalize-space(text())="Enable Cost Centers"]//parent::div//child::div[2]')
        self.click_on_inventory = (By.XPATH, '//*[@name="Inventory"]')
        self.maintain_inventory_feild = (By.XPATH, '//*[@class="p-inputswitch-slider"]')
        self.Inventory_check_boxes = (By.XPATH, '//div[@class="p-hidden-accessible"]')
        self.click_on_GST = (By.XPATH, '//button[@name="GST"]')
        self.click_on_GST_slider = (By.XPATH, '//*[@class="p-inputswitch-slider"]')
        self.enter_gst_in_gst_in_configuration = (By.XPATH, '//input[@name="gstin"]')
        self.name_applicable_from_in_inside_confirmation_box = (By.XPATH, '//input[@name="applicableFrom"]')
        self.enter_registration_name_in_gst = (By.XPATH, '//*[@name="registrationName"]')
        self.click_on_cancel_in_gst = (By.XPATH, '//*[@id="REJECCONFIRM"]')
        self.check_on_active = (By.XPATH, '//*[@aria-label="Active"]')
        self.organisation_name = (By.XPATH, '//*[@class="font-size-16 text-color-1 mb-0 f-500"]')
        self.registration_type_default_value = (By.XPATH, '//*[@name="registrationType"]')
        self.assessee_of_other_territory = (By.XPATH, '(//*[@class="p-checkbox-box"])[1]')
        self.periodcity_drop_down_click = (By.XPATH, '(//i[@class="fi fi-ss-angle-small-down font-size-18"])[2]')
        self.click_on_cancel_for_assess_check_box = (By.XPATH, '//*[@id="REJECCONFIRM"]')
        self.select_monthly_in_periodcity_in_drop_down = (By.XPATH, '//div[normalize-space(text())="Monthly"]')
        self.cancel_button_in_editing_periodity = (By.XPATH, '//*[@id="REJECCONFIRM"]')
        self.gst_preferences_drop_down = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[3]')
        self.select_hsn_8 = (By.XPATH, '(//*[@class="list-inside-div overflow-elipsis"])[4]')
        self.enable_non_ad_valorem_cess = (
            By.XPATH, '//label[normalize-space(text())="Enable Non-Ad Valorem CESS"]//parent::div//child::div[2]')
        self.manual_entry = (By.XPATH, '//label[normalize-space(text())="Manual Entry"]//parent::div//child::div[2]')
        self.via_gst_rate_configuration = (
            By.XPATH, '//label[normalize-space(text())="Via GST Rate Configuration"]//parent::div//child::div[2]')
        self.tax_rate_history = (By.XPATH, '//*[@id="hb"]')
        self.click_on_default_rates = (By.XPATH, '//button[normalize-space(text())="Default Rates"]')
        self.e_way_bill = (By.XPATH, '//button[normalize-space(text())="E - Way Bill"]')
        self.e_way_bill_slider = (By.XPATH, '(//*[@class="p-inputswitch-slider"])[2]')
        self.applicable_from_in_e_way_bill = (By.XPATH, '//*[@name="eWayBill.applicableFrom"]')
        self.click_on_no_for_e_way_bill = (By.XPATH, '//*[@class="btn btn-outline-secondary p-l-r-20 body-text-color"]')
        self.click_on_e_invoice = (By.XPATH, '//button[normalize-space(text())="E - Invoice"]')
        self.click_on_e_invoice_slider = (By.XPATH, '(//*[@class="p-inputswitch-slider"])[2]')
        self.enter_applicable_from_in_gst = (By.XPATH, '//*[@name="eInvoice.applicableFrom"]')
        self.click_on_gst_in_address = (By.XPATH, '//*[normalize-space(text())="Address"]')
        self.click_on_attach_address = (By.XPATH, '//*[@id="ad0"]')
        self.click_on_add_address_inside = (By.XPATH, '//*[@class="fi fi-br-plus font-size-12"]')
        self.click_on_add_address_inside1 = (By.XPATH, '//*[@id="batman"]')
        self.name_feild_in_address = (By.XPATH, '//*[@id="z1"]')
        self.address_feild = (By.XPATH, '//textarea[@name="addressLine1"]')
        self.address_feild2 = (By.XPATH, '//*[@name="addressLine2"]')
        self.country_drop_down_in_address_in_gst = (
            By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[1]')
        self.click_on_india_in_country_drop_down = (By.XPATH, '//div[normalize-space(text())="India"]')
        self.click_on_state_drop_down = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[2]')
        self.click_on_andhrapradesh_on_state_drop_down = (By.XPATH, '//div[normalize-space(text())="Andhra Pradesh"]')
        self.city_input_feild = (By.XPATH, '//*[@name="city"]')
        self.enter_pincode = (By.XPATH, '//*[@id="z7"]')
        self.contact_no_drop_down = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[3]')
        self.contact_no_input_feild = (By.NAME, "mobileNumber")
        self.click_on_close_button = (By.XPATH, '//*[@class="p-dialog-header-close-icon pi pi-times"]')
        self.click_on_outside_close_button = (By.XPATH, '//*[@class="p-dialog-header-close-icon pi pi-times"]')
        self.click_on_tds_and_tcs = (By.XPATH, '//*[@id="m5"]')
        self.enable_tds_in_tds_tcs = (By.XPATH, '//*[@class="p-inputswitch-slider"]')
        self.enable_tds_button = (By.XPATH, '//*[@class="p-inputswitch-slider"]')
        self.enter_tax_deduction = (By.XPATH, '//*[@id="td3"]')
        self.deductor_type_dropdown = (By.XPATH, '//*[@class="fi fi-ss-angle-small-down font-size-18"]')
        self.click_on_company_in_drop_down = (By.XPATH, '//div[normalize-space(text())="Company"]')
        self.deductor_branch_or_division = (By.XPATH, '//input[@id="td5"]')
        self.click_on_add_authorized_person = (By.XPATH, '//*[@class="fi fi-br-plus font-size-12"]')
        self.enter_name_in_authorized_person = (By.XPATH, '//*[@id="a1"]')
        self.son_daughter_of_in_authorized_person = (By.ID, "a2")
        self.designation_in_authorized_person = (By.XPATH, '//*[@id="a3"]')
        self.pan_feild_authorized_person = (By.XPATH, '//*[@id="a4"]')
        self.flat_no_in_authorized_address = (By.XPATH, '//*[@id="a5"]')
        self.name_of_premesis = (By.XPATH, '//*[@id="a6"]')
        self.road_street_name = (By.XPATH, '//*[@id="a7"]')
        self.area_location = (By.XPATH, '//*[@id="a8"]')
        self.town_street_district = (By.XPATH, '//*[@id="a9"]')
        self.click_on_state_drop_down = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[2]')
        self.click_on_andhrapradesh = (By.XPATH, '//*[@title="Andhra Pradesh"]')
        self.enter_pincode = (By.XPATH, '//input[@name="pincode"]')
        self.click_drop_down_in_contact_details = (
            By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[3]')
        self.contact_details_input_feild = (By.XPATH, '//input[@id="a12"]')
        self.alternative_contact_no_drop_down = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[4]')
        self.alternative_contact_no_input_feild = (By.XPATH, '//*[@id="a13"]')
        self.email_id_tds = (By.XPATH, '//*[@id="a14"]')
        self.alternative_email_id_tds = (By.XPATH, '//*[@id="a15"]')
        self.click_on_tcs_button = (By.XPATH, '//button[normalize-space(text())="TCS"]')
        self.click_on_enable_tcs_button = (By.XPATH, '//span[@class="p-inputswitch-slider"]')
        self.tan_input_feild_in_tcs = (By.XPATH, '//input[@name="tcs.taxCollectionDeductionNumber"]')
        self.click_on_collectee_type_drop_down = (By.XPATH, '//i[@class="fi fi-ss-angle-small-down font-size-18"]')
        self.select_company_in_collectee_drop_down = (By.XPATH, '//div[normalize-space(text())="Company"]')
        self.collectee_branch_division = (By.XPATH, '//input[@name="tcs.collectorBranchDivision"]')
        self.add_authorized_person = (By.XPATH, '//button[@class="btn btn-outline-primary text-start border-dashed"]')
        self.name_feild_in_authorized_person = (By.XPATH, '(//input[@class="form-control  h-40px  f-c-b bg-white"])[3]')
        self.son_daughter_name_in_add_authorized = (By.XPATH, '//*[@name="fatherOrHusbandName"]')
        self.designation_feild_in_tcs = (By.XPATH, '//*[@name="designation" and @id="a3"]')
        self.click_on_close_button_in_authorized_feild = (
            By.XPATH, '//*[@class="p-dialog-header-close-icon pi pi-times"]')
        self.click_on_other_statutory = (By.XPATH, '//*[@name="Other Statutory"]')
        self.select_incorporate_drop_down = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[1]')
        self.click_on_pvt_ltd_company_in_incorporate_type_drop_down = (
            By.XPATH, '//div[normalize-space(text())="Private Limited Company"]')
        self.incorporation_no = (By.XPATH, '//input[@name="incorporationNumber"]')
        self.iec_number = (By.XPATH, '//input[@name="iecNumber"]')
        self.date_of_issue = (By.XPATH, '//input[@name="dateOfIssue"]')
        self.last_modified_date = (By.XPATH, '//input[@name="lastModifiedDate" or @id="os5"]')
        self.name_of_signatory_input_feild = (By.XPATH, '//*[@name="nameOfSignatory" or @id="os6" ]')
        self.check_status_active = (By.XPATH, '//span[normalize-space(text())="Active"]')
        self.registration_type_in_msme = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[2]')
        self.click_on_small = (By.XPATH, '//div[normalize-space(text())="Small"]')
        self.date_of_registration_input = (By.XPATH, '//*[@name="dateOfRegistration" or @id="os8"]')
        self.udyam_registration_no_input_feild = (By.XPATH, '//*[@name="udyamRegistrationNumber" or @id="os9"]')
        self.branding_button = (By.XPATH, '//button[@name="Branding" or @id="m7"]')
        self.upload_image = (By.XPATH, '//*[@name="upload"]')
        self.contact_no = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[1]')
        self.contact_no_input = (By.XPATH, '//*[@name="mobileNumber"]')
        self.alternative_no_drop_down = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[2]')
        self.alternative_input_feild = (By.XPATH, '//*[@name="alternativeMobileNumber"]')
        self.email_id = (By.XPATH, '//*[@name="email"]')
        self.alternative_email_id = (By.XPATH, '//*[@name="alternativeEmail" or @id="b6"]')
        self.website = (By.XPATH, '//*[@name="website" or id="b7"]')
        self.linked_in = (By.XPATH, '//*[@name="linkedin"]')
        self.facebook = (By.XPATH, '//*[@name="facebook" or id="b9"]')
        self.youtube = (By.XPATH, '//*[@name="youtube" or id="b10"]')
        self.snap_chat = (By.XPATH, '//*[@name="snapchat" or id="b11"]')
        self.Instagram = (By.XPATH, '//*[@name="instagram" or id="b12"]')
        self.click_on_add_addresses = (By.XPATH, '//*[@name="Addresses" or id="m8"]')

    def click_create_organisation_button_after_login(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        create_organisation_dropdown_locator = wait.until(
            EC.element_to_be_clickable(self.create_organisation_dropdown))
        actions = ActionChains(self.driver)
        actions.move_to_element(create_organisation_dropdown_locator).click().perform()
        time.sleep(3)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_create_organisation_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_create_organisation))
        # self.driver.execute_script("arguments[0].click();", click_on_create_organisation_locator)
        actions.move_to_element(click_on_create_organisation_locator).click().perform()

    def legal_name_element(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        legal_name_locator = wait.until(
            EC.presence_of_element_located(self.legal_name))
        legal_name_locator.send_keys("EcoScribe Solutions")

    def legal_name_attribute(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        legal_name_locator = wait.until(
            EC.presence_of_element_located(self.legal_name))
        Attribute_value_legal_name = legal_name_locator.get_attribute("value")
        print(Attribute_value_legal_name)
        return Attribute_value_legal_name

    def alias_name_feild(self):
        # alias name
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        alias_feild_locator = wait.until(
            EC.presence_of_element_located(self.alias_feild))
        alias_feild_locator.send_keys("EcoScribe")

    def alias_feild_attribute_value(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        alias_feild_locator = wait.until(
            EC.presence_of_element_located(self.alias_feild))
        Attribute_value_alias = alias_feild_locator.get_attribute("value")
        return Attribute_value_alias

    def country_feild(self):
        # country
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            country_drop_down_click_locator = wait.until(
                EC.element_to_be_clickable(self.country_drop_down_click))
            self.driver.execute_script("arguments[0].click();", country_drop_down_click_locator)
            for _ in range(2):
                pyautogui.press('up')
                time.sleep(0.3)
            for _ in range(2):
                pyautogui.press('down')
                time.sleep(0.3)
            pyautogui.press("enter")
        except (StaleElementReferenceException, TimeoutException):
            pass

    def country_feild_attribute_value(self):
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            country_input_feild_in_create_organisation_locator = wait.until(
                EC.presence_of_element_located(self.country_input_feild_in_create_organisation))
            Attribute_value_country_input_feild_in_create_organisation_locator = country_input_feild_in_create_organisation_locator.get_attribute(
                "value")
            return Attribute_value_country_input_feild_in_create_organisation_locator
        except (StaleElementReferenceException, TimeoutException):
            pass

    def currency(self):
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            currency_drop_down_click_locator = wait.until(
                EC.element_to_be_clickable(self.currency_drop_down_click))
            self.driver.execute_script("arguments[0].click();", currency_drop_down_click_locator)
            pyautogui.press('up')
            time.sleep(1)
            pyautogui.press('down')
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.press("space")
            time.sleep(0.5)
            #  GST
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            gst_in_locator = wait.until(
                EC.element_to_be_clickable(self.gst_in))
            gst_in_locator.send_keys("24AABCA9602Q1ZG")
            time.sleep(1)
            # gst active
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            click_on_gst_active_locator = wait.until(
                EC.presence_of_element_located(self.click_on_gst_active))

            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_gst_active_locator).perform()
            time.sleep(1)
            actions.move_to_element(click_on_gst_active_locator).click().perform()
            time.sleep(1)
            # state
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            state_locator = wait.until(
                EC.presence_of_element_located(self.state))
            if state_locator.is_enabled():
                print("state feild by default it is in enabled state")
            else:
                print("state feild by default it is in disabled state")
            time.sleep(2)
            Attribute_value = state_locator.get_attribute("value")
            time.sleep(2)
            Expected_value = "Gujarat"
            if Attribute_value == Expected_value:
                print(f"Both {Attribute_value} and {Expected_value} are equal")
            else:
                print(f"Both {Attribute_value} and {Expected_value} are not equal")
            GST_value = "24AABCA9602Q1ZG"

            sliced_string = GST_value[2:-3]
            print(sliced_string)
            #  pan value
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            pan_value_locator = wait.until(
                EC.presence_of_element_located(self.pan_value))
            pan_attribute_value = pan_value_locator.get_attribute("value")
            if pan_attribute_value == sliced_string:
                print(f"Both {pan_attribute_value} and {sliced_string} are equal")
            else:
                print(f"Both {pan_attribute_value} and {sliced_string} are not equal")
            # save
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            save_button_locator = wait.until(
                EC.element_to_be_clickable(self.save_button))
            actions.move_to_element(save_button_locator).click().perform()
            time.sleep(2)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            click_on_organisation_settings_after_save_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_organisation_settings_after_save))
            actions.move_to_element(click_on_organisation_settings_after_save_locator).click().perform()

            # wait = WebDriverWait(self.driver, 50, poll_frequency=3,
            #                      ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            # click_on_organisation_settings_locator = wait.until(
            #     EC.element_to_be_clickable(self.click_on_organisation_settings))
            # actions.move_to_element(click_on_organisation_settings_locator).click().perform()
            # time.sleep(5)
            # wait = WebDriverWait(self.driver, 50, poll_frequency=3,
            #                      ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            # click_on_organisation_settings_locator = wait.until(
            #     EC.element_to_be_clickable(self.organisation_settings_inside))
            # click_on_organisation_settings_locator.click()
            # # actions.move_to_element(click_on_organisation_settings_locator).click().perform()

            # pyautogui.press('down')
            # time.sleep(0.5)
            # pyautogui.press('up')
            # time.sleep(0.5)
            # pyautogui.press('enter')
            # time.sleep(0.5)

            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            legal_name_in_primary_details_locator = wait.until(
                EC.presence_of_element_located(self.legal_name_in_primary_details))
            Attribute_value_of_legal_name_in_primary_details = (legal_name_in_primary_details_locator
                                                                .get_attribute("value"))
            Attribute_value_legal_name_main = self.legal_name_attribute()

            if Attribute_value_legal_name_main == Attribute_value_of_legal_name_in_primary_details:
                print(
                    f"both {Attribute_value_legal_name_main} and {Attribute_value_of_legal_name_in_primary_details} are equal")
            else:
                print(
                    f"both {Attribute_value_legal_name_main} and {Attribute_value_of_legal_name_in_primary_details} are not  equal")
        except (StaleElementReferenceException, TimeoutException):
            pass

    def alias_comparsion_from_main_page_to_alias_in_primary(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        alias_name_in_primary_details_locator = wait.until(
            EC.presence_of_element_located(self.alias_name_in_primary_details))
        Attribute_value_alias_name_primary_details = alias_name_in_primary_details_locator.get_attribute("value")
        print("2", Attribute_value_alias_name_primary_details)
        time.sleep(6)
        try:
            alias_feild_attribute_value_locator = self.alias_feild_attribute_value()
            time.sleep(4)
            if alias_feild_attribute_value_locator == Attribute_value_alias_name_primary_details:
                print(
                    f"Both {Attribute_value_alias_name_primary_details} and {alias_feild_attribute_value_locator} are equal")
            else:
                print(
                    f"Both {Attribute_value_alias_name_primary_details} and {alias_feild_attribute_value_locator} are not equal")
        except (TimeoutException, ElementClickInterceptedException):
            pass

    def country_and_currency_to_main_to_feilds_in_primary_details(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        country_feild_in_primary_feild_locator = wait.until(
            EC.presence_of_element_located(self.country_feild_in_primary_feild))
        Attribute_value_country_feild_primary_details = country_feild_in_primary_feild_locator.get_attribute("value")
        print("2", Attribute_value_country_feild_primary_details)
        time.sleep(5)
        try:
            country_feild_attribute_value_locator = self.country_feild_attribute_value()
            time.sleep(4)
            if country_feild_attribute_value_locator == Attribute_value_country_feild_primary_details:
                print(
                    f"Both {Attribute_value_country_feild_primary_details} and {country_feild_attribute_value_locator} are equal")
            else:
                print(
                    f"Both {Attribute_value_country_feild_primary_details} and {country_feild_attribute_value_locator} are not equal")
            # currency
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            currency_feild_in_primary_details_locator = wait.until(
                EC.presence_of_element_located(self.currency_feild_in_primary_details))
            Attribute_value_of_currency_in_primary_details = currency_feild_in_primary_details_locator.get_attribute(
                "value")
            print(Attribute_value_of_currency_in_primary_details)

            # GST-In
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            Gst_in_in_primary_details_locator = wait.until(
                EC.presence_of_element_located(self.Gst_in_in_primary_details))
            Attribute_value_of_GST_IN_in_primary_details = Gst_in_in_primary_details_locator.get_attribute("value")
            print(Attribute_value_of_GST_IN_in_primary_details)
        except (TimeoutException, ElementClickInterceptedException, StaleElementReferenceException):
            pass
        time.sleep(5)

    def configuration_in_primary_details(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_configuration_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_configuration))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_configuration_locator).click().perform()
        time.sleep(4)

        # Books beginning from
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        books_begining_from_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.books_begining_from_input_feild))
        books_begining_from_input_feild_locator.send_keys(Keys.END)
        Attribute_value_of_books_beginning_from = books_begining_from_input_feild_locator.get_attribute("value")
        for _ in Attribute_value_of_books_beginning_from:
            books_begining_from_input_feild_locator.send_keys(Keys.BACKSPACE)
        time.sleep(3)
        books_begining_from_input_feild_locator.send_keys("31/3/2000")

        # click on yes for books beginning date
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            click_on_yes_button_for_books_begginning_from_date_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_yes_button_for_books_begginning_from_date))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_yes_button_for_books_begginning_from_date_locator).click().perform()
        except (StaleElementReferenceException, TimeoutException, ElementClickInterceptedException):
            pass
        time.sleep(0.5)
        actions.send_keys(Keys.TAB).perform()

        # Default Accounting period
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        accounting_drop_down_click_locator = wait.until(
            EC.element_to_be_clickable(self.accounting_drop_down_click))
        actions.move_to_element(accounting_drop_down_click_locator).click().perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        default_accounting_period_in_configuration_locator = wait.until(
            EC.presence_of_element_located(self.default_accounting_period_in_configuration))
        actions.move_to_element(default_accounting_period_in_configuration_locator).click().perform()

        # currency in configuration
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_currency_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_currency_drop_down))
        actions.move_to_element(click_on_currency_drop_down_locator).click().perform()

        # click on indian rupee
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_indian_rupee_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_indian_rupee))
        actions.move_to_element(click_on_indian_rupee_locator).click().perform()

        # ISO code
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        ISO_code_locator = wait.until(
            EC.presence_of_element_located(self.ISO_code))
        Attribute_value_iso_code = ISO_code_locator.get_attribute("value")
        print(Attribute_value_iso_code)
        Expected_attribute_value_for_indian_rupee = "INR"
        if Attribute_value_iso_code == Expected_attribute_value_for_indian_rupee:
            print(f"Both {Attribute_value_iso_code} and {Expected_attribute_value_for_indian_rupee} are equal")
        else:
            print(f"Both {Attribute_value_iso_code} and {Expected_attribute_value_for_indian_rupee} are not  equal")
        if ISO_code_locator.is_enabled():
            print(f"ISO code defaultly is in enabled state")
        else:
            print(f"ISO code defaultly is in disabled state")
        # Date
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        date_format_locator = wait.until(
            EC.presence_of_element_located(self.date_format))
        if date_format_locator.is_selected():
            print(f"Defaulty dd/mm/yy is in selected mode")
        else:
            print(f"DD/MM/YY is defaulty in selected mode")

    def Features_all_feilds(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_features_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_features))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_features_locator).click().perform()

        # edit log check box
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        edit_log_check_box_locator = wait.until(
            EC.presence_of_element_located(self.edit_log_check_box))
        if edit_log_check_box_locator.is_selected():
            print("Edit log check box defaultly in selected state")
        else:
            print("Edit log check box defaultly in Unselected state")

        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('space')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('space')

        # Enable bill wise entries
        # wait = WebDriverWait(self.driver, 50, poll_frequency=3,
        #                      ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        # enable_bill_wise_entries_check_box_locator = wait.until(
        #     EC.element_to_be_clickable(self.enable_bill_wise_entries_check_box))
        # actions.move_to_element(enable_bill_wise_entries_check_box_locator).click().perform()
        #
        # # Enable cost centres
        # wait = WebDriverWait(self.driver, 50, poll_frequency=3,
        #                      ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        # Enable_cost_centers_locator = wait.until(
        #     EC.element_to_be_clickable(self.Enable_cost_centers))
        # actions.move_to_element(Enable_cost_centers_locator).click().perform()

    def click_on_inventory_elements(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_inventory_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_inventory))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_inventory_locator).click().perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        maintain_inventory_feild_locator = wait.until(
            EC.element_to_be_clickable(self.maintain_inventory_feild))
        actions = ActionChains(self.driver)
        actions.move_to_element(maintain_inventory_feild_locator).click().perform()
        time.sleep(2)
        actions.move_to_element(maintain_inventory_feild_locator).click().perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        Inventory_check_boxes_locators = wait.until(
            EC.visibility_of_all_elements_located(self.Inventory_check_boxes))
        try:
            if maintain_inventory_feild_locator.is_selected():
                for checkbox in Inventory_check_boxes_locators:
                    if checkbox.is_selected():
                        print("Checkbox is selected")
                    else:
                        print("Checkbox is not selected")
        except AttributeError:
            pass
        else:
            print("maintain inventory feild is not selected")

    def GST_feild_in_primary_details(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_GST_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_GST))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_GST_locator).click().perform()
        time.sleep(5)

        click_on_GST_slider_locator = wait.until(
            EC.presence_of_element_located(self.click_on_GST_slider))
        if click_on_GST_slider_locator.is_selected():
            print("GST slider is defaulty in selected state")
        else:
            print("GST slider is defaulty not in selected state")

        enter_gst_in_gst_in_configuration = wait.until(
            EC.presence_of_element_located(self.enter_gst_in_gst_in_configuration))
        enter_gst_in_gst_in_configuration.send_keys("37AECPJ3940A1Z0")

        name_applicable_from_in_inside_confirmation_box_locator = wait.until(
            EC.presence_of_element_located(self.name_applicable_from_in_inside_confirmation_box))
        name_applicable_from_in_inside_confirmation_box_locator.send_keys("01/04/2023")

        click_on_proceed_in_gst_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_cancel_in_gst))
        actions.move_to_element(click_on_proceed_in_gst_locator).click().perform()

        enter_registration_name_in_gst_locator = wait.until(
            EC.presence_of_element_located(self.enter_registration_name_in_gst))
        Attribute_value_of_registration_name = enter_registration_name_in_gst_locator.get_attribute("value")
        Expected_value = "Andhra Pradesh Registration"
        if Attribute_value_of_registration_name == Expected_value:
            print(f"Both {Attribute_value_of_registration_name} and {Expected_value} are equal")
        else:
            print(f"Both {Attribute_value_of_registration_name} and {Expected_value} are not equal")

        check_on_active_locator = wait.until(
            EC.visibility_of_element_located(self.check_on_active))
        if check_on_active_locator.is_displayed():
            print(f"active symbol is displayed")
        else:
            print(f"active symbol is not displayed")
        time.sleep(4)

        organisation_name_locator = wait.until(
            EC.visibility_of_element_located(self.organisation_name))
        time.sleep(3)
        Attribute_value = organisation_name_locator.get_attribute("value")
        time.sleep(3)
        if organisation_name_locator.is_displayed():
            Expected_text = "APOLLO ELECTRICALS & BUILDING MATERIALS"
            if Expected_text == Attribute_value:
                print(f"Both {Attribute_value} and {Expected_text} are equal")
            else:
                print(f"Both {Attribute_value} and {Expected_text} are equal")
        else:
            print("Trade name not displayed")

        registration_type_default_value_locator = wait.until(
            EC.visibility_of_element_located(self.registration_type_default_value))
        Attribute_value_registration_value = registration_type_default_value_locator.get_attribute("value")
        Expected_value = "Regular"
        if Attribute_value_registration_value == Expected_value:
            print(f"Both {Attribute_value_registration_value} and {Expected_value} are equal")
        else:
            print(f"Both {Attribute_value_registration_value} and {Expected_value} are not equal")

        assessee_of_other_territory_locator = wait.until(
            EC.presence_of_element_located(self.assessee_of_other_territory))
        if assessee_of_other_territory_locator.is_selected():
            print("defaulty assessee is selected state")
        else:
            print("defaulty assessee is not in selected state")
        actions.move_to_element(assessee_of_other_territory_locator).click().perform()

        # click cancel for assess
        click_on_cancel_for_assess_check_box_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_cancel_for_assess_check_box))
        actions.move_to_element(click_on_cancel_for_assess_check_box_locator).click().perform()

        periodcity_drop_down_click_locator = wait.until(
            EC.element_to_be_clickable(self.periodcity_drop_down_click))
        actions.move_to_element(periodcity_drop_down_click_locator).click().perform()

        select_monthly_in_periodcity_in_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.select_monthly_in_periodcity_in_drop_down))
        actions.move_to_element(select_monthly_in_periodcity_in_drop_down_locator).click().perform()

        cancel_button_in_editing_periodity_locator = wait.until(
            EC.element_to_be_clickable(self.cancel_button_in_editing_periodity))
        actions.move_to_element(cancel_button_in_editing_periodity_locator).click().perform()

    def GST_remaining_feilds(self):
        # GST preferences
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        cancel_button_in_editing_periodity_locator = wait.until(
            EC.element_to_be_clickable(self.cancel_button_in_editing_periodity))
        actions = ActionChains(self.driver)
        actions.move_to_element(cancel_button_in_editing_periodity_locator).click().perform()

        gst_preferences_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.gst_preferences_drop_down))
        actions.move_to_element(gst_preferences_drop_down_locator).click().perform()

        select_hsn_8_locator = wait.until(
            EC.element_to_be_clickable(self.select_hsn_8))
        actions.move_to_element(select_hsn_8_locator).click().perform()

        # non-ad valorem cess
        enable_non_ad_valorem_cess_locator = wait.until(
            EC.element_to_be_clickable(self.enable_non_ad_valorem_cess))
        actions.move_to_element(enable_non_ad_valorem_cess_locator).click().perform()

    def Default_rates_all(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_default_rates_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_default_rates))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_default_rates_locator).click().perform()

        manual_entry_locator = wait.until(
            EC.presence_of_element_located(self.manual_entry))
        if manual_entry_locator.is_selected():
            print(f"manual entry defaulty in selected state")
        else:
            print(f"manual entry defaulty not in selected state")

        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        via_gst_rate_configuration_locator = wait.until(
            EC.presence_of_element_located(self.via_gst_rate_configuration))
        if via_gst_rate_configuration_locator.is_selected():
            print(f"via gst rate configuration defaulty in selected state")
        else:
            print(f"via gst rate configuration defaulty not in selected state")

        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        tax_rate_history_locator = wait.until(
            EC.visibility_of_element_located(self.tax_rate_history))
        if tax_rate_history_locator.is_displayed():
            print(f"Tax rate history is displayed")
        else:
            print(f"Tax rate history is not displayed")

    def E_way_bill(self):
        # wait = WebDriverWait(self.driver, 50, poll_frequency=3,
        #                      ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        # e_way_bill_locator = wait.until(
        #     EC.element_to_be_clickable(self.e_way_bill))
        # actions = ActionChains(self.driver)
        # actions.move_to_element(e_way_bill_locator).click().perform()
        # time.sleep(2)
        #
        # e_way_bill_slider_locator = wait.until(
        #     EC.element_to_be_clickable(self.e_way_bill_slider))
        # actions = ActionChains(self.driver)
        # actions.move_to_element(e_way_bill_slider_locator).click().perform()
        # time.sleep(2)
        #
        # applicable_from_in_e_way_bill_locator = wait.until(
        #     EC.presence_of_element_located(self.applicable_from_in_e_way_bill))
        # applicable_from_in_e_way_bill_locator.send_keys("01/04/2024")
        # time.sleep(2)

        # # click on no for e-way bill
        # click_on_no_for_e_way_bill_locator = wait.until(
        #     EC.element_to_be_clickable(self.click_on_no_for_e_way_bill))
        # actions.move_to_element(click_on_no_for_e_way_bill_locator).click().perform()
        # time.sleep(2)

        # e-invoice
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_e_invoice_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_e_invoice))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_e_invoice_locator).click().perform()
        time.sleep(2)

        click_on_e_invoice_slider_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_e_invoice_slider))
        actions.move_to_element(click_on_e_invoice_slider_locator).click().perform()
        time.sleep(2)

        enter_applicable_from_in_gst_locator = wait.until(
            EC.presence_of_element_located(self.enter_applicable_from_in_gst))
        enter_applicable_from_in_gst_locator.send_keys("01/04/2025")

        # Address
        click_on_gst_in_address_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_gst_in_address))
        actions.move_to_element(click_on_gst_in_address_locator).click().perform()

        click_on_attach_address_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_attach_address))
        actions.move_to_element(click_on_attach_address_locator).click().perform()

        click_on_add_address_inside_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_add_address_inside))
        actions.move_to_element(click_on_add_address_inside_locator).click().perform()

        # Enter Address
        click_on_add_address_inside1_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_add_address_inside1))
        actions.move_to_element(click_on_add_address_inside1_locator).click().perform()

        name_feild_in_address_locator = wait.until(
            EC.presence_of_element_located(self.name_feild_in_address))
        name_feild_in_address_locator.send_keys("P.Dinesh Kumar")

        address_feild_locator = wait.until(
            EC.presence_of_element_located(self.address_feild))
        address_feild_locator.send_keys("41-4-3/11F,Garapati Industrial Area,East Godavari,Andhra Pradesh,533103")

        address_feild2_locator = wait.until(
            EC.presence_of_element_located(self.address_feild2))
        address_feild2_locator.send_keys("41-4-3/11F,Garapati Industrial Area,East Godavari,Andhra Pradesh,533103")

        country_drop_down_in_address_in_gst_locator = wait.until(
            EC.element_to_be_clickable(self.country_drop_down_in_address_in_gst))
        actions.move_to_element(country_drop_down_in_address_in_gst_locator).click().perform()

        click_on_india_in_country_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_india_in_country_drop_down))
        actions.move_to_element(click_on_india_in_country_drop_down_locator).click().perform()
        time.sleep(5)
        try:
            click_on_state_drop_down_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_state_drop_down))
            actions.move_to_element(click_on_state_drop_down_locator).click().perform()

            click_on_andhrapradesh_on_state_drop_down_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_andhrapradesh_on_state_drop_down))
            actions.move_to_element(click_on_andhrapradesh_on_state_drop_down_locator).click().perform()
        except (TimeoutException, StaleElementReferenceException):
            pass

        city_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.city_input_feild))
        city_input_feild_locator.send_keys("Hyderabad")

        enter_pincode_locator = wait.until(
            EC.presence_of_element_located(self.enter_pincode))
        enter_pincode_locator.send_keys("533103")

        contact_no_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.contact_no_drop_down))
        actions.move_to_element(contact_no_drop_down_locator).click().perform()

        pyautogui.FAILSAFE = False
        pyautogui.press('up')
        pyautogui.press('down')

        contact_no_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.contact_no_input_feild))
        contact_no_input_feild_locator.send_keys("123456789")

        click_on_close_button_locator = wait.until(
            EC.presence_of_element_located(self.click_on_close_button))
        actions.move_to_element(click_on_close_button_locator).click().perform()
        time.sleep(3)

        click_on_outside_close_button_locator = wait.until(
            EC.presence_of_element_located(self.click_on_outside_close_button))
        actions.move_to_element(click_on_outside_close_button_locator).click().perform()
        time.sleep(3)

    def tds_in_organisation_settings(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_tds_and_tcs_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_tds_and_tcs))
        # actions.move_to_element(click_on_tds_and_tcs_locator).click().perform()
        self.driver.execute_script("arguments[0].click();", click_on_tds_and_tcs_locator)

        actions = ActionChains(self.driver)
        enable_tds_button_locator = wait.until(
            EC.element_to_be_clickable(self.enable_tds_button))
        actions.move_to_element(enable_tds_button_locator).click().perform()

        enter_tax_deduction_locator = wait.until(
            EC.presence_of_element_located(self.enter_tax_deduction))
        enter_tax_deduction_locator.send_keys("HYDFM26917C")

        deductor_type_dropdown_locator = wait.until(
            EC.element_to_be_clickable(self.deductor_type_dropdown))
        actions.move_to_element(deductor_type_dropdown_locator).click().perform()

        click_on_company_in_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_company_in_drop_down))
        actions.move_to_element(click_on_company_in_drop_down_locator).click().perform()

        deductor_branch_or_division_locator = wait.until(
            EC.presence_of_element_located(self.deductor_branch_or_division))
        deductor_branch_or_division_locator.send_keys("Hyderabad")

        click_on_add_authorized_person_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_add_authorized_person))
        actions.move_to_element(click_on_add_authorized_person_locator).click().perform()

        enter_name_in_authorized_person_locator = wait.until(
            EC.presence_of_element_located(self.enter_name_in_authorized_person))
        enter_name_in_authorized_person_locator.send_keys("Lakshminarayana Murthy")

        son_daughter_of_in_authorized_person_locator = wait.until(
            EC.presence_of_element_located(self.son_daughter_of_in_authorized_person))
        son_daughter_of_in_authorized_person_locator.send_keys("Narasimha")

        designation_in_authorized_person_locator = wait.until(
            EC.presence_of_element_located(self.designation_in_authorized_person))
        designation_in_authorized_person_locator.send_keys("CEO")

        pan_feild_authorized_person_locator = wait.until(
            EC.presence_of_element_located(self.pan_feild_authorized_person))
        pan_feild_authorized_person_locator.send_keys("FSFPM35642")

        flat_no_in_authorized_address_locator = wait.until(
            EC.presence_of_element_located(self.flat_no_in_authorized_address))
        flat_no_in_authorized_address_locator.send_keys("201")

        name_of_premesis_locator = wait.until(
            EC.presence_of_element_located(self.name_of_premesis))
        name_of_premesis_locator.send_keys("Krishna Nilayam")

        road_street_name_locator = wait.until(
            EC.presence_of_element_located(self.road_street_name))
        road_street_name_locator.send_keys("Krishna Nilayam veedhi")

        area_location_locator = wait.until(
            EC.presence_of_element_located(self.area_location))
        area_location_locator.send_keys("Himayath Nagar")

        town_street_district_locator = wait.until(
            EC.presence_of_element_located(self.town_street_district))
        town_street_district_locator.send_keys("Hyderabad")

        click_on_state_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_state_drop_down))
        actions.move_to_element(click_on_state_drop_down_locator).click().perform()

        click_on_andhrapradesh_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_andhrapradesh))
        actions.move_to_element(click_on_andhrapradesh_locator).click().perform()

        enter_pincode_locator = wait.until(
            EC.presence_of_element_located(self.enter_pincode))
        enter_pincode_locator.send_keys("500044")

        click_drop_down_in_contact_details_locator = wait.until(
            EC.element_to_be_clickable(self.click_drop_down_in_contact_details))
        actions.move_to_element(click_drop_down_in_contact_details_locator).click().perform()

        pyautogui.FAILSAFE = False
        pyautogui.press('up')
        pyautogui.press('down')

        contact_details_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.contact_details_input_feild))
        contact_details_input_feild_locator.send_keys("7898438989")

        # alternative contact no.
        alternative_contact_no_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.alternative_contact_no_drop_down))
        actions.move_to_element(alternative_contact_no_drop_down_locator).click().perform()

        alternative_contact_no_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.alternative_contact_no_input_feild))
        alternative_contact_no_input_feild_locator.send_keys("9666669016")

        email_id_locator = wait.until(
            EC.presence_of_element_located(self.email_id_tds))
        email_id_locator.send_keys("shreenu@kitaab.biz")

        alternative_email_id_locator = wait.until(
            EC.presence_of_element_located(self.alternative_email_id_tds))
        alternative_email_id_locator.send_keys("sambhaaru@kitaab.biz")

        pyautogui.press('esc')
        time.sleep(5)

    def click_on_tcs(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_tcs_button_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_tcs_button))
        # actions = ActionChains(self.driver)
        # actions.move_to_element(click_on_tcs_button_locator).click().perform()
        self.driver.execute_script("arguments[0].click();", click_on_tcs_button_locator)

        click_on_enable_tcs_button_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_enable_tcs_button))
        if click_on_enable_tcs_button_locator.is_selected():
            print("defaulty tcs is in selected state")
        else:
            print("defaulty tcs is not in selected state")
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_enable_tcs_button_locator).click().perform()

        # tan feild in tcs
        tan_input_feild_in_tcs_locator = wait.until(
            EC.presence_of_element_located(self.tan_input_feild_in_tcs))
        tan_input_feild_in_tcs_locator.send_keys("MUMT23405E")

        # collectee type drop down
        click_on_collectee_type_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_collectee_type_drop_down))
        actions.move_to_element(click_on_collectee_type_drop_down_locator).click().perform()

        select_company_in_collectee_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.select_company_in_collectee_drop_down))
        actions.move_to_element(select_company_in_collectee_drop_down_locator).click().perform()

        collectee_branch_division_locator = wait.until(
            EC.presence_of_element_located(self.collectee_branch_division))
        collectee_branch_division_locator.send_keys("Mumbai")

        add_authorized_person_locator = wait.until(
            EC.presence_of_element_located(self.add_authorized_person))
        actions.move_to_element(add_authorized_person_locator).click().perform()

        name_feild_in_authorized_person_locator = wait.until(
            EC.presence_of_element_located(self.name_feild_in_authorized_person))
        actions.move_to_element(name_feild_in_authorized_person_locator).click().perform()

        son_daughter_name_in_add_authorized_locator = wait.until(
            EC.presence_of_element_located(self.son_daughter_name_in_add_authorized))
        son_daughter_name_in_add_authorized_locator.send_keys("Chandrasekaran")

        designation_feild_in_tcs_locator = wait.until(
            EC.presence_of_element_located(self.designation_feild_in_tcs))
        designation_feild_in_tcs_locator.send_keys("Chairman")

        click_on_close_button_in_authorized_feild_locator = wait.until(
            EC.presence_of_element_located(self.click_on_close_button_in_authorized_feild))
        actions.move_to_element(click_on_close_button_in_authorized_feild_locator).click().perform()

    def other_statutory(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_other_statutory_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_other_statutory))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_other_statutory_locator).click().perform()

        select_incorporate_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.select_incorporate_drop_down))
        actions.move_to_element(select_incorporate_drop_down_locator).click().perform()

        select_incorporate_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.select_incorporate_drop_down))
        actions.move_to_element(select_incorporate_drop_down_locator).click().perform()

        click_on_pvt_ltd_company_in_incorporate_type_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_pvt_ltd_company_in_incorporate_type_drop_down))
        actions.move_to_element(click_on_pvt_ltd_company_in_incorporate_type_drop_down_locator).click().perform()

        incorporation_no_locator = wait.until(
            EC.presence_of_element_located(self.incorporation_no))
        incorporation_no_locator.send_keys("U72200KA2013PTC097389")

        # IEC code
        iec_number_locator = wait.until(
            EC.presence_of_element_located(self.iec_number))
        iec_number_locator.send_keys("ABCDE1345K")

        date_of_issue_locator = wait.until(
            EC.presence_of_element_located(self.date_of_issue))
        date_of_issue_locator.send_keys("01/04/2024")

        last_modified_date_locator = wait.until(
            EC.presence_of_element_located(self.last_modified_date))
        last_modified_date_locator.send_keys("01/04/2024")

        name_of_signatory_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.name_of_signatory_input_feild))
        name_of_signatory_input_feild_locator.send_keys("Abhi ram")

        check_status_active_locator = wait.until(
            EC.presence_of_element_located(self.check_status_active))
        status_text = check_status_active_locator.text
        Expected_text = "Active"
        if status_text == Expected_text:
            print(f"Both {status_text} and {Expected_text} are equal")
        else:
            print(f"Both {status_text} and {Expected_text} are not equal")

    def MSME(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        registration_type_in_msme_locator = wait.until(
            EC.element_to_be_clickable(self.registration_type_in_msme))
        actions = ActionChains(self.driver)
        actions.move_to_element(registration_type_in_msme_locator).click().perform()

        click_on_small_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_small))
        actions.move_to_element(click_on_small_locator).click().perform()

        date_of_registration_input_locator = wait.until(
            EC.presence_of_element_located(self.date_of_registration_input))
        date_of_registration_input_locator.send_keys("01/04/2024")

        udyam_registration_no_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.udyam_registration_no_input_feild))
        udyam_registration_no_input_feild_locator.send_keys("UDYAM-DL-02-0123457")

    def branding(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        branding_button_locator = wait.until(
            EC.element_to_be_clickable(self.branding_button))
        actions = ActionChains(self.driver)
        actions.move_to_element(branding_button_locator).click().perform()

        upload_image_locator = wait.until(
            EC.element_to_be_clickable(self.upload_image))
        actions.move_to_element(upload_image_locator).click().perform()

        file_path = "C:\\Users\\Dinesh\\Downloads\\Kitaabh-Logo-1111x258-black-double-size 1-20240919-123908.png"
        pyautogui.write(file_path)
        pyautogui.press('enter')

        # contact no
        contact_no = wait.until(
            EC.element_to_be_clickable(self.contact_no))
        actions.move_to_element(contact_no).click().perform()

        pyautogui.FAILSAFE = False
        pyautogui.press('up')
        pyautogui.press('down')

        contact_no_input_locator = wait.until(
            EC.presence_of_element_located(self.contact_no_input))
        contact_no_input_locator.send_keys("9876543210")

        # alternative no.
        alternative_no_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.alternative_no_drop_down))
        actions.move_to_element(alternative_no_drop_down_locator).click().perform()

        pyautogui.FAILSAFE = False
        pyautogui.press('up')
        pyautogui.press('down')

        alternative_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.alternative_input_feild))
        alternative_input_feild_locator.send_keys("123456789")

        # e-mail-id
        email_id_locator = wait.until(
            EC.presence_of_element_located(self.email_id))
        email_id_locator.send_keys("dineshkumar.pentakota@gmail.com")

        # alternative email-id
        alternative_email_id_locator = wait.until(
            EC.presence_of_element_located(self.alternative_email_id))
        alternative_email_id_locator.send_keys("dinesh@kitaab.biz")

        website_locator = wait.until(
            EC.presence_of_element_located(self.website))
        website_locator.send_keys("www.kitaab.biz")

        # social media
        linked_in_locator = wait.until(
            EC.presence_of_element_located(self.linked_in))
        linked_in_locator.send_keys("linkedin.com/company/warehousesolutionsindia")

        facebook_locator = wait.until(
            EC.presence_of_element_located(self.facebook))
        facebook_locator.send_keys("facebook.com/WarehouseLogisticsHub")

        youtube_locator = wait.until(
            EC.presence_of_element_located(self.youtube))
        youtube_locator.send_keys("http://youtube.com/c/FintechSolutionsIndia")

        snap_chat_locator = wait.until(
            EC.presence_of_element_located(self.snap_chat))
        snap_chat_locator.send_keys("twitter.com/AuditGenius")

        Instagram_locator = wait.until(
            EC.presence_of_element_located(self.Instagram))
        Instagram_locator.send_keys("instagram.com/fintech_pros")

    def Address_all_feilds(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        click_on_add_addresses_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_add_addresses))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_add_addresses_locator).click().perform()
