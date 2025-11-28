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

class ReceiptVoucher:
    def __init__(self, driver):
        self.driver = driver
        self.click_on_organisation_drop_down = (
            By.XPATH, '(//*[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"])[1]')
        self.click_on_alpha_adarsh_organisation = (By.XPATH, '//*[normalize-space(text())="Alpha Adarsh"]')
        self.click_on_create_button = (By.XPATH, '//i[@class="fi fi-br-plus l-h-1 v-align-middle font-size-12"]')
        self.click_on_receipt_voucher_transcation_type = (By.XPATH,'(//*[@class="fi fi-ss-angle-small-down font-size-18"])[1]')
        self.click_on_receipt_in_transcation_type = (By.XPATH,'//*[normalize-space(text())="Receipt"]')
        self.click_on_receipt = (By.ID,'VCHCTABLE1')
        self.click_on_Amount_received_from_drop_down = (By.XPATH,'(//*[@class="fi fi-ss-angle-small-down font-size-18"])[3]')
        self.click_on_list = (By.XPATH,'//ul[@id="VCHCT10-listbox"]//li')
        self.click_on_add_button = (By.XPATH,'//*[@class="btn btn-link text-primary btn-sm"]')

    def organisation_selection(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_organisation_dropdown = wait.until(
            EC.element_to_be_clickable(self.click_on_organisation_drop_down))
        self.driver.execute_script("arguments[0].click();", click_on_organisation_dropdown)

    def click_on_alpha_adarsh(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_alpha_adarsh_organisation_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_alpha_adarsh_organisation))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_alpha_adarsh_organisation_locator).click().perform()
        time.sleep(4)

    def click_on_create_button_element(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_create_button_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_create_button))
        self.driver.execute_script("arguments[0].click();", click_on_create_button_locator)
        time.sleep(3)
        pyautogui.hotkey('alt','a')
        pyautogui.press('r')

    def select_on_receipt_transcation_type(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_receipt_voucher_transcation_type_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_receipt_voucher_transcation_type))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_receipt_voucher_transcation_type_locator).click().perform()
        # select receipt
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_receipt_in_transcation_type_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_receipt_in_transcation_type))
        actions.move_to_element(click_on_receipt_in_transcation_type_locator).click().perform()

    def click_on_Amount_received_from(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_receipt_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_receipt))
        for _ in range(2):
            self.driver.execute_script("arguments[0].click();", click_on_receipt_locator)
            time.sleep(1)
        click_on_Amount_received_from_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_Amount_received_from_drop_down))
        dinesh = ActionChains(self.driver)
        dinesh.move_to_element(click_on_Amount_received_from_drop_down_locator).click().perform()

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(2)
        actions.send_keys(Keys.ESCAPE).perform()
        click_on_Amount_received_from_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_Amount_received_from_drop_down))
        dinesh = ActionChains(self.driver)
        dinesh.move_to_element(click_on_Amount_received_from_drop_down_locator).click().perform()
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_list_lists = wait.until(
            EC.presence_of_all_elements_located(self.click_on_list))
        for i in click_on_list_lists:
            click_on_Amount_received_from_drop_down_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_Amount_received_from_drop_down))
            dinesh = ActionChains(self.driver)
            dinesh.move_to_element(click_on_Amount_received_from_drop_down_locator).click().perform()
            click_on_list_lists = wait.until(
                EC.presence_of_all_elements_located(self.click_on_list))
            i.click()
            click_on_add_button_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_add_button))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_add_button_locator).click().perform()
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(0.5)



            











