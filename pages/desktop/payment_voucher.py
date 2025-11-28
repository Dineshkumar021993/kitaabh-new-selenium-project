from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
import pyautogui
from datetime import datetime
import pyautogui
import time
import allure


def highlight_element(driver, element):
    """Highlights a Selenium WebDriver element."""
    driver.execute_script("arguments[0].style.border='2px solid magenta'", element)
    time.sleep(1)
    driver.execute_script("arguments[0].style.border=''; arguments[0].style.backgroundColor='';", element)


class PaymentVoucher:
    def __init__(self, driver):
        self.driver = driver
        self.click_on_create_button = (By.XPATH, '//i[@class="fi fi-br-plus l-h-1 v-align-middle font-size-12"]')
        self.click_on_accounting_vouchers = (By.XPATH, '//div[normalize-space(text())="Accounting Transactions"]')
        self.click_on_payments = (By.XPATH, '//div[normalize-space(text())="Payments"]')
        self.create_payment_drop_down_default_value = (By.XPATH, '//*[@id="VCHC0"]')
        self.click_on_create_payment_drop_down = (By.XPATH, '(//i[@class="fi fi-ss-angle-small-down font-size-18"])[1]')
        self.create_payment_list = (By.XPATH, '//*[normalize-space(text())="Payment"]//ancestor::ul//div')
        self.click_on_kitaab_image = (
            By.XPATH,
            '//*[@class="c-sidebar-brand-full mobile-logo-width img-fluid inside-logo-full normal-theme-logo"]')
        self.click_on_yes_button = (By.XPATH, '//button[@id="ACCEP"]')
        self.click_on_currency_in_kitaab_list = (By.XPATH,'//*[normalize-space(text())="Currency"]')
        self.click_on_transaction_type_in_kitaab_list = (By.XPATH, '//*[normalize-space(text())="Transaction Type"]')
        self.transcation_list_in_kitaab = (
            By.XPATH,
            '//*[normalize-space(text())="Voucher Name"]//ancestor::thead//following-sibling::tbody//td[1]//p')
        self.click_on_next_page = (By.XPATH, '//span[@class="p-paginator-icon pi pi-angle-right"]')
        self.search_input_feild = (By.XPATH,'//*[@class="p-inputtext p-component form-control h-40px shadow-none filter-search-inp figma-bg"]')
        self.click_on_edit = (By.XPATH,'//*[normalize-space(text())="Edit"]')
        self.delete_saved_voucher_type_in_list = (By.XPATH,'//*[@class="fi fi-rs-trash"]')
        self.yes_for_confirmation_of_delete = (By.ID,'B2')
        self.name_feild_in_edit = (By.XPATH,'//*[@id="voucherType_name"]')
        self.click_on_elipses = (By.XPATH,'//*[@class="fi fi-br-menu-dots-vertical"]')
        self.click_on_edit1 = (By.ID,'CardMenu_EDIT_0')
        self.method_of_transcation_vouchering = (By.ID,"VN-details-methodOfVoucherNumbering")
        self.click_on_series = (By.ID,'VoucherNumberingAddTab_1')
        self.starting_no_in_series = (By.XPATH,'//*[@id="VN-numberings_0_1"]')
        self.click_on_prefix = (By.ID,'VoucherNumberingAddTab_2')
        self.applicable_from_input_feild_in_prefix = (By.ID,'VN-prefixes_0_0')
        self.click_on_add_button_in_prefix = (By.ID,'VN-prefixes_add')
        self.prefix_input = (By.ID,'VN-prefixes_0_1')
        self.click_on_suffix = (By.ID,'VoucherNumberingAddTab_3')
        self.click_on_add_record_in_suffix = (By.ID,'VN-suffixes_add')
        self.applicable_from_input_feild_in_suffix = (By.ID,'VN-suffixes_0_0')
        self.suffix_input_feild = (By.ID,'VN-suffixes_0_1')
        self.voucher_feild_in_payment_voucher_main_page = (By.NAME,'voucherNo')
        self.check_single = (By.ID,'VCHCSINGLE')
        self.create_input_feild = (By.ID,'VCHC0')
        self.create_button_redirection = (By.ID,'createNewBtn')
        self.name_feild_in_new_redirected = (By.ID,'voucherType_name')
        self.name_feild_in_new = (By.ID,'voucherType_name')
        self.type_of_transcation_in_new = (By.ID,'voucherType_voucherType')
        self.click_on_save = (By.ID,'voucherType_mainSave')
        self.abbrevation_in_new = (By.ID,'voucherType_abbreviation')
        self.click_on_cancel_in_new_redirected_page_voucher_type= (By.ID,'voucherType_mainCancel')
        self.click_on_yes_in_redirected_page_after_click_cancel = (By.ID,'ACCEP')
        self.payment_made_from_ledger_name = (By.XPATH,'(//*[normalize-space(text())="Payment Made From"]//ancestor::div[6]//following-sibling::div)[2]//tr//th[1]')
        # saving in regular or draft
        self.drop_down_for_regular_drop_down = (By.XPATH,'//*[@class="ms-2"]')
        self.default_value_text = (By.XPATH,'//*[@id= "VCHCDD"]//span[1]')
        self.saving_default_list = (By.XPATH,'//button[normalize-space(text())="As Regular"]//parent::ul//button')
        self.exchange_button_element = (By.ID,'EXCHANGEBTN')
        self.voucher_input_feild_inside_exchange = (By.ID,"ex2")
        self.base_input_feild = (By.ID,"ex1")
        self.base_currency_in_voucher_exchnage_rate = (By.XPATH,'(//p[@class="font-size-16 text-color-1 mb-0"])[2]')
        self.input_feild_of_base_currecy_in_voucher_exchange_rate = (By.ID,"ex4")
        self.voucher_currency_in_voucher_exchange_rate = (By.XPATH,'(//p[@class="font-size-16 text-color-1 mb-0"])[1]')
        self.empty_error_msg_for_value_input_feild_in_voucher_exchange_rate = (By.XPATH,'//*[@aria-label="Exchange Rate is a required field"]')
        self.input_feild_of_voucher_currency_in_voucher_exchange_rate = (By.ID,"ex3")
        self.list_of_voucher_cuureency = (By.XPATH,'//div[normalize-space(text())="asddbg - $!$!@"]//ancestor::ul//div')
        self.voucher_type_drop_down_click = (By.XPATH,'(//*[@class="fi fi-ss-angle-small-down font-size-18"])[4]')
        self.create_new_in_voucher_currency = (By.ID,'createNewBtn')
        self.click_on_add_new_symbol_in_symbol_drop_down = (By.XPATH,'//div[normalize-space(text())="Add New Symbol"]')
        self.create_currency_drop_down_click = (By.XPATH,'(//*[@class="fi fi-ss-angle-small-down font-size-18"])[1]')
        self.click_on_dollar = (By.XPATH,'//div[normalize-space(text())="Dollar - $"]')
        self.formal_name_in_create_currency = (By.ID,'CR2')
        self.iso_currency = (By.ID,'CR3')
        self.word_representing_in = (By.ID,'CR8')
        self.save_button = (By.ID,'CR10')
        self.currency_symbol_input_feild = (By.ID,'CR1')
        self.exchange_button_element1= (By.ID,'ex5')
        self.search_feild_in_currency = (By.XPATH,'//input[@class="p-inputtext p-component form-control h-40px shadow-none filter-search-inp figma-bg"]')
        self.click_on_delete_in_currency_list = (By.XPATH,'//p[normalize-space(text())="wow pratice"]//parent::td//following-sibling::td[3]//button[2]//i')
        self.mouse_hover_to_wow_pratice = (By.XPATH,'//*[normalize-space(text())="wow pratice"]')
        self.transcation_date_in_main_page = (By.ID,'VCHC1')
        self.transcation_date_tool_tip = (By.XPATH,'//*[normalize-space(text())="Transaction Date ( F2 )"]')
        self.transcation_no_tool_tip = (By.XPATH, '//*[normalize-space(text())="Transaction Number"]')
        self.error_msg_for_wrong_input_validation_in_transcation_date = (By.XPATH,'//*[@aria-label="Please enter valid date"]')
        self.error_msg_for_date_prior_in_transcation_date = (By.XPATH,'//*[@class="fi fi-br-info font-size-14"]')
        self.empty_transcation_date  = (By.XPATH,'//*[@aria-label="Voucher date is required"]')
        self.transcation_no_element = (By.NAME,'voucherNo')
        self.empty_error_msg_for_transcation_no = (By.XPATH,'//*[@aria-label="This field is mandatory"]')
        self.error_msg_in_transcation_date_more_than_16 = (By.XPATH,'//*[@aria-label="Voucher Number Exceeds 16 characters"]')
        self.click_on_refresh = (By.XPATH,'//*[@class="fi fi-bs-refresh"]')
        self.gst_in_no = (By.XPATH,'(//*[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-primary"])[2]')
        self.first_text_in_gst = (By.XPATH,'//div[@class="option-name overflow-elipsis"]')
        self.second_text_in_gst = (By.XPATH,'//div[@class="option-value"]')
        self.mouse_hover_in_gst_in = (By.XPATH,'//*[normalize-space(text())="27AHTPT7639N2Z0"]')

    def Click_on_payment_voucher(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_create_button_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_create_button))
        highlight_element(self.driver, click_on_create_button_locator)
        self.driver.execute_script("arguments[0].click();", click_on_create_button_locator)

        # click on accounting vouchers and sales
        click_on_accounting_vouchers_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_accounting_vouchers))
        highlight_element(self.driver, click_on_accounting_vouchers_locator)
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnAccountingVouchers",
                      attachment_type=allure.attachment_type.PNG)
        click_on_accounting_vouchers_locator.click()
        time.sleep(2)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_payment_voucher_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_payments))
        highlight_element(self.driver, click_on_payment_voucher_locator)
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnSalesVoucher",
                      attachment_type=allure.attachment_type.PNG)
        click_on_payment_voucher_locator.click()
        time.sleep(2)
        return click_on_create_button_locator,click_on_accounting_vouchers_locator,click_on_payment_voucher_locator

    def create_payment(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        create_payment_drop_down_default_value_locator = wait.until(
            EC.element_to_be_clickable(self.create_payment_drop_down_default_value))
        highlight_element(self.driver, create_payment_drop_down_default_value_locator)
        Attribute_value_of_create_payment = create_payment_drop_down_default_value_locator.get_attribute("value")
        print(f"Attribute_value_of_create_payment:", Attribute_value_of_create_payment)

        # click on payment drop down
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_create_payment_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_create_payment_drop_down))
        highlight_element(self.driver, click_on_create_payment_drop_down_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_create_payment_drop_down_locator).click().perform()
        time.sleep(3)

        # create payment list
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        create_payment_list_locator = wait.until(
            EC.presence_of_all_elements_located(self.create_payment_list))
        Element_list = [element.text for element in create_payment_list_locator]
        print("Element_list_in_kitaab_page:",Element_list)
        print(len(Element_list))

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_kitaab_image_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_kitaab_image))
        highlight_element(self.driver, click_on_kitaab_image_locator)
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnKitaabImage",
                      attachment_type=allure.attachment_type.PNG)
        click_on_kitaab_image_locator.click()
        time.sleep(2)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_yes_button_locator = wait.until(
            EC.presence_of_element_located(self.click_on_yes_button))
        highlight_element(self.driver, click_on_yes_button_locator)
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnYesButton",
                      attachment_type=allure.attachment_type.PNG)
        actions.move_to_element(click_on_yes_button_locator).click().perform()
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_transaction_type_in_kitaab_list_locator = wait.until(
            EC.presence_of_element_located(self.click_on_transaction_type_in_kitaab_list))
        highlight_element(self.driver, click_on_transaction_type_in_kitaab_list_locator)
        click_on_transaction_type_in_kitaab_list_locator.click()
        # search feild
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        search_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.search_input_feild))
        search_input_feild_locator.send_keys("payment")
        time.sleep(3)

        list_values = []
        for j in range(6):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_next_page_locator = wait.until(
                EC.presence_of_element_located(self.click_on_next_page))
            actions.move_to_element(click_on_next_page_locator).click().perform()

            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            transcation_list_in_kitaab_locator = wait.until(
                EC.presence_of_all_elements_located(self.transcation_list_in_kitaab))
            for i in transcation_list_in_kitaab_locator:
                element_text = i.text
                list_values.append(element_text)
        print("List_values_in_kitaab_main_page:", list_values)
        print(len(list_values))

        Equal_elements = []
        Unequal_elements = []
        for i in Element_list:
            if any(item in Element_list for item in list_values):
                Equal_elements.append(i)
            else:
                Unequal_elements.append(i)
        print("Equal_elements:", Equal_elements)
        print(len(Equal_elements))
        print("UnEqual_elements:", Unequal_elements)

    def payment_number_series_click(self):
        global element_text3
        self.Click_on_payment_voucher()
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_create_payment_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_create_payment_drop_down))
        highlight_element(self.driver, click_on_create_payment_drop_down_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_create_payment_drop_down_locator).click().perform()
        time.sleep(3)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        create_payment_list_locator = wait.until(
            EC.presence_of_all_elements_located(self.create_payment_list))
        Element_list = [element.text for element in create_payment_list_locator]
        length_of_element_list = len(Element_list)
        for i in range(length_of_element_list):
            if i == 1:
                break
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            create_payment_list_locator = wait.until(
                EC.presence_of_all_elements_located(self.create_payment_list))
            element2 = create_payment_list_locator[i]
            element_text = element2.text
            actions = ActionChains(self.driver)
            actions.move_to_element(element2).perform()
            actions.move_to_element(element2).click().perform()
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_kitaab_image_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_kitaab_image))
            highlight_element(self.driver, click_on_kitaab_image_locator)
            allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnKitaabImage",
                          attachment_type=allure.attachment_type.PNG)
            click_on_kitaab_image_locator.click()
            time.sleep(2)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_yes_button_locator = wait.until(
                EC.presence_of_element_located(self.click_on_yes_button))
            highlight_element(self.driver, click_on_yes_button_locator)
            allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnYesButton",
                          attachment_type=allure.attachment_type.PNG)
            actions.move_to_element(click_on_yes_button_locator).click().perform()

            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_transaction_type_in_kitaab_list_locator = wait.until(
                EC.presence_of_element_located(self.click_on_transaction_type_in_kitaab_list))
            highlight_element(self.driver, click_on_transaction_type_in_kitaab_list_locator)
            actions.move_to_element(click_on_transaction_type_in_kitaab_list_locator).click().perform()

            # search feild
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            search_input_feild_locator = wait.until(
                EC.presence_of_element_located(self.search_input_feild))
            search_input_feild_locator.send_keys(element_text)
            time.sleep(2)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            transcation_list_in_kitaab_locator = wait.until(
                EC.presence_of_all_elements_located(self.transcation_list_in_kitaab))
            Element_list = [element.text for element in transcation_list_in_kitaab_locator]
            length_of_element_list2 = len(Element_list)
            for j in range(length_of_element_list2):
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                transcation_list_in_kitaab_locator = wait.until(
                    EC.presence_of_all_elements_located(self.transcation_list_in_kitaab))
                element3 = transcation_list_in_kitaab_locator[j]
                element_text3 = element3.text
                print(element_text3)
                if element_text3 == element_text:
                    actions.move_to_element(element3).click().perform()
                else:
                    print(f"Both {element_text3} and {element_text} are not equal")
            time.sleep(2)
            # click on edit
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_edit_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_edit))
            actions.move_to_element(click_on_edit_locator).click().perform()
            # name feild in edit
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            name_feild_in_edit_locator = wait.until(
                EC.presence_of_element_located(self.name_feild_in_edit))
            Attribute_value_of_name_feild = name_feild_in_edit_locator.get_attribute("value")
            if Attribute_value_of_name_feild == element_text3:
                print(f"Both {Attribute_value_of_name_feild} and element_text3 are equal")
            else:
                print(f"Both {Attribute_value_of_name_feild} and element_text3 are not equal")

            pyautogui.hotkey('alt', 't')
            time.sleep(2)
            # click on elipses
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_elipses = wait.until(
                EC.element_to_be_clickable(self.click_on_elipses))
            actions.move_to_element(click_on_elipses).click().perform()
            time.sleep(2)
            # click on edit
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_edit1_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_edit1))
            actions.move_to_element(click_on_edit1_locator).click().perform()
            time.sleep(1)
            # pyautogui.press("down")
            # pyautogui.press("up")
            # pyautogui.press("enter")
            # method of voucher numering default value
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            method_of_transcation_vouchering_locator = wait.until(
                EC.presence_of_element_located(self.method_of_transcation_vouchering))
            Attribute_value_voucher_number = method_of_transcation_vouchering_locator.get_attribute("value")
            if Attribute_value_voucher_number == "Automatic (Manual Override)":
                # click on series
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_series_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_series))
                actions.move_to_element(click_on_series_locator).click().perform()
                time.sleep(2)
                # wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                # starting_no_in_series_locator = wait.until(
                #     EC.presence_of_element_located(self.starting_no_in_series))
                # starting_no_in_series_locator.send_keys("1")
                # click on prefix
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_prefix_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_prefix))
                actions.move_to_element(click_on_prefix_locator).click().perform()
                time.sleep(2)
                # click on add details in prefix
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_add_button_in_prefix_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_add_button_in_prefix))
                actions.move_to_element(click_on_add_button_in_prefix_locator).click().perform()
                time.sleep(2)
                # applicable from input
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                applicable_from_input_feild_in_prefix_locator = wait.until(
                    EC.presence_of_element_located(self.applicable_from_input_feild_in_prefix))
                applicable_from_input_feild_in_prefix_locator.send_keys("10/12/2024")
                time.sleep(2)
                # prefix_input
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                prefix_input_locator = wait.until(
                    EC.presence_of_element_located(self.prefix_input))
                prefix_input_locator.send_keys("pratice")
                time.sleep(2)
                # click on suffix
                click_on_suffix_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_suffix))
                actions.move_to_element(click_on_suffix_locator).click().perform()
                time.sleep(2)
                # click add record in suffix
                click_on_add_record_in_suffix_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_add_record_in_suffix))
                actions.move_to_element(click_on_add_record_in_suffix_locator).click().perform()
                time.sleep(2)
                # applicable from in suffix
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                applicable_from_input_feild_in_suffix_locator = wait.until(
                    EC.presence_of_element_located(self.applicable_from_input_feild_in_suffix))
                applicable_from_input_feild_in_suffix_locator.send_keys("10/12/2024")
                time.sleep(2)
                # suffix input feild
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                suffix_input_feild_locator = wait.until(
                    EC.presence_of_element_located(self.suffix_input_feild))
                suffix_input_feild_locator.send_keys("best")
                time.sleep(2)
                for _ in range(3):
                    actions.send_keys(Keys.ESCAPE).perform()
                    time.sleep(1)
                time.sleep(4)
                click_on_create_payment_drop_down_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_create_payment_drop_down))
                highlight_element(self.driver, click_on_create_payment_drop_down_locator)
                actions = ActionChains(self.driver)
                actions.move_to_element(click_on_create_payment_drop_down_locator).click().perform()
                time.sleep(2)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                create_payment_list_locator = wait.until(
                    EC.presence_of_all_elements_located(self.create_payment_list))
                element2 = create_payment_list_locator[i]
                actions.move_to_element(element2).click().perform()
                time.sleep(1)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                voucher_feild_in_payment_voucher_main_page_locator = wait.until(
                    EC.presence_of_element_located(self.voucher_feild_in_payment_voucher_main_page))
                Attribute_value_of_voucher_input_feild = voucher_feild_in_payment_voucher_main_page_locator.get_attribute(
                    "value")
                print(Attribute_value_of_voucher_input_feild)
                # Attribute_value_voucher_number = method_of_transcation_vouchering_locator.get_attribute("value")
            elif Attribute_value_voucher_number == "Automatic":
                # click on series
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_series_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_series))
                actions.move_to_element(click_on_series_locator).click().perform()
                time.sleep(2)
                # wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                # starting_no_in_series_locator = wait.until(
                #     EC.presence_of_element_located(self.starting_no_in_series))
                # starting_no_in_series_locator.send_keys("1")
                # click on prefix
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_prefix_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_prefix))
                actions.move_to_element(click_on_prefix_locator).click().perform()
                time.sleep(2)
                # click on add details in prefix
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_add_button_in_prefix_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_add_button_in_prefix))
                actions.move_to_element(click_on_add_button_in_prefix_locator).click().perform()
                time.sleep(2)
                # applicable from input
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                applicable_from_input_feild_in_prefix_locator = wait.until(
                    EC.presence_of_element_located(self.applicable_from_input_feild_in_prefix))
                applicable_from_input_feild_in_prefix_locator.send_keys("10/12/2024")
                time.sleep(2)
                # prefix_input
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                prefix_input_locator = wait.until(
                    EC.presence_of_element_located(self.prefix_input))
                prefix_input_locator.send_keys("pratice")
                time.sleep(2)
                # click on suffix
                click_on_suffix_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_suffix))
                actions.move_to_element(click_on_suffix_locator).click().perform()
                time.sleep(2)
                # click add record in suffix
                click_on_add_record_in_suffix_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_add_record_in_suffix))
                actions.move_to_element(click_on_add_record_in_suffix_locator).click().perform()
                time.sleep(2)
                # applicable from in suffix
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                applicable_from_input_feild_in_suffix_locator = wait.until(
                    EC.presence_of_element_located(self.applicable_from_input_feild_in_suffix))
                applicable_from_input_feild_in_suffix_locator.send_keys("10/12/2024")
                time.sleep(2)
                # suffix input feild
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                suffix_input_feild_locator = wait.until(
                    EC.presence_of_element_located(self.suffix_input_feild))
                suffix_input_feild_locator.send_keys("best")
                time.sleep(2)
                for _ in range(3):
                    actions.send_keys(Keys.ESCAPE).perform()
                    time.sleep(1)
                time.sleep(4)
                click_on_create_payment_drop_down_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_create_payment_drop_down))
                highlight_element(self.driver, click_on_create_payment_drop_down_locator)
                actions = ActionChains(self.driver)
                actions.move_to_element(click_on_create_payment_drop_down_locator).click().perform()
                time.sleep(2)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                create_payment_list_locator = wait.until(
                    EC.presence_of_all_elements_located(self.create_payment_list))
                element2 = create_payment_list_locator[i]
                actions.move_to_element(element2).click().perform()
                time.sleep(1)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                voucher_feild_in_payment_voucher_main_page_locator = wait.until(
                    EC.presence_of_element_located(self.voucher_feild_in_payment_voucher_main_page))
                Attribute_value_of_voucher_input_feild = voucher_feild_in_payment_voucher_main_page_locator.get_attribute(
                    "value")
                print(Attribute_value_of_voucher_input_feild)
                # Attribute_value_voucher_number = method_of_transcation_vouchering_locator.get_attribute("value")
            elif Attribute_value_voucher_number == "Manual":
                for _ in range(3):
                    actions.send_keys(Keys.ESCAPE).perform()
                    time.sleep(1)
                time.sleep(4)
                click_on_create_payment_drop_down_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_create_payment_drop_down))
                highlight_element(self.driver, click_on_create_payment_drop_down_locator)
                actions = ActionChains(self.driver)
                actions.move_to_element(click_on_create_payment_drop_down_locator).click().perform()
                time.sleep(2)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                create_payment_list_locator = wait.until(
                    EC.presence_of_all_elements_located(self.create_payment_list))
                element2 = create_payment_list_locator[i]
                actions.move_to_element(element2).click().perform()
                time.sleep(1)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                voucher_feild_in_payment_voucher_main_page_locator = wait.until(
                    EC.presence_of_element_located(self.voucher_feild_in_payment_voucher_main_page))
                Attribute_value_of_voucher_input_feild = voucher_feild_in_payment_voucher_main_page_locator.get_attribute(
                    "value")
                print(Attribute_value_of_voucher_input_feild)

            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_create_payment_drop_down_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_create_payment_drop_down))
            highlight_element(self.driver, click_on_create_payment_drop_down_locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_create_payment_drop_down_locator).click().perform()

    def create_button_in_create_payment(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_create_payment_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_create_payment_drop_down))
        highlight_element(self.driver, click_on_create_payment_drop_down_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_create_payment_drop_down_locator).click().perform()


        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        create_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.create_input_feild))
        create_input_feild_locator.send_keys(" pratice voucher type")
        time.sleep(2)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        create_button_redirection_locator = wait.until(
            EC.element_to_be_clickable(self.create_button_redirection))
        highlight_element(self.driver, create_button_redirection_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(create_button_redirection_locator).click().perform()
        time.sleep(2)

        # voucher type selection
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        type_of_transcation_in_new_locator = wait.until(
            EC.presence_of_element_located(self.type_of_transcation_in_new))
        type_of_transcation_in_new_locator.send_keys("Payment")

        # abbrevation
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        abbrevation_in_new_locator = wait.until(
            EC.presence_of_element_located(self.abbrevation_in_new))
        abbrevation_in_new_locator.send_keys("paypravouty")
        return create_input_feild_locator

    def save_new_voucher_type(self):
        # click on save
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_save_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_save))
        highlight_element(self.driver, click_on_save_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_save_locator).click().perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        create_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.create_input_feild))
        Attribute_value = create_input_feild_locator.get_attribute("value")
        Expected_text = "Payment pratice voucher type"
        if Attribute_value == Attribute_value:
            print(f"Both {Attribute_value} and {Expected_text} are equal")
        else:
            print(f"Both {Attribute_value} and {Expected_text} are  not equal")

    def delete_saved_voucher_type(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_kitaab_image_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_kitaab_image))
        highlight_element(self.driver, click_on_kitaab_image_locator)
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnKitaabImage",
                      attachment_type=allure.attachment_type.PNG)
        click_on_kitaab_image_locator.click()
        time.sleep(2)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_yes_button_locator = wait.until(
            EC.presence_of_element_located(self.click_on_yes_button))
        highlight_element(self.driver, click_on_yes_button_locator)
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnYesButton",
                      attachment_type=allure.attachment_type.PNG)
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_yes_button_locator).click().perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_transaction_type_in_kitaab_list_locator = wait.until(
            EC.presence_of_element_located(self.click_on_transaction_type_in_kitaab_list))
        highlight_element(self.driver, click_on_transaction_type_in_kitaab_list_locator)
        actions.move_to_element(click_on_transaction_type_in_kitaab_list_locator).click().perform()
        time.sleep(0.5)
        # pyautogui.hotkey("ctrl", 'r')
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        search_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.search_input_feild))
        search_input_feild_locator.send_keys("Payment pratice voucher type")
        time.sleep(1)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        delete_saved_voucher_type_in_list_locator = wait.until(
            EC.presence_of_element_located(self.delete_saved_voucher_type_in_list))
        highlight_element(self.driver, delete_saved_voucher_type_in_list_locator)
        actions.move_to_element(delete_saved_voucher_type_in_list_locator).click().perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        yes_for_confirmation_of_delete_locator = wait.until(
            EC.presence_of_element_located(self.yes_for_confirmation_of_delete))
        highlight_element(self.driver, yes_for_confirmation_of_delete_locator)
        actions.move_to_element(yes_for_confirmation_of_delete_locator).click().perform()

    def check_cancel_button_in_new_derict_page(self):
        self.Click_on_payment_voucher()
        self.create_button_in_create_payment()
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_cancel_in_new_redirected_page_voucher_type_locator = wait.until(
            EC.presence_of_element_located(self.click_on_cancel_in_new_redirected_page_voucher_type))
        highlight_element(self.driver, click_on_cancel_in_new_redirected_page_voucher_type_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_cancel_in_new_redirected_page_voucher_type_locator).click().perform()
        # click_on_yes_in_redirected_page_after_click_cancel
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_yes_in_redirected_page_after_click_cancel_locator = wait.until(
            EC.presence_of_element_located(self.click_on_yes_in_redirected_page_after_click_cancel))
        highlight_element(self.driver, click_on_yes_in_redirected_page_after_click_cancel_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_yes_in_redirected_page_after_click_cancel_locator).click().perform()


    def saving_in_regular_mode(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        default_value_text_locator = wait.until(
            EC.presence_of_element_located(self.default_value_text))
        text = default_value_text_locator.text
        Expected_text = "Saving in Regular"
        if text == Expected_text:
            print(f"Both {text} and {Expected_text} are equal")
        else:
            print(f"Both {text} and {Expected_text} are not equal")
        time.sleep(2)
        # default_value_text_locator.click()
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        drop_down_for_regular_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.drop_down_for_regular_drop_down))
        actions = ActionChains(self.driver)
        actions.move_to_element(drop_down_for_regular_drop_down_locator).click().perform()
        time.sleep(2)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(2)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(2)
        text1 = default_value_text_locator.text
        Expected_text2 = "Saving in Draft"
        if text1 == Expected_text2:
            print(text1)
            print(f"Both {text1} and {Expected_text2} are equal")
        else:
            print(f"Both {text1} and {Expected_text2} are not equal")
        time.sleep(1)
        actions.send_keys(Keys.BACKSPACE).perform()
        time.sleep(1)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(0.5)
        actions.send_keys(Keys.ARROW_UP).perform()
        time.sleep(0.5)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(1)

    def exchange_button(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        exchange_button_element_locator = wait.until(
            EC.presence_of_element_located(self.exchange_button_element))
        actions = ActionChains(self.driver)
        actions.move_to_element(exchange_button_element_locator).click().perform()
        time.sleep(2)
        # base currency
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        base_input_feild_locator = wait.until(
            EC.visibility_of_element_located(self.base_input_feild))
        if base_input_feild_locator.is_enabled():
            print(f"defauty it is enabled state")
        else:
            print(f"defauty it is disabled state")
        Attribute_value = base_input_feild_locator.get_attribute("value")
        print(f"Even though it is disable state the default value is:", Attribute_value)
        # base currency in voucher exchange rate
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        base_currency_in_voucher_exchnage_rate_locator = wait.until(
            EC.presence_of_element_located(self.base_currency_in_voucher_exchnage_rate))
        text = base_currency_in_voucher_exchnage_rate_locator.text
        if text == Attribute_value:
            print(f"Both base currency and 'Base currency' in voucher exchange rate are equal")
        else:
            print(f"Both base currency and 'Base currency' in voucher exchange rate are not equal")

        # input_feild_of_base_currecy_in_voucher_exchange_rate
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        input_feild_of_base_currecy_in_voucher_exchange_rate_locator = wait.until(
            EC.presence_of_element_located(self.input_feild_of_base_currecy_in_voucher_exchange_rate))
        if input_feild_of_base_currecy_in_voucher_exchange_rate_locator.is_enabled():
            print(f"defaulty it is in enabled state")
        else:
            Attribute_value1 = input_feild_of_base_currecy_in_voucher_exchange_rate_locator.get_attribute("value")
            Expected_value = "1"
            if Attribute_value1 == Expected_value:
                print(f"both {Attribute_value1} and {Expected_value} are equal")
            else:
                print(f"both {Attribute_value1} and {Expected_value} are not equal")

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        exchange_button_element_locator = wait.until(
            EC.presence_of_element_located(self.voucher_input_feild_inside_exchange))
        Attribute_value_voucher_input_feild = exchange_button_element_locator.get_attribute("value")
        print(Attribute_value_voucher_input_feild)
        # voucher currency in voucher exchange rate
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        voucher_currency_in_voucher_exchange_rate_locator = wait.until(
            EC.presence_of_element_located(self.voucher_currency_in_voucher_exchange_rate))
        Attribute_value_voucher_currency_in_voucher_exchange_rate = (voucher_currency_in_voucher_exchange_rate_locator
                                                                     .get_attribute("value"))
        if Attribute_value_voucher_input_feild == Attribute_value_voucher_currency_in_voucher_exchange_rate:
            print(f"Both {Attribute_value_voucher_input_feild} and "
                  f"{Attribute_value_voucher_currency_in_voucher_exchange_rate} are equal")
        else:
            print(
                f"Both {Attribute_value_voucher_input_feild} and "
                f"{Attribute_value_voucher_currency_in_voucher_exchange_rate} are not equal")

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        input_feild_of_voucher_currency_in_voucher_exchange_rate_locator = wait.until(
            EC.presence_of_element_located(self.input_feild_of_voucher_currency_in_voucher_exchange_rate))

        if input_feild_of_voucher_currency_in_voucher_exchange_rate_locator.is_enabled():
            print(f"defaulty it is in enabled state")
        else:
            Attribute_value2 = input_feild_of_voucher_currency_in_voucher_exchange_rate_locator.get_attribute("value")
            Expected_value = "1"
            if Attribute_value2 == Expected_value:
                print(f"both {Attribute_value2} and {Expected_value} are equal")
            else:
                print(f"both {Attribute_value2} and {Expected_value} are not  equal")

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()

        # list
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        list_of_voucher_cuureency_lists = wait.until(
            EC.presence_of_all_elements_located(self.list_of_voucher_cuureency))
        Element_list = [element.text for element in list_of_voucher_cuureency_lists]
        length = len(Element_list)
        for i in range(length):
            if i == 3:
                break
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            list_of_voucher_cuureency_lists = wait.until(
                EC.presence_of_all_elements_located(self.list_of_voucher_cuureency))
            element = list_of_voucher_cuureency_lists[i]
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            time.sleep(0.5)
            actions.move_to_element(element).click().perform()
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            input_feild_of_base_currecy_in_voucher_exchange_rate_lists = wait.until(
                EC.presence_of_element_located(self.input_feild_of_base_currecy_in_voucher_exchange_rate))
            input_feild_of_base_currecy_in_voucher_exchange_rate_lists.send_keys("1")
            time.sleep(1)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            voucher_currency_in_voucher_exchange_rate_locator = wait.until(
                EC.presence_of_element_located(self.voucher_currency_in_voucher_exchange_rate))
            text_voucher_currency_in_voucher_exchange_rate_locator = voucher_currency_in_voucher_exchange_rate_locator.text

            time.sleep(1)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            exchange_button_element_locator = wait.until(
                EC.presence_of_element_located(self.voucher_input_feild_inside_exchange))
            Attribute_value_voucher_input_feild = exchange_button_element_locator.get_attribute("value")

            time.sleep(1)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(3)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            exchange_button_element_locator = wait.until(
                EC.presence_of_element_located(self.exchange_button_element))
            text_exchange_button_element_locator = exchange_button_element_locator.text
            time.sleep(1)

            if text_voucher_currency_in_voucher_exchange_rate_locator == Attribute_value_voucher_input_feild == text_exchange_button_element_locator:
                print(f"All '{text_voucher_currency_in_voucher_exchange_rate_locator}' = '{Attribute_value_voucher_input_feild}'= '{text_exchange_button_element_locator}'  are equal")
            else:
                print(f"All '{text_voucher_currency_in_voucher_exchange_rate_locator}' = '{Attribute_value_voucher_input_feild}'= '{text_exchange_button_element_locator}'  are not equal")
            time.sleep(1)
            actions.move_to_element(exchange_button_element_locator).click().perform()
            time.sleep(1)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            voucher_type_drop_down_click_locator = wait.until(
                EC.element_to_be_clickable(self.voucher_type_drop_down_click))
            actions.move_to_element(voucher_type_drop_down_click_locator).click().perform()
            time.sleep(1)

    def voucher_currency_list_create(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        voucher_input_feild_inside_exchange_locator = wait.until(
            EC.presence_of_element_located(self.voucher_input_feild_inside_exchange))
        Attribute_value = voucher_input_feild_inside_exchange_locator.get_attribute("value")
        for _ in Attribute_value:
            voucher_input_feild_inside_exchange_locator.send_keys(Keys.BACKSPACE)
        voucher_input_feild_inside_exchange_locator.send_keys("dummy pratice currency")
        # create button
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        create_new_in_voucher_currency_locator = wait.until(
            EC.element_to_be_clickable(self.create_new_in_voucher_currency))
        actions = ActionChains(self.driver)
        actions.move_to_element(create_new_in_voucher_currency_locator).click().perform()
        time.sleep(1)
        # create new currency symbol
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        currency_symbol_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.currency_symbol_input_feild))
        Attribute_value3 = currency_symbol_input_feild_locator.get_attribute("value")
        for _ in Attribute_value3:
            currency_symbol_input_feild_locator.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        create_currency_drop_down_click_locator = wait.until(
            EC.element_to_be_clickable(self.create_currency_drop_down_click))
        actions.move_to_element(create_currency_drop_down_click_locator).click().perform()
        time.sleep(1)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_add_new_symbol_in_symbol_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_add_new_symbol_in_symbol_drop_down))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_add_new_symbol_in_symbol_drop_down_locator).click().perform()
        time.sleep(1)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        currency_symbol_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.currency_symbol_input_feild))
        currency_symbol_input_feild_locator.send_keys("wow!")

        # formal name in create currency
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        formal_name_in_create_currency = wait.until(
            EC.presence_of_element_located(self.formal_name_in_create_currency))
        Attribute_value1 = formal_name_in_create_currency.get_attribute("value")
        for _ in Attribute_value1:
            formal_name_in_create_currency.send_keys(Keys.BACKSPACE)
        formal_name_in_create_currency.send_keys("wow pratice")
        Attribute_value3 = formal_name_in_create_currency.get_attribute("value")
        # iso name
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        iso_currency_locator = wait.until(
            EC.presence_of_element_located(self.iso_currency))
        Attribute_value2 = iso_currency_locator.get_attribute("value")
        for _ in Attribute_value2:
            iso_currency_locator.send_keys(Keys.BACKSPACE)
        iso_currency_locator.send_keys("wow")
        # word representing
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        word_representing_in_locator = wait.until(
            EC.presence_of_element_located(self.word_representing_in))
        word_representing_in_locator.send_keys("dummy")
        # save
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        save_button_locator = wait.until(
            EC.element_to_be_clickable(self.save_button))
        actions.move_to_element(save_button_locator).click().perform()
        time.sleep(6)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        voucher_input_feild_inside_exchange_locator = wait.until(
            EC.presence_of_element_located(self.voucher_input_feild_inside_exchange))
        Attribute_value_of_voucher_input_feild = voucher_input_feild_inside_exchange_locator.get_attribute("value")

        if Attribute_value3 == Attribute_value_of_voucher_input_feild:
            print(f"both {Attribute_value3} and {Attribute_value_of_voucher_input_feild} are equal")
        else:
            print(f"both {Attribute_value3} and {Attribute_value_of_voucher_input_feild} are not equal")

    def switch_locator(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        voucher_type_drop_down_click_locator = wait.until(
            EC.element_to_be_clickable(self.voucher_type_drop_down_click))
        actions = ActionChains(self.driver)
        actions.move_to_element(voucher_type_drop_down_click_locator).click().perform()

        # click on dollar
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_dollar_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_dollar))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_dollar_locator).click().perform()
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=3)
            exchange_button_locator = wait.until(
                EC.visibility_of_element_located(self.exchange_button_element1))
            if exchange_button_locator.is_displayed():
                print("displayed")
        except TimeoutException:
            pass
        print("Exchange button not displayed")

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        voucher_type_drop_down_click_locator = wait.until(
            EC.element_to_be_clickable(self.voucher_type_drop_down_click))
        actions = ActionChains(self.driver)
        actions.move_to_element(voucher_type_drop_down_click_locator).click().perform()
        time.sleep(0.5)
        actions.send_keys(Keys.ARROW_UP).perform()
        time.sleep(0.5)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(0.5)
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=3)
            exchange_button_locator = wait.until(
                EC.visibility_of_element_located(self.exchange_button_element1))
            if exchange_button_locator.is_displayed():
                print("Exchange button displayed")
            else:
                print("Exchange button not displayed")
        except TimeoutException:
            pass

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        base_currency_in_voucher_exchnage_rate_locator = wait.until(
            EC.presence_of_element_located(self.base_currency_in_voucher_exchnage_rate))
        text = base_currency_in_voucher_exchnage_rate_locator.text
        print(text)
        Expected_text = "Dollar - $"
        if text == Expected_text:
            print(f"both {text} and {Expected_text} are equal and it is exchange button not clicked")
        else:
            print("both are not equal")

        wait = WebDriverWait(self.driver, 10, poll_frequency=3)
        exchange_button_locator = wait.until(
            EC.element_to_be_clickable(self.exchange_button_element1))
        actions.move_to_element(exchange_button_locator).click().perform()
        time.sleep(3)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        voucher_currency_in_voucher_exchange_rate_locator = wait.until(
            EC.presence_of_element_located(self.voucher_currency_in_voucher_exchange_rate))
        text1 = voucher_currency_in_voucher_exchange_rate_locator.text
        print(text1)
        Expected_text = "dftg - !$!"
        if text1 == Expected_text:
            print(f"both {text1} and {Expected_text} are equal and it is exchange button  clicked and switched")
        else:
            print(f"both {text1} and {Expected_text} are not equal and it is exchange button  not clicked and not switched")

        # empty eror for value input feild in voucher exchange rate
        wait = WebDriverWait(self.driver, 40, poll_frequency=3, ignored_exceptions=[Exception])
        empty_error_msg_for_value_input_feild_in_voucher_exchange_rate_locator = wait.until(
            EC.presence_of_element_located(self.empty_error_msg_for_value_input_feild_in_voucher_exchange_rate))

        if empty_error_msg_for_value_input_feild_in_voucher_exchange_rate_locator.is_displayed():
            actions = ActionChains(self.driver)
            actions.move_to_element(empty_error_msg_for_value_input_feild_in_voucher_exchange_rate_locator).perform()
            # Capture the text of the error message
            error_message_text = empty_error_msg_for_value_input_feild_in_voucher_exchange_rate_locator.get_attribute("aria-label")
            # Expected error message
            expected_error_message = "Exchange Rate is a required field"  # Replace with your expected error message
            if error_message_text == expected_error_message:
                print("Validation error message matches the expected error message:", error_message_text)
            else:
                print("Validation error message does not match the expected error message. Actual:",
                      error_message_text)
        else:
            print("validation message in empty Ledger input feild is not displayed")

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        input_feild_of_base_currecy_in_voucher_exchange_rate_locator = wait.until(
            EC.element_to_be_clickable(self.input_feild_of_base_currecy_in_voucher_exchange_rate))
        input_feild_of_base_currecy_in_voucher_exchange_rate_locator.send_keys("10.56789")

        actions.send_keys(Keys.ESCAPE).perform()
        time.sleep(0.5)

        # delete create currency
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_kitaab_image_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_kitaab_image))
        highlight_element(self.driver, click_on_kitaab_image_locator)
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnKitaabImage",
                      attachment_type=allure.attachment_type.PNG)
        actions.move_to_element(click_on_kitaab_image_locator).click().perform()
        time.sleep(2)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_yes_button_locator = wait.until(
            EC.presence_of_element_located(self.click_on_yes_button))
        highlight_element(self.driver, click_on_yes_button_locator)
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnYesButton",
                      attachment_type=allure.attachment_type.PNG)
        actions.move_to_element(click_on_yes_button_locator).click().perform()


        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_currency_in_kitaab_list_locator = wait.until(
            EC.presence_of_element_located(self.click_on_currency_in_kitaab_list))
        highlight_element(self.driver, click_on_currency_in_kitaab_list_locator)
        actions.move_to_element(click_on_currency_in_kitaab_list_locator).click().perform()
        time.sleep(4)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        search_feild_in_currency_locator = wait.until(
            EC.presence_of_element_located(self.search_feild_in_currency))
        search_feild_in_currency_locator.send_keys("wow pratice")
        time.sleep(3)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        mouse_hover_to_wow_pratice_locator = wait.until(
            EC.presence_of_element_located(self.mouse_hover_to_wow_pratice))
        actions.move_to_element(mouse_hover_to_wow_pratice_locator).perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_delete_in_currency_list_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_delete_in_currency_list))
        actions.move_to_element(click_on_delete_in_currency_list_locator).click().perform()
        time.sleep(1)
        self.Click_on_payment_voucher()

    def transcation_date(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcation_date_in_main_page_locator = wait.until(
            EC.presence_of_element_located(self.transcation_date_in_main_page))
        actions = ActionChains(self.driver)
        actions.move_to_element(transcation_date_in_main_page_locator).perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcation_date_tool_tip_locator = wait.until(
            EC.visibility_of_element_located(self.transcation_date_tool_tip))
        text = transcation_date_tool_tip_locator.text
        Expected_text = "Transcation Date ( F2 ) "
        if transcation_date_tool_tip_locator.is_displayed():
            print(f"tool tip displayed for transcation date")
            if text == Expected_text:
                print(f"Both {text} and {Expected_text} are equal")
            else:
                print(f"Both {text} and {Expected_text} are not equal")
        else:
            print(f"tool tip is not displayed for transcation date")

        Error_text2 = []
        for _ in range(7):
            transcation_date_in_main_page_locator.send_keys(Keys.BACKSPACE)
            # error msg
            wait = WebDriverWait(self.driver, 40, poll_frequency=3, ignored_exceptions=[Exception])
            error_msg_for_wrong_input_validation_in_transcation_date_locator = wait.until(
                EC.presence_of_element_located(self.error_msg_for_wrong_input_validation_in_transcation_date))
            if error_msg_for_wrong_input_validation_in_transcation_date_locator.is_displayed():
                actions = ActionChains(self.driver)
                actions.move_to_element(error_msg_for_wrong_input_validation_in_transcation_date_locator).perform()
                # Capture the text of the error message
                error_message_text = error_msg_for_wrong_input_validation_in_transcation_date_locator.get_attribute("aria-label")
                # Expected error message
                expected_error_message = "Please enter valid date"  # Replace with your expected error message
                if error_message_text == expected_error_message:
                    Error_text2.append(error_message_text)
                else:
                    print("Validation error message does not match the expected error message. Actual:",
                          error_message_text)
            else:
                print("validation message in Applicable from is not displayed")
            time.sleep(1)
        time.sleep(1)

        transcation_date_in_main_page_locator.send_keys("33/2024")
        Error_text3 = []
        for _ in range(7):
            transcation_date_in_main_page_locator.send_keys(Keys.BACKSPACE)
            # error msg
            wait = WebDriverWait(self.driver, 40, poll_frequency=3, ignored_exceptions=[Exception])
            error_msg_for_wrong_input_validation_in_transcation_date_locator = wait.until(
                EC.presence_of_element_located(self.error_msg_for_wrong_input_validation_in_transcation_date))
            if error_msg_for_wrong_input_validation_in_transcation_date_locator.is_displayed():
                actions = ActionChains(self.driver)
                actions.move_to_element(error_msg_for_wrong_input_validation_in_transcation_date_locator).perform()
                # Capture the text of the error message
                error_message_text = error_msg_for_wrong_input_validation_in_transcation_date_locator.get_attribute(
                    "aria-label")
                # Expected error message
                expected_error_message = "Please enter valid date"  # Replace with your expected error message
                if error_message_text == expected_error_message:
                    Error_text2.append(error_message_text)
                else:
                    print("Validation error message does not match the expected error message. Actual:",
                          error_message_text)
            else:
                print("validation message in Applicable from is not displayed")
            time.sleep(1)
        time.sleep(1)
        transcation_date_in_main_page_locator.send_keys("12/2020")
        wait = WebDriverWait(self.driver, 40, poll_frequency=3, ignored_exceptions=[Exception])
        error_msg_for_date_prior_in_transcation_date_locator = wait.until(
            EC.presence_of_element_located(self.error_msg_for_date_prior_in_transcation_date))
        if error_msg_for_date_prior_in_transcation_date_locator.is_displayed():
            actions = ActionChains(self.driver)
            actions.move_to_element(error_msg_for_date_prior_in_transcation_date_locator).perform()
            # Capture the text of the error message
            error_message_text = error_msg_for_date_prior_in_transcation_date_locator.get_attribute(
                "aria-label")
            # Expected error message
            expected_error_message = "Date should not be prior to books beginning from date"  # Replace with your expected error message
            if error_message_text == expected_error_message:
                Error_text2.append(error_message_text)
            else:
                print("Validation error message does not match the expected error message. Actual:",
                      error_message_text)
        else:
            print("validation message in Applicable from is not displayed")
        time.sleep(1)
        # empty
        for _ in range(10):
            transcation_date_in_main_page_locator.send_keys(Keys.BACKSPACE)
        # error msg
        wait = WebDriverWait(self.driver, 40, poll_frequency=3, ignored_exceptions=[Exception])
        empty_transcation_date_locator = wait.until(
            EC.presence_of_element_located(self.empty_transcation_date))
        if empty_transcation_date_locator.is_displayed():
            actions = ActionChains(self.driver)
            actions.move_to_element(empty_transcation_date_locator).perform()
            # Capture the text of the error message
            error_message_text = empty_transcation_date_locator.get_attribute("aria-label")
            # Expected error message
            expected_error_message = "Voucher date is required"  # Replace with your expected error message
            if error_message_text == expected_error_message:
                print("Validation error message matches the expected error message:", error_message_text)
            else:
                print("Validation error message does not match the expected error message. Actual:",
                          error_message_text)
        else:
            print("validation message in Applicable from is not displayed")
        time.sleep(1)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcation_date_in_main_page_locator = wait.until(
            EC.presence_of_element_located(self.transcation_date_in_main_page))
        transcation_date_in_main_page_locator.send_keys("01/10/2024")

    def transcation_no(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcation_no_locator = wait.until(
            EC.presence_of_element_located(self.transcation_no_element))
        actions = ActionChains(self.driver)
        actions.move_to_element(transcation_no_locator).perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcation_no_tool_tip_locator = wait.until(
            EC.visibility_of_element_located(self.transcation_no_tool_tip))
        text = transcation_no_tool_tip_locator.text
        Expected_text = "Transcation Number"
        if transcation_no_tool_tip_locator.is_displayed():
            print(f"tool tip displayed for transcation Number")
            if text == Expected_text:
                print(f"Both {text} and {Expected_text} are equal")
            else:
                print(f"Both {text} and {Expected_text} are not equal")
        else:
            print(f"tool tip is not displayed for transcation Number")
        Atttribute_value = transcation_no_locator.get_attribute("value")
        for _ in Atttribute_value:
            transcation_no_locator.send_keys(Keys.BACKSPACE)

        # empty error msg
        wait = WebDriverWait(self.driver, 40, poll_frequency=3, ignored_exceptions=[Exception])
        empty_error_msg_for_transcation_no_locator = wait.until(
            EC.presence_of_element_located(self.empty_error_msg_for_transcation_no))
        if empty_error_msg_for_transcation_no_locator.is_displayed():
            actions = ActionChains(self.driver)
            actions.move_to_element(empty_error_msg_for_transcation_no_locator).perform()
            # Capture the text of the error message
            error_message_text = empty_error_msg_for_transcation_no_locator.get_attribute("aria-label")
            # Expected error message
            expected_error_message = "This field is mandatory"  # Replace with your expected error message
            if error_message_text == expected_error_message:
                print("Validation error message matches the expected error message:", error_message_text)
            else:
                print("Validation error message does not match the expected error message. Actual:",
                      error_message_text)
        else:
            print("validation message in Applicable from is not displayed")
        # up to 50 characters
        transcation_no_locator.send_keys("pay-to-dinesh-123@#")

        wait = WebDriverWait(self.driver, 40, poll_frequency=3, ignored_exceptions=[Exception])
        error_msg_in_transcation_date_more_than_16_locator = wait.until(
            EC.presence_of_element_located(self.error_msg_in_transcation_date_more_than_16))
        if error_msg_in_transcation_date_more_than_16_locator.is_displayed():
            actions = ActionChains(self.driver)
            actions.move_to_element(error_msg_in_transcation_date_more_than_16_locator).perform()
            # Capture the text of the error message
            error_message_text = error_msg_in_transcation_date_more_than_16_locator.get_attribute("aria-label")
            # Expected error message
            expected_error_message = "Voucher Number Exceeds 16 characters"  # Replace with your expected error message
            if error_message_text == expected_error_message:
                print("Validation error message matches the expected error message:", error_message_text)
            else:
                print("Validation error message does not match the expected error message. Actual:",
                      error_message_text)
        else:
            print("validation message in Applicable from is not displayed")

        # click on refresh
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_refresh_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_refresh))
        actions.move_to_element(click_on_refresh_locator).click().perform()

    def GST_in_main_page(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        gst_in_no_locator = wait.until(
            EC.element_to_be_clickable(self.gst_in_no))
        actions.move_to_element(gst_in_no_locator).click().perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        first_text_in_gst_locator = wait.until(
            EC.presence_of_element_located(self.first_text_in_gst))
        text1  = first_text_in_gst_locator.text
        print(text1)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        second_text_in_gst_locator = wait.until(
            EC.presence_of_element_located(self.second_text_in_gst))
        text2 = second_text_in_gst_locator.text
        print(text2)

        # mouse hover
        actions.move_to_element(gst_in_no_locator).perform()
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        mouse_hover_in_gst_in = wait.until(
            EC.presence_of_element_located(self.mouse_hover_in_gst_in))
        text3 = mouse_hover_in_gst_in.text
        if mouse_hover_in_gst_in.is_displayed():
            print("element is displayed")
            Expected_text = "27AHTPT7639N2Z0"
            if text3 == Expected_text:
                print(f"Both {text3} and {Expected_text} are equal")
            else:
                print(f"Both {text3} and {Expected_text} are not  equal")
        else:
            print("element is not displayed")

    # organisation settings
    def check_single_double(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        check_single_locator = wait.until(
            EC.presence_of_element_located(self.check_single))
        color = check_single_locator.value_of_css_property("color")
        print(color)
        Expected_text  = "rgba(48, 95, 240, 1)"
        if color == Expected_text:
            print("default selected value is single and colour code matches")
        background_color = check_single_locator.value_of_css_property("background-color")
        print(background_color)
        Expected_text1 = "rgba(247, 248, 250, 1)"
        if background_color == Expected_text1:
            print("default selected value is single and colour code matches")
        Text = check_single_locator.text
        Expected_text3 = "Single"
        if Text == Expected_text3:
            print(f"Both {Text} and {Expected_text3} are equal")
        # check payment made from
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=3)
            payment_made_from_ledger_name_locator = wait.until(
                EC.presence_of_element_located(self.payment_made_from_ledger_name))
            if payment_made_from_ledger_name_locator.is_displayed():
                print("it is in double mode")
        except TimeoutException:
            pass
        print("it is single mode and it is default also")



















































































































