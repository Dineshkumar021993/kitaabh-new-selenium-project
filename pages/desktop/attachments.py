import os.path
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
import allure
from pynput.keyboard import Key, Controller
from tqdm import tqdm

global i
class auto_update:
    def __init__(self, driver):
        self.driver = driver
        self.tooltip_text = (By.XPATH, '//*[normalize-space(text())="Yes, please"]')

    def auto_update_tool_tip(self):
        # switchingToPopUpWindow = self.driver.window_handles[-1]
        # self.driver.switch_to.window(switchingToPopUpWindow)
        time.sleep(6)
        # alert = self.driver.switch_to.alert()
        # alert.accept()
        time.sleep(2)
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        tooltip_text_locator = wait.until(
            EC.element_to_be_clickable(self.tooltip_text))
        actions = ActionChains(self.driver)
        actions.move_to_element(
            tooltip_text_locator).click().perform()

class PraticeAttachments:
    def __init__(self, driver):
        self.driver = driver
        self.click_on_ledgers_locator = (By.XPATH, '//*[normalize-space(text())="Ledgers"]')
        self.click_masters_in_create_ledger = (By.XPATH,
                                               '(//*[normalize-space(text())="Accounting Masters"])[1]')
        self.click_CreateButton_On_MainPage = (By.XPATH, '//*[@class="btn btn-primary dropdown-toggle h-36px-plus-btn new-btn-tooltip b-r-8"]')
        self.click_on_add_attachments = (By.XPATH, '//*[@id="Abtn"]')
        self.load_bar = (By.XPATH, '//*[@class="p-progressbar"]')
        self.click_on_attachments_outside = (By.XPATH, '//span[normalize-space(text())="Attachments"]')
        self.click_on_accounting_vouchers = (By.XPATH, '//*[@id="MODULE1"]')
        self.click_on_sales = (By.XPATH, '//*[@id="SUB_MODULE0"]')
        self.voucher_no_input_feild = (By.XPATH, '//*[@id="voucherNo"]')
        self.tooltip_text = (By.XPATH,'//*[normalize-space(text())="Voucher Number"]')
        self.click_on_configurations = (By.XPATH,'//*[normalize-space(text())="Configurations"]')
        self.voucher_date_list = (By.XPATH,'//*[normalize-space(text())="Current Date"]//ancestor::ul//div')
        self.default_voucher_date_click = (By.XPATH,'(//i[@class="fi fi-ss-angle-small-down font-size-18"])[3]')

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

    def Click_masters_in_create_ledger(self):
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        Click_masters_in_create_ledger_locator = wait.until(
            EC.presence_of_element_located(self.click_masters_in_create_ledger))
        Click_masters_in_create_ledger_locator.click()
        time.sleep(3)

    def Click_ledgers_button(self):
        wait = WebDriverWait(self.driver, timeout=50, poll_frequency=3,
                             ignored_exceptions=[Exception, TimeoutException])
        Click_on_ledgers = wait.until(
            EC.presence_of_element_located(self.click_on_ledgers_locator))
        Click_on_ledgers.click()
        time.sleep(3)

    def click_attachments(self):
        # actions = ActionChains(self.driver)
        # actions.key_down(Keys.ALT).send_keys('u').key_up(Keys.ALT).perform()
        #
        # click_on_attachments

        global i
        wait = WebDriverWait(self.driver, 50, poll_frequency=3, ignored_exceptions=[Exception])
        click_on_attachments_outside_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_attachments_outside))
        actions = ActionChains(self.driver)
        actions.move_to_element(
            click_on_attachments_outside_locator).click().perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3, ignored_exceptions=[Exception])
        click_on_add_attachments_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_add_attachments))
        actions = ActionChains(self.driver)
        actions.move_to_element(
            click_on_add_attachments_locator).click().perform()

        # PDF xlsx
        file_path = "C:\\Users\\Dinesh\\Downloads\\pratice.xlsx"
        keyboard = Controller()
        time.sleep(3)
        keyboard.type(file_path)
        time.sleep(3)
        keyboard.press(Key.enter)
        time.sleep(2)
        keyboard.release(Key.enter)

        file_name = os.path.basename(file_path)
        file_extension = os.path.splitext(file_name)[1]
        file_size = os.path.getsize(file_path)
        file_size_mb = round(file_size / (1024 * 1024),2)

        print(f"File Name: {file_name}")
        print(f"File Extension: {file_extension}")
        print(f"File Size: {file_size} bytes")
        print(f"File Size in MB: {file_size_mb} MB")

        file_name_expected_text = "pratice.xlsx"
        file_extension_expected_text = ".xlsx"
        file_size_expected_text = 0.02

        if file_name == file_name_expected_text:
            print(f"Both {file_name} and {file_name_expected_text} are equal")

        if file_extension == file_extension_expected_text:
            print(f"Both {file_extension} and {file_extension_expected_text} are equal")

        if file_size_mb == file_size_expected_text:
            print(f"Both {file_size_mb} MB and {file_size_expected_text} MB are equal")


        for i in tqdm(range(101), ascii=False, ncols=75):
            time.sleep(0.01)

            if i == 79:
                print("\nReached 79%")

            print(f"Progress: {i}% ", end='\r', flush=True)
        print("\nProgress bar displayed and completed fully")
        print(f"Final value of i: {i}")

    def sales_voucher(self,locator,click=True,text = None):
        if click:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3, ignored_exceptions=[Exception])
            element = wait.until(
                EC.element_to_be_clickable(locator))
            actions = ActionChains(self.driver)
            actions.move_to_element(
                element).click().perform()

        elif isinstance(locator, list):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3, ignored_exceptions=[Exception])
            elements = wait.until(EC.presence_of_all_elements_located(locator))
            for element in elements:
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()

                element = wait.until(
                    EC.element_to_be_clickable(locator))
                actions = ActionChains(self.driver)
                actions.move_to_element(
                    element).click().perform()
        else:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3, ignored_exceptions=[Exception])
            element = wait.until(EC.presence_of_element_located(locator))
            if text is not None:
               element.send_keys(text)
            return element

    def click_on_sales_vouchers(self):
        self.sales_voucher(self.click_on_accounting_vouchers)
        self.sales_voucher(self.click_on_sales)
        # self.sales_voucher(self.voucher_no_input_feild, click=False,text = "dinesh")
        for text in ["dinesh", "shiva","Dinesh"*10]:
            element = self.sales_voucher(self.voucher_no_input_feild, click=False, text=text)
            Attribute_value = element.get_attribute("value")
            for _ in Attribute_value:
                element.send_keys(Keys.BACKSPACE)
            time.sleep(1)
        self.sales_voucher(self.voucher_no_input_feild, click=False,text = "dinesh")
        self.sales_voucher(self.click_on_configurations)
        self.sales_voucher(self.voucher_date_list)
        self.sales_voucher(self.default_voucher_date_click)








