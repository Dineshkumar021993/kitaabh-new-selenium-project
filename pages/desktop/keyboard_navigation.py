import time

import pyautogui
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException
import allure


# # utils/logger.py
# import logging
#
# def setup_logger(log_file='test_log.log'):
#     # Set up basic configuration for logging
#     logging.basicConfig(
#         level=logging.INFO,  # Set the logging level
#         format='%(asctime)s - %(levelname)s - %(message)s',
#         handlers=[
#             logging.FileHandler(log_file),  # Log to a file
#             logging.StreamHandler()  # Log to the console
#         ]
#     )
#
# # Function to get the logger
# def get_logger(name):
#     return logging.getLogger(name)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.XPATH, '//input[@id="emailOrPhoneNum"]')
        self.nextbutton_locator = (By.XPATH, '//button[@data-testid="sign-in-verify"]')
        self.password_locator = (By.XPATH, '//input[@id="password"]')
        self.login_button_locator = (By.XPATH, '//button[normalize-space(text())="Sign In"]')

    def enter_username(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        enter_username = wait.until(
            EC.presence_of_element_located(self.username_locator))
        enter_username.send_keys("mahesh.k@lotusinsights.in")
        allure.attach(self.driver.get_screenshot_as_png(), name="EnterUserName",
                      attachment_type=allure.attachment_type.PNG)

    def click_NextButton(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        Click_next_button = wait.until(
            EC.element_to_be_clickable(self.nextbutton_locator))
        self.driver.execute_script("arguments[0].click();", Click_next_button)
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickNextButton",
                      attachment_type=allure.attachment_type.PNG)

    def enter_password(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException,
                                                 TimeoutException])
        enter_password = wait.until(
            EC.presence_of_element_located(self.password_locator))
        enter_password.send_keys("Mahesh@123")
        allure.attach(self.driver.get_screenshot_as_png(), name="EnterPassword",
                      attachment_type=allure.attachment_type.PNG)

    def click_login_button(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        Click_login_button = wait.until(
            EC.element_to_be_clickable(self.login_button_locator))
        self.driver.execute_script("arguments[0].click();", Click_login_button)
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickLoginButton",
                      attachment_type=allure.attachment_type.PNG)
        print("Dinesh..success")


class select_organisation:
    def __init__(self, driver):
        self.driver = driver
        self.organisation_drop_down_click = (
            By.XPATH, '//i[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"]')
        # self.select_organisation = (By.XPATH, '//div[normalize-space(text())="S R MARKETING"]')
        self.select_organisation = (By.XPATH, '//div[normalize-space(text())="Alpha Adarsh"]')
        self.search_organisation_feild = (
            By.XPATH, '//input[@class="p-inputtext p-component form-control h-40px shadow-none select-filter-input"]')

        self.search_feild_ledgers_list = (By.XPATH,
                                          '//input[@class="p-inputtext p-component form-control h-40px shadow-none filter-search-inp figma-bg"]')
        self.click_on_feilds = (By.XPATH,
                                '//button[@class="btn btn-outline-light figma-bg rounded-pill table-vch-card text-color-1 outline-dark-border l-h-23"]')
        self.click_on_all_check_box = (By.XPATH, '(//*[@class="p-checkbox-box"])[1]')
        self.all_check_boxes_in_feilds = (By.XPATH, '//*[@class="p-checkbox p-component"]')
        self.ledger_list = (By.XPATH, '//*[normalize-space(text())="Ledger Name"]//ancestor::thead//following-sibling::tbody//tr//td[1]//p')
        self.click_on_compare_in_summary = (By.XPATH,'//i[@class="fi fi-br-code-compare text-primary font-size-14"]')
        self.click_on_feilds_in_summary = (By.XPATH,'//button[@class="btn btn-outline-light figma-bg font-size-14 rounded-pill table-vch-card text-color-1 outline-dark-border"]//i')
        self.search_feild_in_feilds_in_summary = (By.XPATH,'//input[@class="p-inputtext p-component p-multiselect-filter"]')
        self.show_net_transcations_in_feilds_in_summary = (By.XPATH,'(//*[@class="p-checkbox-box"])[2]')
        self.filter_based_on_percentage_feild = (By.XPATH,'//*[@name="code" or id="FP1"]')
        self.percentage_input_box = (By.XPATH,'//*[@name="percentageInput" or @id="FP2"]')
        self.click_on_monthly_drop_down = (By.XPATH,'(//button[@class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium MuiAutocomplete-popupIndicator css-uge3vf"])[1]')
        self.click_on_transcations = (By.XPATH,'//div[@class="btn-group btn-tabs-list"]//button[3]')
        self.side_panel_list = (By.XPATH, '//div[@class="btn-group btn-tabs-list"]//button')
        self.click_on_aggregates = (By.XPATH,'//button[normalize-space(text())="Aggregates"]')
        self.click_on_balances = (By.XPATH,'//*[normalize-space(text())="Balances"]')
        self.click_on_compare_in_balances = (By.XPATH,'//*[@class="fi fi-br-code-compare text-primary font-size-14"]')
        self.click_on_reports = (By.XPATH,'(//button[@class="btn btn-link btn-sm text-color-3 ps-0 pe-0 me-24"])[5]')
        self.search_feild_in_columnar_feilds_in_reports = (By.XPATH,'//*[@id="ledger-columnar-search-filter"]')

    def select_organisation_element(self):
        actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_organisation_drop_down = wait.until(
            EC.element_to_be_clickable(self.organisation_drop_down_click))
        actions.move_to_element(click_on_organisation_drop_down).click().perform()
        time.sleep(3)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        search_organisation_feild_locator = wait.until(
            EC.presence_of_element_located(self.search_organisation_feild))
        # search_organisation_feild_locator.send_keys("S R MARKETING")
        search_organisation_feild_locator.send_keys("Alpha Adarsh")
        time.sleep(3)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        select_organisation_selection = wait.until(
            EC.element_to_be_clickable(self.select_organisation))
        actions.move_to_element(select_organisation_selection).click().perform()
        time.sleep(2)

        # pyautogui.press('g')
        pyautogui.press('l')
        time.sleep(5)

    def keyboard_navigation_ledgers_list(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        search_feild_ledgers_list_locator = wait.until(
            EC.presence_of_element_located(self.search_feild_ledgers_list))
        if self.driver.switch_to.active_element == search_feild_ledgers_list_locator:
            print("The cursor is already focused on the input field by default.")
        else:
            print("The cursor is not focused on the input field by default.")

        click_on_feilds_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_feilds))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_feilds_locator).click().perform()

        pyautogui.FAILSAFE = False
        # check feilds
        for _ in range(9):
            pyautogui.press('tab')
            time.sleep(0.3)
            time.sleep(2)
            for _ in range(1):
                pyautogui.press('space')
                time.sleep(0.3)
        for _ in range(9):
            pyautogui.press('backspace')
            time.sleep(0.3)
            time.sleep(2)
            for _ in range(1):
                pyautogui.press('space')
                time.sleep(0.3)
        for _ in range(9):
            pyautogui.press('tab')
            time.sleep(0.3)
            time.sleep(2)
            for _ in range(1):
                pyautogui.press('enter')
                time.sleep(0.3)
        for _ in range(9):
            pyautogui.hotkey('shift', 'tab')
            time.sleep(0.3)
            time.sleep(2)
            for _ in range(1):
                pyautogui.press('enter')
                time.sleep(0.3)
        pyautogui.press('esc')

        click_on_all_check_box_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_all_check_box))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_all_check_box_locator).click().perform()
        time.sleep(5)

        all_check_boxes_in_feilds_locator = wait.until(
            EC.presence_of_all_elements_located(self.all_check_boxes_in_feilds))
        for i in range(1, 9):
            # for checkbox in all_check_boxes_in_feilds_locator:
            #     if checkbox.is_selected():
            #         print(f"They are in selected state after clicking main check box")
            #     else:
            #         print("They are not in selected state after clicking main check box")

            if all_check_boxes_in_feilds_locator[i].is_selected():
                print("selected state")
                time.sleep(0.5)
            else:
                print("not in selected state")

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list))
        Element_list = [element.text for element in ledger_list_locator]
        length_of_element_list = len(Element_list)
        time.sleep(2)
        print(len(Element_list))
        time.sleep(1)
        print("Element_list of Ledger List:", Element_list)
        time.sleep(2)
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_elements = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list))
                element = ledger_list_elements[i]
                time.sleep(2)
                actions.move_to_element(element).click().perform()
                time.sleep(4)
                # ledger_list_locator = wait.until(
                #     EC.presence_of_all_elements_located(self.ledger_list))
                # for i in ledger_list_locator:
                #     ledger_list_locator = wait.until(
                #         EC.presence_of_all_elements_located(self.ledger_list))
                #     try:
                #         i.click()

                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
                for _ in range(5):
                    pyautogui.press('down')
                    time.sleep(0.5)
                for _ in range(5):
                    pyautogui.press('up')
                    time.sleep(1)
                time.sleep(2)
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
                time.sleep(1.5)
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
                time.sleep(1.5)
                actions.send_keys(Keys.ARROW_DOWN).perform()
                for _ in range(3):
                    pyautogui.press('enter')
                    time.sleep(1)
                    pyautogui.press('esc')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                time.sleep(3)
                # feilds in summary
                click_on_feilds_in_summary_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_feilds_in_summary))
                actions.move_to_element(click_on_feilds_in_summary_locator).click().perform()
                # search  feild in summary
                search_feild_in_feilds_in_summary_locator = wait.until(
                    EC.presence_of_element_located(self.search_feild_in_feilds_in_summary))
                if self.driver.switch_to.active_element == search_feild_in_feilds_in_summary_locator:
                    print("The cursor is already focused on the input field by default.")
                else:
                    print("The cursor is not focused on the input field by default.")
                # click check box in feilds
                show_net_transcations_in_feilds_in_summary_locator = wait.until(
                    EC.element_to_be_clickable(self.show_net_transcations_in_feilds_in_summary))
                actions.move_to_element(show_net_transcations_in_feilds_in_summary_locator).click().perform()

                actions.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(1)
                actions.send_keys(Keys.SPACE).perform()
                time.sleep(1)
                actions.send_keys(Keys.ARROW_UP).perform()
                time.sleep(1)
                actions.send_keys(Keys.SPACE).perform()
                time.sleep(1)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(1)
                # equals dropdown
                # filter based on percentage
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                filter_based_on_percentage_feild_locator = wait.until(
                    EC.presence_of_element_located(self.filter_based_on_percentage_feild))
                if self.driver.switch_to.active_element == filter_based_on_percentage_feild_locator:
                    print("The cursor is already focused on the input field by default.")
                else:
                    print("The cursor is not focused on the input field by default.")
                for _ in range(4):
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1)
                for _ in range(4):
                    actions.send_keys(Keys.ARROW_UP).perform()
                    time.sleep(1)
                actions.send_keys(Keys.TAB).perform()

                # filter based on percentage
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                percentage_input_box_locator = wait.until(
                    EC.presence_of_element_located(self.percentage_input_box))
                if self.driver.switch_to.active_element == percentage_input_box_locator:
                    print("The cursor is already focused on the input field by default.")
                else:
                    print("The cursor is not focused on the input field by default.")

                # compare in summary
                click_on_compare_in_summary_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_compare_in_summary))
                actions.move_to_element(click_on_compare_in_summary_locator).click().perform()
                # organisation name
                for _ in range(5):
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1)
                for _ in range(5):
                    actions.send_keys(Keys.ARROW_UP).perform()
                    time.sleep(1)
                actions.send_keys(Keys.TAB).perform()
                time.sleep(1)
                for _ in range(5):
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1)
                for _ in range(5):
                    actions.send_keys(Keys.ARROW_UP).perform()
                    time.sleep(1)

                actions.send_keys(Keys.TAB).perform()
                time.sleep(1)
                actions.send_keys(Keys.TAB).perform()
                time.sleep(1)
                actions.send_keys(Keys.BACKSPACE).perform()
                time.sleep(1)
                actions.send_keys(Keys.ENTER).perform()
                time.sleep(1)
                # monthly drop down
                click_on_monthly_drop_down_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_monthly_drop_down))
                actions.move_to_element(click_on_monthly_drop_down_locator).click().perform()
                time.sleep(1)
                for _ in range(2):
                    actions.send_keys(Keys.ARROW_UP).perform()
                    time.sleep(1.5)
                for _ in range(2):
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1.5)
                for _ in range(2):
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1.5)
                for _ in range(5):
                    actions.send_keys(Keys.ARROW_UP).perform()
                    time.sleep(1.5)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(1)
                # transcations
                click_on_transcations_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_transcations))
                actions.move_to_element(click_on_transcations_locator).click().perform()
                for _ in range(5):
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1.5)
                for _ in range(5):
                    actions.send_keys(Keys.ARROW_UP).perform()
                    time.sleep(1.5)
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
                time.sleep(1.5)
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
                time.sleep(1.5)
                for _ in range(3):
                    for _ in range(2):
                        actions.send_keys(Keys.ENTER).perform()
                        time.sleep(1.5)
                    for _ in range(2):
                        actions.send_keys(Keys.ESCAPE).perform()
                        time.sleep(1.5)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1.5)
                # balances
                # actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
                click_on_balances_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_balances))
                actions.move_to_element(click_on_balances_locator).click().perform()
                time.sleep(3)
                # click on compare in balances
                click_on_balances_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_compare_in_balances))
                actions.move_to_element(click_on_balances_locator).click().perform()
                # self.driver.execute_script("arguments[0].click();", click_on_balances_locator)
                time.sleep(3)
                # In compare organisation drop down
                for _ in range(5):
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                for _ in range(5):
                    actions.send_keys(Keys.ARROW_UP).perform()
                    time.sleep(1.5)
                actions.send_keys(Keys.ENTER).perform()
                time.sleep(2)
                for _ in range(5):
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                for _ in range(5):
                    actions.send_keys(Keys.ARROW_UP).perform()
                time.sleep(1)
                for _ in range(2):
                    actions.send_keys(Keys.TAB).perform()
                    time.sleep(1)
                for _ in range(2):
                    actions.send_keys(Keys.BACKSPACE).perform()
                    time.sleep(1)
                actions.send_keys(Keys.ENTER).perform()
                time.sleep(1.5)
                actions.send_keys(Keys.ESCAPE).perform()
                # aggregates
                click_on_aggregates_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_aggregates))
                self.driver.execute_script("arguments[0].click();", click_on_aggregates_locator)
                # actions.move_to_element(click_on_aggregates_locator).click().perform()
                # actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
                time.sleep(1)
                for _ in range(4):
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1.5)
                for _ in range(4):
                    actions.send_keys(Keys.ARROW_UP).perform()
                    time.sleep(1.5)
                for _ in range(3):
                    for _ in range(3):
                        actions.send_keys(Keys.ENTER).perform()
                        time.sleep(1.5)
                    for _ in range(3):
                        actions.send_keys(Keys.ESCAPE).perform()
                        time.sleep(1.5)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1.5)
                time.sleep(2)
                # reports
                click_on_reports_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_reports))
                actions.move_to_element(click_on_reports_locator).click().perform()
                time.sleep(1.5)
                # columnar report
                actions.send_keys(Keys.ENTER).perform()
                time.sleep(1)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                search_feild_in_columnar_feilds_in_reports_locator = wait.until(
                    EC.presence_of_element_located(self.search_feild_in_columnar_feilds_in_reports))

                if self.driver.switch_to.active_element == search_feild_in_columnar_feilds_in_reports_locator:
                    print("The cursor is already focused on the input field by default.")
                else:
                    print("The cursor is not focused on the input field by default.")
                # actions.send_keys(Keys.ENTER).perform()
                time.sleep(1)
                for _ in range(4):
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1.5)
                for _ in range(4):
                    actions.send_keys(Keys.ARROW_UP).perform()
                    time.sleep(1.5)
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
                time.sleep(1.5)
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
                time.sleep(1.5)
                for _ in range(2):
                    actions.send_keys(Keys.ESCAPE).perform()
                    time.sleep(1)
                time.sleep(3)
            # actions.send_keys(Keys.ARROW_DOWN).perform()
            # time.sleep(1)
            except (StaleElementReferenceException,ElementClickInterceptedException,TimeoutException,AttributeError):
                pass



































