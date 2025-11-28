import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import pyautogui
from datetime import date


class Sales:
    def __init__(self, driver):
        self.driver = driver
        self.click_CreateButton_On_MainPage = (By.XPATH,
                                               '//*[@class="btn btn-primary dropdown-toggle h-36px-plus-btn new-btn-tooltip b-r-8"]')
        self.click_on_Accounting_transcations = (By.XPATH, '//*[normalize-space(text())="Accounting Transactions"]')
        self.click_on_Accounting_transcations_sales = (By.XPATH,
                                                       '//*[normalize-space(text())="Accounting Transactions"]')
        self.click_on_sales = (By.XPATH, '//*[normalize-space(text())="Sales"]')
        self.click_on_inventory_button = (By.XPATH, '//*[@class="p-inputswitch-slider"]')
        self.click_on_yes_button_while_reswitch = (By.XPATH, '//*[@id="ACCEP"]')
        self.click_on_customer_details_dropdown = (By.XPATH,
                                                   '(//*[@class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium '
                                                   'MuiAutocomplete-popupIndicator '
                                                   'css-qzbt6i-MuiButtonBase-root-MuiIconButton-root-MuiAutocomplete-popupIndicator"])[1]')
        self.click_on_customer_details_list = (By.XPATH, '//*[@class="col-8 flex-grow-1"]')
        self.closing_balance_amount = (By.XPATH, '//*[@class="text-color-3"]')
        self.click_on_godown = (By.XPATH, '(//*[@class="card-body p-total-16"])[2]')
        self.change_organisation_drop_down = (By.XPATH,
                                              '(//*[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"])[1]')
        self.alpha_tech_bhavani = (By.XPATH, '//*[normalize-space(text())="Alpha Tech Bhavani"]')
        self.godown_list = (By.XPATH, '//*[@class="col-8 flex-grow-1"]')
        self.click_on_godown_dropdown = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[2]')
        self.order_no_list = (By.XPATH, '//*[@class="col-8 flex-grow-1"]')
        self.order_no_dropdown = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[3]')
        self.effective_date_feild = (By.XPATH, '//*[@id="vp-effectiveDate"]')
        self.validation_error = (By.XPATH, '//*[@aria-label="Invalid date format"]')
        self.click_on_add_item = (By.XPATH, '//*[@id="addItemButton"]')
        self.text_to_conform_add_details_page_opened = (By.XPATH, '//*[@id="ItemTab_0"]')
        self.itemlist_in_stock_item_list = (By.XPATH, '//*[@id="item-stockItemID-listbox"]//li')
        self.click_on_stock_item_drop_down = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[2]')
        self.mouse_hover_on_sales_ledger_hover = (By.XPATH,
                                                  '//*[@class="fi fi-br-info l-h-1 v-align-middle font-size-12"]')
        self.sales_ledger_drop_down = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[3]')
        self.sales_ledger_list = (By.XPATH, '//*[@id="item-ledgerID-listbox"]//li')
        self.unit_drop_down_click = (By.XPATH, '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[4]')
        self.unit_list = (By.XPATH, '//*[@id="item-stockUnitID-listbox"]//li')
        self.hsn_code_input_feild = (By.XPATH, '//*[@name="item.gstTaxRate.hsnSAC"]')
        self.currency_drop_down_click = (By.XPATH,
                                         '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[5]')
        self.currency_list = (By.XPATH,
                              '//ul[@class="MuiAutocomplete-listbox autocomplete-listbox css-gdh49b-MuiAutocomplete-listbox"]//li')
        self.hsn_code_after8_validation_error = (By.XPATH, '//*[@aria-label="HSN Code must be between 4 to 8 digits"]')
        self.validation_error_for_empty_rate = (By.XPATH, '//*[@aria-label="Provide exchange rate"]')
        self.rate_input_feild = (By.XPATH, '//*[@id="item-exchangeRate"]')
        self.order_no_drop_down = (By.XPATH,
                                   '//*[@class="fi fi-bs-angle-down l-h-1 v-align-middle font-size-10 text-color-2"]')
        self.order_no_input_feild = (By.XPATH, '//*[@placeholder="Order No."]')
        self.create_new_order = (By.XPATH, '//*[@id="singleSelection-Create"]')
        self.order_no_input_feild_inside = (By.XPATH, '//*[@id="singleSelection_CreateInput"]')
        self.click_on_radio_button_not_applicable = (By.XPATH, '//*[@class="p-radiobutton-box "]')
        self.click_on_select_button = (By.XPATH, '//*[@id="singleSelection_Save"]')
        self.click_on_new_button_radio_button = (By.XPATH, '//*[@class="p-radiobutton-box p-highlight"]')
        self.click_on_godown_dropdown_in_quantity_and_prices = (By.XPATH,
                                                                '(//*[@class="fi fi-ss-angle-small-down font-size-18"])[6]')
        self.godown_list_in_quantities = (By.XPATH, '//*[@id="item-batches-0-godownID-listbox"]//li')
        self.batch_no_input_feild = (By.XPATH, '//*[@placeholder="Batch No."]')
        self.click_on_create_new_batch = (By.XPATH, '//*[@id="createNewBtn"]')
        self.validation_error_for_empty_actual_quantity = (By.XPATH, '//*[@aria-label="Provide actual quantity"]')
        self.quantity_input_feild = (By.XPATH, '(//*[@placeholder="Qty"])[1]')
        self.count_for_actual_no_s = (By.XPATH, '//*[@class="plain-label b-r-8-imp ms-2"]')
        self.billed_quantity_input = (By.XPATH, '//*[@name="item.batches.0.billedQty"]')
        self.billed_quantity_empty_validation_error_msg = (By.XPATH,
                                                           '//*[@aria-label="Either Billed Quantity or Actual Quantity should be above 0"]')
        self.empty_unit_price_validation_error = (By.XPATH,'//*[@aria-label="Provide unit price"]')
        self.unit_feild = (By.XPATH,'//*[@id="item-batches-0-unitPrice"]')
        self.discount_input_feild = (By.NAME,"item.batches.0.discount")

    def Click_CreateButton_On_MainPage(self):
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        Click_CreateButton_On_MainPage_locator = wait.until(
            EC.element_to_be_clickable(self.click_CreateButton_On_MainPage))
        # actions = ActionChains(self.driver)
        # actions.move_to_element(Click_CreateButton_On_MainPage_locator).perform()
        # tooltip_text = self.driver.execute_script('return arguments[0].getAttribute("data-original-title");',
        #                                           Click_CreateButton_On_MainPage_locator)
        # print("Tooltip Text:", tooltip_text)
        self.driver.execute_script("arguments[0].click();", Click_CreateButton_On_MainPage_locator)
        time.sleep(3)

    def Click_accounting_transcations_in_create_sales(self):
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        click_accounting_transcations_button = wait.until(
            EC.presence_of_element_located(self.click_on_Accounting_transcations))
        click_accounting_transcations_button.click()
        time.sleep(3)

    def Click_accounting_transcations_sales_in_create_sales(self):
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        click_accounting_transcations_sales_button = wait.until(
            EC.presence_of_element_located(self.click_on_Accounting_transcations))
        click_accounting_transcations_sales_button.click()
        time.sleep(3)
        # click on sales
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        click_on_sales_button = wait.until(
            EC.element_to_be_clickable(self.click_on_sales))
        click_on_sales_button.click()
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)

    def change_organisation(self):
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        change_organisation_drop_down_button = wait.until(
            EC.element_to_be_clickable(self.change_organisation_drop_down))
        actions = ActionChains(self.driver)
        actions.move_to_element(change_organisation_drop_down_button).click().perform()
        # select organisation
        alpha_tech_bhavani_org = wait.until(
            EC.element_to_be_clickable(self.alpha_tech_bhavani))
        actions.move_to_element(alpha_tech_bhavani_org).click().perform()

    def check_inventory_button(self):
        actions = ActionChains(self.driver)
        try:
            wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                                 ignored_exceptions=[Exception, TimeoutException])
            time.sleep(1)
            for _ in range(2):
                click_accounting_transcations_inventory_button = wait.until(
                    EC.presence_of_element_located(self.click_on_inventory_button))
                actions = ActionChains(self.driver)
                actions.move_to_element(click_accounting_transcations_inventory_button).click().perform()
                time.sleep(1)
            click_on_yes_button = wait.until(
                EC.element_to_be_clickable(self.click_on_yes_button_while_reswitch))
            actions.move_to_element(click_on_yes_button).click().perform()
            time.sleep(2)
            click_accounting_transcations_inventory_button = wait.until(
                EC.presence_of_element_located(self.click_on_inventory_button))
            actions.move_to_element(click_accounting_transcations_inventory_button).click().perform()
        except StaleElementReferenceException:
            pass

    def customer_details_dropdown(self):
        actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        click_customer_details_dropdown = wait.until(
            EC.presence_of_element_located(self.click_on_customer_details_dropdown))
        actions.move_to_element(click_customer_details_dropdown).click().perform()
        time.sleep(3)

    def click_on_list(self):
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_customer_details_lists = wait.until(
                EC.presence_of_all_elements_located(self.click_on_customer_details_list))

            # for index in range(len(click_on_customer_details_lists)):
            for index in range(min(10, len(click_on_customer_details_lists))):
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_customer_details_lists = wait.until(
                    EC.presence_of_all_elements_located(self.click_on_customer_details_list))

                # re-fetch element by index each time to avoid stale element
                i = click_on_customer_details_lists[index]

                print(f"Clicking customer details element at index: {index}")  # 👈 index print

                dinesh = ActionChains(self.driver)
                dinesh.move_to_element(i).click().perform()
                time.sleep(0.5)
                closing_dropdown_text = wait.until(
                    EC.presence_of_element_located(self.closing_balance_amount))
                closing_balance_text1 = closing_dropdown_text.text

                # print(f"closingbalancetext: {closing_balance_text1}")
                right_side_text = closing_balance_text1.split(":")[1].strip()
                print(f"closingbalancetext: {right_side_text}")

                actions = ActionChains(self.driver)
                wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                                     ignored_exceptions=[Exception, TimeoutException])
                click_customer_details_dropdown = wait.until(
                    EC.element_to_be_clickable(self.click_on_customer_details_dropdown))
                actions.move_to_element(click_customer_details_dropdown).click().perform()

        except (StaleElementReferenceException, TimeoutException):
            pass
        pyautogui.press("escape")
        time.sleep(3)

        # click on godown
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        click_on_godown_button = wait.until(
            EC.element_to_be_clickable(self.click_on_godown))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_godown_button).click().perform()
        time.sleep(0.5)
        for i in range(2):
            pyautogui.press("escape")
            time.sleep(0.5)
        pyautogui.press("space")
        time.sleep(1)

    def click_on_godown_list(self):
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            godown_list_lists = wait.until(
                EC.presence_of_all_elements_located(self.godown_list))

            # for index in range(len(click_on_customer_details_lists)):
            for index in range(len(godown_list_lists)):
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                godown_list_lists = wait.until(
                    EC.presence_of_all_elements_located(self.godown_list))

                # re-fetch element by index each time to avoid stale element
                i = godown_list_lists[index]

                print(f"Clicking customer details element at index: {index}")  # 👈 index print

                dinesh = ActionChains(self.driver)
                dinesh.move_to_element(i).click().perform()
                time.sleep(0.5)

                actions = ActionChains(self.driver)
                wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                                     ignored_exceptions=[Exception, TimeoutException])
                click_on_godown_dropdown_button = wait.until(
                    EC.element_to_be_clickable(self.click_on_godown_dropdown))
                actions.move_to_element(click_on_godown_dropdown_button).click().perform()
        except (StaleElementReferenceException, TimeoutException):
            pass
        pyautogui.press("escape")
        time.sleep(2)

    def order_no_list_overall(self):
        try:
            wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                                 ignored_exceptions=[Exception, TimeoutException])
            order_no_dropdown_click = wait.until(
                EC.element_to_be_clickable(self.order_no_dropdown))
            actions = ActionChains(self.driver)
            actions.move_to_element(order_no_dropdown_click).click().perform()
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            order_no_lists = wait.until(
                EC.presence_of_all_elements_located(self.order_no_list))

            # for index in range(len(click_on_customer_details_lists)):
            for index in range(len(order_no_lists)):
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                order_no_lists = wait.until(
                    EC.presence_of_all_elements_located(self.order_no_list))

                # re-fetch element by index each time to avoid stale element
                i = order_no_lists[index]

                print(f"Clicking customer details element at index: {index}")  # 👈 index print

                dinesh = ActionChains(self.driver)
                dinesh.move_to_element(i).click().perform()
                time.sleep(0.5)

                actions = ActionChains(self.driver)
                wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                                     ignored_exceptions=[Exception, TimeoutException])
                order_no_dropdown_click = wait.until(
                    EC.element_to_be_clickable(self.order_no_dropdown))
                actions.move_to_element(order_no_dropdown_click).click().perform()
        except (StaleElementReferenceException, TimeoutException):
            pass

    def effective_date(self):
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        effective_date_feild_feild = wait.until(
            EC.presence_of_element_located(self.effective_date_feild))
        get_value = effective_date_feild_feild.get_attribute("value")
        print("Value attribute:", get_value)
        Expected_value_today = date.today()
        formatted_date = Expected_value_today.strftime("%d/%m/%Y")
        if formatted_date == get_value:
            print(f"both {formatted_date} and {get_value} are equal")
        else:
            print(f"both {formatted_date} and {get_value} are not equal")

        for _ in get_value:
            effective_date_feild_feild.send_keys(Keys.BACKSPACE)
        time.sleep(0.5)
        effective_date_feild_feild.send_keys("1/3/2000")
        time.sleep(0.5)
        pyautogui.press("escape")
        time.sleep(0.5)
        # error for wrong date
        wait = WebDriverWait(self.driver, 40, poll_frequency=3, ignored_exceptions=[Exception])
        error_msg_for_wrong_date = wait.until(
            EC.presence_of_element_located(self.validation_error))

        if error_msg_for_wrong_date.is_displayed():
            actions = ActionChains(self.driver)
            actions.move_to_element(error_msg_for_wrong_date).perform()
            # Capture the text of the error message
            error_message_text = error_msg_for_wrong_date.get_attribute(
                "aria-label")
            # Expected error message
            expected_error_message = "Invalid date format"  # Replace with your expected error message
            if error_message_text == expected_error_message:
                print("Validation error message matches the expected error message:", error_message_text)
            else:
                print("Validation error message does not match the expected error message. Actual:",
                      error_message_text)
        else:
            print("validation message in empty Ledger input feild is not displayed")
        for _ in get_value:
            effective_date_feild_feild.send_keys(Keys.BACKSPACE)
        time.sleep(0.5)
        effective_date_feild_feild.send_keys("01/03/2024")
        time.sleep(5)
        pyautogui.press("escape")
        time.sleep(3)

    def items_and_ledgers(self):
        # pyautogui.hotkey('alt', '1')
        # time.sleep(0.5)
        # pyautogui.press("escape")
        # time.sleep(1.5)
        try:
            wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                                 ignored_exceptions=[Exception, TimeoutException])
            click_on_add_item_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_add_item))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_add_item_locator).click().perform()
        except TimeoutException:
            pass

        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        text_to_conform_add_details_page_opened_locator = wait.until(
            EC.presence_of_element_located(self.text_to_conform_add_details_page_opened))
        text = text_to_conform_add_details_page_opened_locator.text
        Expected_text = "Stock Item Details"
        if text == Expected_text:
            print(f"Both {text} and {Expected_text} are equal,so button is clicked")
        else:
            print(f"Both {text} and {Expected_text} are not equal,so button is not clicked")

    def check_item_name_list_in_stock_items(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_item_details_in_stock_item_details = wait.until(
            EC.presence_of_all_elements_located(self.itemlist_in_stock_item_list))

        # for index in range(len(click_on_customer_details_lists)):
        for index in range(min(10, len(click_item_details_in_stock_item_details))):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_item_details_in_stock_item_details = wait.until(
                EC.presence_of_all_elements_located(self.itemlist_in_stock_item_list))

            # re-fetch element by index each time to avoid stale element
            i = click_item_details_in_stock_item_details[index]

            print(f"Clicking stock item details element at index: {index}")  # 👈 index print

            dinesh = ActionChains(self.driver)
            dinesh.move_to_element(i).click().perform()
            time.sleep(0.5)

            actions = ActionChains(self.driver)
            wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                                 ignored_exceptions=[Exception, TimeoutException])
            click_on_stock_item_drop_down_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_stock_item_drop_down))
            actions.move_to_element(click_on_stock_item_drop_down_locator).click().perform()

    def mouse_hover_on_sales_ledger(self):
        actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        click_on_sales_item_hover = wait.until(
            EC.presence_of_element_located(self.mouse_hover_on_sales_ledger_hover))
        actions.move_to_element(click_on_sales_item_hover).perform()

        Expected_text = ('You can select the most used Sales Ledger as the default sales Ledger'
                         'in the Configurations Tab under "Default Sales Ledger"')

        time.sleep(2)
        Actual_text = click_on_sales_item_hover.get_attribute("aria-label")

        print(Actual_text)
        # Replace with your expected error message
        if Expected_text == Actual_text:
            print(f"Both {Expected_text} and {Actual_text} are equal")
        else:
            print(f"Both {Expected_text} and {Actual_text} are not equal")

        # sales ledger list
        actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        sales_ledger_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.sales_ledger_drop_down))
        actions.move_to_element(sales_ledger_drop_down_locator).click().perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        sales_ledger_list_lists_locator = wait.until(
            EC.presence_of_all_elements_located(self.sales_ledger_list))

        # for index in range(len(click_on_customer_details_lists)):
        for index in range(min(10, len(sales_ledger_list_lists_locator))):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            sales_ledger_list_lists_locator = wait.until(
                EC.presence_of_all_elements_located(self.sales_ledger_list))

            # re-fetch element by index each time to avoid stale element
            i = sales_ledger_list_lists_locator[index]

            print(f"Clicking stock item details element at index: {index}")  # 👈 index print

            dinesh = ActionChains(self.driver)
            dinesh.move_to_element(i).click().perform()
            time.sleep(0.5)

            wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                                 ignored_exceptions=[Exception, TimeoutException])
            sales_ledger_drop_down_locator = wait.until(
                EC.element_to_be_clickable(self.sales_ledger_drop_down))
            actions.move_to_element(sales_ledger_drop_down_locator).click().perform()

    def check_unit_dropdown_in_add_stock_item(self):
        actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        unit_drop_down_click_locator = wait.until(
            EC.element_to_be_clickable(self.unit_drop_down_click))
        actions.move_to_element(unit_drop_down_click_locator).click().perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        unit_list_lists = wait.until(
            EC.presence_of_all_elements_located(self.unit_list))

        # for index in range(len(click_on_customer_details_lists)):
        for index in range(min(10, len(unit_list_lists))):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            unit_list_lists = wait.until(
                EC.presence_of_all_elements_located(self.unit_list))

            # re-fetch element by index each time to avoid stale element
            i = unit_list_lists[index]

            print(f"Clicking unit item details element at index: {index}")  # 👈 index print

            dinesh = ActionChains(self.driver)
            dinesh.move_to_element(i).click().perform()
            time.sleep(0.5)

            wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                                 ignored_exceptions=[Exception, TimeoutException])
            unit_drop_down_click_locator = wait.until(
                EC.element_to_be_clickable(self.unit_drop_down_click))
            actions.move_to_element(unit_drop_down_click_locator).click().perform()

        # HSN code
        hsn_code_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.hsn_code_input_feild))
        Get_attribute_value = hsn_code_input_feild_locator.get_attribute("value")
        for _ in Get_attribute_value:
            hsn_code_input_feild_locator.send_keys(Keys.BACKSPACE)
            time.sleep(0.5)
        hsn_code_input_feild_locator.send_keys("123456789")

        pyautogui.press('tab')
        time.sleep(0.5)

        # validation error for hsn code
        wait = WebDriverWait(self.driver, 40, poll_frequency=3, ignored_exceptions=[Exception])
        hsn_code_after8_validation_error_locator = wait.until(
            EC.presence_of_element_located(self.hsn_code_after8_validation_error))

        if hsn_code_after8_validation_error_locator.is_displayed():
            actions = ActionChains(self.driver)
            actions.move_to_element(hsn_code_after8_validation_error_locator).perform()
            # Capture the text of the error message
            error_message_text = hsn_code_after8_validation_error_locator.get_attribute(
                "aria-label")
            # Expected error message
            expected_error_message = "HSN Code must be between 4 to 8 digits"  # Replace with your expected error message
            if error_message_text == expected_error_message:
                print("Validation error message matches the expected error message:", error_message_text)
            else:
                print("Validation error message does not match the expected error message. Actual:",
                      error_message_text)
        else:
            print("validation message in empty Ledger input feild is not displayed")

        Get_attribute_value1 = hsn_code_input_feild_locator.get_attribute("value")
        for _ in Get_attribute_value1:
            hsn_code_input_feild_locator.send_keys(Keys.BACKSPACE)
            time.sleep(0.5)
        hsn_code_input_feild_locator.send_keys("12345678")

    def rupee_list(self):
        actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        currency_drop_down_click_locator = wait.until(
            EC.element_to_be_clickable(self.currency_drop_down_click))
        actions.move_to_element(currency_drop_down_click_locator).click().perform()
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        currency_list_locators = wait.until(
            EC.presence_of_all_elements_located(self.currency_list))

        # for index in range(len(click_on_customer_details_lists)):
        for index in range(len(currency_list_locators)):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            currency_list_locators = wait.until(
                EC.presence_of_all_elements_located(self.currency_list))

            # re-fetch element by index each time to avoid stale element
            i = currency_list_locators[index]
            print(f"Clicking currency item details element at index: {index}")  # 👈 index print
            dinesh = ActionChains(self.driver)
            dinesh.move_to_element(i).click().perform()
            time.sleep(0.5)
            actions = ActionChains(self.driver)
            wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                                 ignored_exceptions=[Exception, TimeoutException])
            currency_drop_down_click_locator = wait.until(
                EC.element_to_be_clickable(self.currency_drop_down_click))
            actions.move_to_element(currency_drop_down_click_locator).click().perform()

        # check validation error for empty rate
        wait = WebDriverWait(self.driver, 40, poll_frequency=3, ignored_exceptions=[Exception])
        validation_error_for_empty_rate_locator = wait.until(
            EC.presence_of_element_located(self.validation_error_for_empty_rate))

        if validation_error_for_empty_rate_locator.is_displayed():
            actions = ActionChains(self.driver)
            actions.move_to_element(validation_error_for_empty_rate_locator).perform()
            # Capture the text of the error message
            error_message_text = validation_error_for_empty_rate_locator.get_attribute(
                "aria-label")
            # Expected error message
            expected_error_message = "Provide exchange rate"  # Replace with your expected error message
            if error_message_text == expected_error_message:
                print("Validation error message matches the expected error message:", error_message_text)
            else:
                print("Validation error message does not match the expected error message. Actual:",
                      error_message_text)
        else:
            print("validation message in empty Ledger input feild is not displayed")

    def rate_feild(self):
        wait = WebDriverWait(self.driver, 40, poll_frequency=3, ignored_exceptions=[Exception])
        rate_input_feild_locator = wait.until(
            EC.visibility_of_element_located(self.rate_input_feild))
        rate_input_feild_locator.click()
        rate_input_feild_locator.send_keys("10.5")
        # checking normal are taking
        Get_attribute_value_rate_feild = rate_input_feild_locator.get_attribute("value")
        for _ in Get_attribute_value_rate_feild:
            rate_input_feild_locator.send_keys(Keys.BACKSPACE)
            time.sleep(0.5)
        rate_input_feild_locator.send_keys("10")

    def order_no(self):
        # actions = ActionChains(self.driver)
        # wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
        #                      ignored_exceptions=[Exception, TimeoutException])
        # order_no_drop_down_locator = wait.until(
        #     EC.element_to_be_clickable(self.order_no_drop_down))
        # actions.move_to_element(order_no_drop_down_locator).click().perform()
        # time.sleep(5)

        # default value
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        order_no_input_feild_locator = wait.until(
            EC.element_to_be_clickable(self.order_no_input_feild))
        actions = ActionChains(self.driver)
        actions.move_to_element(order_no_input_feild_locator).click().perform()
        Expected_text = "Not Applicable"
        Attribute_value = order_no_input_feild_locator.get_attribute("value")
        print(Attribute_value)
        if Expected_text == Attribute_value:
            print(f"Both {Expected_text} and {Attribute_value} are equal")
        else:
            print(f"Both {Expected_text} and {Attribute_value} are not equal")

    def create_new_order_no(self):
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        create_new_order_locator = wait.until(
            EC.element_to_be_clickable(self.create_new_order))
        dinesh = ActionChains(self.driver)
        dinesh.move_to_element(create_new_order_locator).click().perform()

        # create new thing
        order_no_input_feild_locator1 = wait.until(
            EC.presence_of_element_located(self.order_no_input_feild_inside))
        order_no_input_feild_locator1.send_keys("PO-12345")
        time.sleep(1)

        # click on select
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        click_on_select_button_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_select_button))
        dinesh.move_to_element(click_on_select_button_locator).click().perform()
        time.sleep(1)

    def godown_in_quantity_and_prices(self):
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        click_on_godown_dropdown_in_quantity_and_prices = wait.until(
            EC.element_to_be_clickable(self.click_on_godown_dropdown_in_quantity_and_prices))
        dinesh = ActionChains(self.driver)
        dinesh.move_to_element(click_on_godown_dropdown_in_quantity_and_prices).click().perform()
        # click_on_godown_dropdown_in_quantity_and_prices.click()

        # list checking
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        godown_list_in_quantities_locators = wait.until(
            EC.presence_of_all_elements_located(self.godown_list_in_quantities))

        # for index in range(len(click_on_customer_details_lists)):
        for index in range(len(godown_list_in_quantities_locators)):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            currency_list_locators = wait.until(
                EC.presence_of_all_elements_located(self.godown_list_in_quantities))

            # re-fetch element by index each time to avoid stale element
            i = currency_list_locators[index]
            print(f"Clicking godown item at index: {index}")  # 👈 index print
            dinesh = ActionChains(self.driver)
            dinesh.move_to_element(i).click().perform()
            time.sleep(0.5)
            wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                                 ignored_exceptions=[Exception, TimeoutException])
            click_on_godown_dropdown_in_quantity_and_prices = wait.until(
                EC.element_to_be_clickable(self.click_on_godown_dropdown_in_quantity_and_prices))
            dinesh = ActionChains(self.driver)
            dinesh.move_to_element(click_on_godown_dropdown_in_quantity_and_prices).click().perform()

    def batch_no_total(self):
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        batch_no_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.batch_no_input_feild))
        batch_no_input_feild_locator.send_keys("122")
        time.sleep(3)

        # create new batch
        click_on_create_new_batch_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_create_new_batch))
        dinesh = ActionChains(self.driver)
        dinesh.move_to_element(click_on_create_new_batch_locator).click().perform()
        time.sleep(3)

        for _ in range(2):
            pyautogui.press('tab')
            time.sleep(0.3)

    def Actual_quantity(self):
        # empty error msg
        wait = WebDriverWait(self.driver, 40, poll_frequency=3, ignored_exceptions=[Exception])
        validation_error_for_empty_actual_quantity_locator = wait.until(
            EC.presence_of_element_located(self.validation_error_for_empty_actual_quantity))

        if validation_error_for_empty_actual_quantity_locator.is_displayed():
            actions = ActionChains(self.driver)
            actions.move_to_element(validation_error_for_empty_actual_quantity_locator).perform()
            # Capture the text of the error message
            error_message_text = validation_error_for_empty_actual_quantity_locator.get_attribute("aria-label")
            # Expected error message
            expected_error_message = "Provide actual quantity"  # Replace with your expected error message
            if error_message_text == expected_error_message:
                print("Validation error message matches the expected error message:", error_message_text)
            else:
                print("Validation error message does not match the expected error message. Actual:",
                      error_message_text)
        else:
            print("validation message in empty Ledger input feild is not displayed")

        # input feild of actual quantity
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        quantity_input_feild_locator = wait.until(
            EC.presence_of_element_located(self.quantity_input_feild))
        input_value = quantity_input_feild_locator.get_attribute("value")
        text = len(input_value)
        count_for_actual_no_s_locator = wait.until(
            EC.presence_of_element_located(self.count_for_actual_no_s))
        text_count = count_for_actual_no_s_locator.text
        print(text_count)
        if text == text_count:
            print("Both are equal")
        else:
            print("Both are not equal")

        # enter something
        quantity_input_feild_locator.send_keys("10")
        time.sleep(2)

        Attribute_value_of_quantity_feild = quantity_input_feild_locator.get_attribute("value")
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        billed_quantity_input_locator = wait.until(
            EC.presence_of_element_located(self.billed_quantity_input))

        Attribute_value_of_billed_quantity = billed_quantity_input_locator.get_attribute("value")

        if Attribute_value_of_quantity_feild == Attribute_value_of_billed_quantity:
            print(f"Both {Attribute_value_of_billed_quantity} and {Attribute_value_of_quantity_feild} are equal")
        else:
            print(f"Both {Attribute_value_of_billed_quantity} and {Attribute_value_of_quantity_feild} are not equal")
        for _ in range(2):
            pyautogui.press('tab')

    def unit_price_column(self):
        # empty error msg
        wait = WebDriverWait(self.driver, 40, poll_frequency=3, ignored_exceptions=[Exception])
        empty_unit_price_validation_error_locator = wait.until(
            EC.presence_of_element_located(self.empty_unit_price_validation_error))

        if empty_unit_price_validation_error_locator.is_displayed():
            actions = ActionChains(self.driver)
            actions.move_to_element(empty_unit_price_validation_error_locator).perform()
            # Capture the text of the error message
            error_message_text = empty_unit_price_validation_error_locator.get_attribute("aria-label")
            # Expected error message
            expected_error_message = "Provide unit price"  # Replace with your expected error message
            if error_message_text == expected_error_message:
                print("Validation error message matches the expected error message:", error_message_text)
            else:
                print("Validation error message does not match the expected error message. Actual:",
                      error_message_text)
        else:
            print("validation message in empty Ledger input feild is not displayed")

        #   unit price
        wait = WebDriverWait(self.driver,timeout=20,poll_frequency=3,
                             ignored_exceptions=(TimeoutException,StaleElementReferenceException))
        unit_feild_input = wait.until(EC.presence_of_element_located(self.unit_feild))
        unit_feild_input.send_keys("10000")

    def discount(self):
        wait = WebDriverWait(self.driver,timeout=30,poll_frequency=3,
                             ignored_exceptions=(TimeoutException,StaleElementReferenceException))
        discount_feild_input_locator = wait.until(EC.presence_of_element_located(self.discount_input_feild))
        discount_feild_input_locator.send_keys("10.5333")

















