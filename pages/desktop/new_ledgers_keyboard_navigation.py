import time

import pyautogui
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException, MoveTargetOutOfBoundsException
import allure
# utils/logger.py
import logging


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
        Enter_username = wait.until(
            EC.presence_of_element_located(self.username_locator))
        Enter_username.send_keys("mahesh.k@lotusinsights.in")

    def click_NextButton(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        Click_next_button = wait.until(
            EC.element_to_be_clickable(self.nextbutton_locator))
        self.driver.execute_script("arguments[0].click();", Click_next_button)

    def enter_password(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException,
                                                 TimeoutException])
        Enter_password = wait.until(
            EC.presence_of_element_located(self.password_locator))
        Enter_password.send_keys("Mahesh@123")

    def click_login_button(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
        Click_login_button = wait.until(
            EC.element_to_be_clickable(self.login_button_locator))
        self.driver.execute_script("arguments[0].click();", Click_login_button)
        print("Dinesh..success")


class LedgersListKeyBoardNavigation:
    def __init__(self, driver):
        self.driver = driver
        self.search_feild_ledgers_list = (By.XPATH,
                                          '//input[@class="p-inputtext p-component form-control h-40px shadow-none filter-search-inp figma-bg"]')
        self.ledger_list_10 = (
            By.XPATH,
            '//*[normalize-space(text())="Ledger Name"]//ancestor::thead//following-sibling::tbody//tr//td[1]//p')
        self.click_on_10_element = (By.XPATH, '(//*[@class="btn-p text-start text-primary mb-0 overflow-elipsis"])[10]')
        self.click_on_side_arrow = (By.XPATH, '//span[@class="p-paginator-icon pi pi-angle-right"]')
        self.click_on_first_element = (
            By.XPATH, '(//*[@class="btn-p text-start text-primary mb-0 overflow-elipsis"])[1]')
        self.click_on_20_drop_down = (
            By.XPATH, '//span[@class="p-dropdown-trigger-icon p-clickable pi pi-chevron-down"]')
        self.click_on_actual_drop_down_20 = (By.XPATH, '(//li[@class="p-dropdown-item"])[1]')
        self.click_on_actual_drop_down_50 = (By.XPATH, '(//li[@class="p-dropdown-item"])[2]')
        self.click_on_transcations_elements_inside_drop_down = (
            By.XPATH, '(//tbody[@class="p-datatable-tbody"])[2]//tr//td[2]')
        self.ledger_list = (
            By.XPATH,
            '//*[normalize-space(text())="Ledger Name"]//ancestor::thead//following-sibling::tbody//tr//td[1]//p')
        # self.setup_logger()

    # def setup_logger(self, driver, log_file='test_log.log'):
    #     # Set up basic configuration for logging
    #     logging.basicConfig(
    #         level=logging.INFO,  # Set the logging level
    #         format='%(asctime)s - %(levelname)s - %(message)s',
    #         handlers=[
    #             logging.FileHandler(log_file),  # Log to a file
    #             logging.StreamHandler()  # Log to the console
    #         ]
    #     )
    #     self.logger = logging.getLogger(__name__)

    def ledgers_list(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        search_feild_ledgers_list_locator = wait.until(
            EC.presence_of_element_located(self.search_feild_ledgers_list))
        allure.attach(self.driver.get_screenshot_as_png(), name='search',
                      attachment_type=allure.attachment_type.PNG)
        if self.driver.switch_to.active_element == search_feild_ledgers_list_locator:
            print("The cursor is already focused on the input field by default.")
        else:
            print("The cursor is not focused on the input field by default.")

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_10_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list_10))
        Element_list = [element.text for element in ledger_list_10_locator]
        length_of_element_list = len(Element_list)
        time.sleep(2)
        print(len(Element_list))
        time.sleep(1)
        print("Element_list of Ledger List 10:", Element_list)
        time.sleep(2)
        # ctrl down
        # self.logger.info("Opening the login page")
        # logging.FileHandler('D:\\NewSeleniumProject\\pages\\desktop\\logs.py')
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name='ControlDown',
                      attachment_type=allure.attachment_type.PNG)
        # ctrl up
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name='ControlUp',
                      attachment_type=allure.attachment_type.PNG)
        for i in range(length_of_element_list):
            print("index is:", i)
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list_10))
                element = ledger_list_10_locator[i]
                text = element.text
                print(text)
                actions.send_keys(Keys.ARROW_DOWN).perform()
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                # self.logger.error("StaleElementReferenceException caught.")
                pass
        # Arrow up
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list_10))
                element = ledger_list_10_locator[i]
                text = element.text
                print(text)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_UP).perform()
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                pass

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_10_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list_10))

        for j in enumerate(ledger_list_10_locator):
            print(j)
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_side_arrow_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_side_arrow))
                actions = ActionChains(self.driver)
                actions.move_to_element(click_on_side_arrow_locator).click().perform()

                # Ctrl + Arrow Down
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), name='CtrlDown',
                              attachment_type=allure.attachment_type.PNG)

                # Ctrl + Arrow Up
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), name='CtrlUp',
                              attachment_type=allure.attachment_type.PNG)

                for i in range(length_of_element_list):
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledger_list_10_locator = wait.until(
                        EC.presence_of_all_elements_located(self.ledger_list_10))
                    element = ledger_list_10_locator[i]
                    text = element.text
                    print(text)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDownAll',
                                  attachment_type=allure.attachment_type.PNG)
                # Move back up
                for k in range(length_of_element_list):
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledger_list_10_locator = wait.until(
                        EC.presence_of_all_elements_located(self.ledger_list_10))

                    element = ledger_list_10_locator[k]
                    text = element.text
                    print(text)
                    actions.send_keys(Keys.ARROW_UP).perform()
                    allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUpAll',
                                  attachment_type=allure.attachment_type.PNG)
            except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
                pass

        # Send Home key action
        actions.send_keys(Keys.HOME).perform()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='HomeButton',
                      attachment_type=allure.attachment_type.PNG)

    def ledgers_list_10_1(self):
        # for 1
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_10_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list_10))
        Element_list = [element.text for element in ledger_list_10_locator]
        length_of_element_list = len(Element_list)
        time.sleep(2)
        print(len(Element_list))
        time.sleep(1)
        print("Element_list of Ledger List 10:", Element_list)
        time.sleep(2)

        # ctrl down
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name='ctrlArrowDown',
                      attachment_type=allure.attachment_type.PNG)

        # ctrl up
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name='ctrlArrowUp',
                      attachment_type=allure.attachment_type.PNG)

        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list_10))
                element = ledger_list_10_locator[i]
                text = element.text
                print(text)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                pass

        # Arrow up
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list_10))
                element = ledger_list_10_locator[i]
                text = element.text
                print(text)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_UP).perform()
                time.sleep(1.5)
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                pass

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_10_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list_10))
        try:
            for j in enumerate(ledger_list_10_locator):
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_side_arrow_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_side_arrow))
                # Scroll to the button before clicking to ensure it's in view
                self.driver.execute_script("arguments[0].scrollIntoView();", click_on_side_arrow_locator)
                actions = ActionChains(self.driver)
                actions.move_to_element(click_on_side_arrow_locator).click().perform()
                # ctrl down
                actions = ActionChains(self.driver)
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
                time.sleep(2)
                allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowDown',
                              attachment_type=allure.attachment_type.PNG)
                # ctrl up
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
                time.sleep(2)
                allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowUp',
                              attachment_type=allure.attachment_type.PNG)
                for s in range(length_of_element_list):
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledger_list_10_locator = wait.until(
                        EC.presence_of_all_elements_located(self.ledger_list_10))
                    element = ledger_list_10_locator[s]
                    text = element.text
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                                  attachment_type=allure.attachment_type.PNG)

                for k in range(length_of_element_list):
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledger_list_10_locator = wait.until(
                        EC.presence_of_all_elements_located(self.ledger_list_10))
                    element = ledger_list_10_locator[k]
                    text = element.text
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_UP).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                                  attachment_type=allure.attachment_type.PNG)
        except (StaleElementReferenceException, MoveTargetOutOfBoundsException) as e:
            print(f"Exception occurred: {e}")
            pass
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.HOME).perform()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='HomePage',
                      attachment_type=allure.attachment_type.PNG)

    def ledgers_list_20(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_20_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_20_drop_down))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_20_drop_down_locator).click().perform()
        allure.attach(self.driver.get_screenshot_as_png(), name='Ledger20DropDown',
                      attachment_type=allure.attachment_type.PNG)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_actual_drop_down_20_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_actual_drop_down_20))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_actual_drop_down_20_locator).click().perform()
        allure.attach(self.driver.get_screenshot_as_png(), name='Ledger20DropDownLick',
                      attachment_type=allure.attachment_type.PNG)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_10_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list_10))
        Element_list = [element.text for element in ledger_list_10_locator]
        length_of_element_list = len(Element_list)
        time.sleep(2)
        print(len(Element_list))
        time.sleep(1)
        print("Element_list of Ledger List 10:", Element_list)
        time.sleep(2)
        # ctrl down
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowDown',
                      attachment_type=allure.attachment_type.PNG)
        # ctrl up
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowUp',
                      attachment_type=allure.attachment_type.PNG)
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list_10))
                element = ledger_list_10_locator[i]
                text = element.text
                print(text)
                actions.send_keys(Keys.ARROW_DOWN).perform()
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                pass
        # Arrow up
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list_10))
                element = ledger_list_10_locator[i]
                text = element.text
                print(text)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_UP).perform()
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                pass
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_10_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list_10))
        for _ in enumerate(ledger_list_10_locator):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_side_arrow_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_side_arrow))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_side_arrow_locator).click().perform()
            # ctrl down
            actions = ActionChains(self.driver)
            actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
            time.sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowDown',
                          attachment_type=allure.attachment_type.PNG)
            # ctrl up
            actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
            time.sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowUp',
                          attachment_type=allure.attachment_type.PNG)
            for i in range(length_of_element_list):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledger_list_10_locator = wait.until(
                        EC.presence_of_all_elements_located(self.ledger_list_10))
                    element = ledger_list_10_locator[i]
                    text = element.text
                    print(text)
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                                  attachment_type=allure.attachment_type.PNG)
                except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
                    pass
            for k in range(length_of_element_list):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledger_list_10_locator = wait.until(
                        EC.presence_of_all_elements_located(self.ledger_list_10))
                    element = ledger_list_10_locator[k]
                    text = element.text
                    print(text)
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_UP).perform()
                    allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                                  attachment_type=allure.attachment_type.PNG)
                except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
                    pass
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.HOME).perform()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='Home',
                      attachment_type=allure.attachment_type.PNG)

    def ledgers_list_20_1_sec(self):
        # for 1
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_10_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list_10))
        Element_list = [element.text for element in ledger_list_10_locator]
        length_of_element_list = len(Element_list)
        time.sleep(2)
        print(len(Element_list))
        time.sleep(1)
        print("Element_list of Ledger List 10:", Element_list)
        time.sleep(2)
        # ctrl down
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowDown',
                      attachment_type=allure.attachment_type.PNG)
        # ctrl up
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowUP',
                      attachment_type=allure.attachment_type.PNG)
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list_10))
                element = ledger_list_10_locator[i]
                text = element.text
                print(text)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                pass
        # Arrow up
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list_10))
                element = ledger_list_10_locator[i]
                text = element.text
                print(text)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_UP).perform()
                time.sleep(1.5)
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                pass
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_10_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list_10))
        for _ in enumerate(ledger_list_10_locator):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_side_arrow_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_side_arrow))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_side_arrow_locator).click().perform()
            # ctrl down
            actions = ActionChains(self.driver)
            actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowUp',
                          attachment_type=allure.attachment_type.PNG)
            # ctrl up
            actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowDown',
                          attachment_type=allure.attachment_type.PNG)
            for i in range(length_of_element_list):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledger_list_10_locator = wait.until(
                        EC.presence_of_all_elements_located(self.ledger_list_10))
                    element = ledger_list_10_locator[i]
                    text = element.text
                    print(text)
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                                  attachment_type=allure.attachment_type.PNG)
                except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
                    pass
            for k in range(length_of_element_list):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledger_list_10_locator = wait.until(
                        EC.presence_of_all_elements_located(self.ledger_list_10))
                    element = ledger_list_10_locator[k]
                    text = element.text
                    print(text)
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_UP).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                                  attachment_type=allure.attachment_type.PNG)
                except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
                    pass
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.HOME).perform()
        time.sleep(2)

    def ledgers_list_50(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_20_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_20_drop_down))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_20_drop_down_locator).click().perform()
        allure.attach(self.driver.get_screenshot_as_png(), name='DropdownClickfor50',
                      attachment_type=allure.attachment_type.PNG)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_actual_drop_down_20_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_actual_drop_down_50))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_actual_drop_down_20_locator).click().perform()
        allure.attach(self.driver.get_screenshot_as_png(), name='ClickOn50',
                      attachment_type=allure.attachment_type.PNG)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_10_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list_10))
        Element_list = [element.text for element in ledger_list_10_locator]
        length_of_element_list = len(Element_list)
        time.sleep(2)
        print(len(Element_list))
        time.sleep(1)
        print("Element_list of Ledger List 10:", Element_list)
        time.sleep(2)
        # ctrl down
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                      attachment_type=allure.attachment_type.PNG)
        # ctrl up
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUP',
                      attachment_type=allure.attachment_type.PNG)
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list_10))
                element = ledger_list_10_locator[i]
                text = element.text
                print(text)
                actions.send_keys(Keys.ARROW_DOWN).perform()
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                pass
        # Arrow up
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list_10))
                element = ledger_list_10_locator[i]
                text = element.text
                print(text)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_UP).perform()
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                pass
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_10_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list_10))
        for _ in enumerate(ledger_list_10_locator):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_side_arrow_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_side_arrow))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_side_arrow_locator).click().perform()
            # ctrl down
            actions = ActionChains(self.driver)
            actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
            time.sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowUp',
                          attachment_type=allure.attachment_type.PNG)
            # ctrl up
            actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
            time.sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowUp',
                          attachment_type=allure.attachment_type.PNG)
            for i in range(length_of_element_list):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledger_list_10_locator = wait.until(
                        EC.presence_of_all_elements_located(self.ledger_list_10))
                    element = ledger_list_10_locator[i]
                    text = element.text
                    print(text)
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                                  attachment_type=allure.attachment_type.PNG)
                except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
                    pass
            for k in range(length_of_element_list):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledger_list_10_locator = wait.until(
                        EC.presence_of_all_elements_located(self.ledger_list_10))
                    element = ledger_list_10_locator[k]
                    text = element.text
                    print(text)
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_UP).perform()
                    allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                                  attachment_type=allure.attachment_type.PNG)
                except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
                    pass
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.HOME).perform()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='Home',
                      attachment_type=allure.attachment_type.PNG)

    def ledgers_list_50_1_sec(self):
        # for 1
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_10_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list_10))
        Element_list = [element.text for element in ledger_list_10_locator]
        length_of_element_list = len(Element_list)
        time.sleep(2)
        print(len(Element_list))
        time.sleep(1)
        print("Element_list of Ledger List 10:", Element_list)
        time.sleep(2)
        # ctrl down
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowDown',
                      attachment_type=allure.attachment_type.PNG)
        # ctrl up
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
        time.sleep(1)
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list_10))
                element = ledger_list_10_locator[i]
                text = element.text
                print(text)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                pass
        # Arrow up
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list_10))
                element = ledger_list_10_locator[i]
                text = element.text
                print(text)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_UP).perform()
                time.sleep(1.5)
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                pass
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_10_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list_10))
        for _ in enumerate(ledger_list_10_locator):
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_side_arrow_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_side_arrow))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_side_arrow_locator).click().perform()
            # ctrl down
            actions = ActionChains(self.driver)
            actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowDown',
                          attachment_type=allure.attachment_type.PNG)
            # ctrl up
            actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowUp',
                          attachment_type=allure.attachment_type.PNG)
            for i in range(length_of_element_list):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledger_list_10_locator = wait.until(
                        EC.presence_of_all_elements_located(self.ledger_list_10))
                    element = ledger_list_10_locator[i]
                    text = element.text
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                                  attachment_type=allure.attachment_type.PNG)
                except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
                    pass
            for k in range(length_of_element_list):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledger_list_10_locator = wait.until(
                        EC.presence_of_all_elements_located(self.ledger_list_10))
                    element = ledger_list_10_locator[k]
                    text = element.text
                    print(text)
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_UP).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                                  attachment_type=allure.attachment_type.PNG)
                except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
                    pass
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.HOME).perform()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='Home',
                      attachment_type=allure.attachment_type.PNG)


class Transcations:
    def __init__(self, driver):
        self.driver = driver
        self.click_on_transcations_elements_inside_drop_down = (
            By.XPATH, '(//tbody[@class="p-datatable-tbody"])[2]//tr//td[2]')
        self.ledger_list = (
            By.XPATH,
            '//*[normalize-space(text())="Ledger Name"]//ancestor::thead//following-sibling::tbody//tr//td[1]//p')
        self.click_on_aggregates_list_inside_side_panel = (
            By.XPATH, '(//tbody[@class="p-datatable-tbody"])[2]//tr//td[2]')
        # self.list_of_aggregates_inside_inside_panel = (By.XPATH,'(//tbody[@class="p-datatable-tbody"])[2]//tr//td[2]')
        self.list_of_aggregates_inside_inside_panel = (By.XPATH,'(//*[normalize-space(text())="Voucher Date"])[1]//ancestor::thead//following-sibling::tbody//tr//td[2]')

    def transcations(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_10_locator = wait.until(
            EC.presence_of_all_elements_located(self.ledger_list))
        Element_list = [element.text for element in ledger_list_10_locator]
        length_of_element_list = len(Element_list)
        time.sleep(2)
        print(len(Element_list))
        time.sleep(1)
        print("Element_list of Ledger List 10:", Element_list)
        time.sleep(2)
        for i in range(length_of_element_list):
            print("index is:", i)
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_elements = wait.until(
                    EC.presence_of_all_elements_located(self.ledger_list))
                element = ledger_list_elements[i]
                time.sleep(2)
                # element.send_keys(Keys.ENTER)
                actions = ActionChains(self.driver)
                # actions.move_to_element(element).click().perform()
                # element.click()
                self.driver.execute_script("arguments[0].click();", element)
                time.sleep(2)
                allure.attach(self.driver.get_screenshot_as_png(), name='Transcations',
                              attachment_type=allure.attachment_type.PNG)
                actions.key_down(Keys.ALT).send_keys('e').key_up(Keys.ALT).perform()
                time.sleep(2)
                allure.attach(self.driver.get_screenshot_as_png(), name='alt+e',
                              attachment_type=allure.attachment_type.PNG)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                # ctrl right
                for _ in range(2):
                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='controlArrowRight',
                                  attachment_type=allure.attachment_type.PNG)
                for _ in range(2):
                    # ctrl left
                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_LEFT).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowLeft',
                                  attachment_type=allure.attachment_type.PNG)
                for _ in range(2):
                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='controlArrowRight',
                                  attachment_type=allure.attachment_type.PNG)

                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_transcations_elements_inside_drop_down_locator = wait.until(
                    EC.presence_of_all_elements_located(self.click_on_transcations_elements_inside_drop_down))
                Element_list_transcations = [element.text for element in
                                             click_on_transcations_elements_inside_drop_down_locator]
                length_of_element_list_transcations = len(Element_list_transcations)
                time.sleep(2)
                print(len(Element_list_transcations))
                time.sleep(1)
                print("Element_list:", Element_list_transcations)
                time.sleep(2)
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowDown',
                              attachment_type=allure.attachment_type.PNG)
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowUp',
                              attachment_type=allure.attachment_type.PNG)
                for k in range(length_of_element_list_transcations):
                    try:
                        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                        click_on_transcations_elements_inside_drop_down_locator = wait.until(
                            EC.presence_of_all_elements_located(self.click_on_transcations_elements_inside_drop_down))
                        element = click_on_transcations_elements_inside_drop_down_locator[k]
                        text = element.text
                        print(text)
                        actions.send_keys(Keys.ARROW_DOWN).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                                      attachment_type=allure.attachment_type.PNG)
                    except (StaleElementReferenceException, TimeoutException):
                        pass

                # Arrow up
                for j in range(length_of_element_list_transcations):
                    try:
                        click_on_transcations_elements_inside_drop_down_locator = wait.until(
                            EC.presence_of_all_elements_located(self.click_on_transcations_elements_inside_drop_down))
                        element = click_on_transcations_elements_inside_drop_down_locator[j]
                        text = element.text
                        print(text)
                        actions = ActionChains(self.driver)
                        actions.send_keys(Keys.ARROW_UP).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                                      attachment_type=allure.attachment_type.PNG)
                    except (StaleElementReferenceException, TimeoutException):
                        pass

                for p in range(length_of_element_list_transcations):
                    try:
                        click_on_transcations_elements_inside_drop_down_locator = wait.until(
                            EC.presence_of_all_elements_located(
                                self.click_on_transcations_elements_inside_drop_down))
                        element = click_on_transcations_elements_inside_drop_down_locator[p]
                        text = element.text
                        print(text)
                        for _ in range(2):
                            actions.send_keys(Keys.ENTER).perform()
                            time.sleep(2)
                            allure.attach(self.driver.get_screenshot_as_png(), name='InsideTranscation',
                                          attachment_type=allure.attachment_type.PNG)
                        actions.send_keys(Keys.ESCAPE).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='Escape',
                                      attachment_type=allure.attachment_type.PNG)
                        time.sleep(1)
                        # for alt+ enter
                        actions.key_down(Keys.ALT).send_keys(Keys.ENTER).key_up(Keys.ALT).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='Edit',
                                      attachment_type=allure.attachment_type.PNG)
                        time.sleep(1)
                        actions.send_keys(Keys.ESCAPE).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='Escape',
                                      attachment_type=allure.attachment_type.PNG)
                        actions.send_keys(Keys.ARROW_DOWN).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                                      attachment_type=allure.attachment_type.PNG)
                        time.sleep(1)
                        actions.send_keys(Keys.ENTER).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='Enter',
                                      attachment_type=allure.attachment_type.PNG)
                        time.sleep(1)
                        actions.send_keys(Keys.ESCAPE).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='Escape',
                                      attachment_type=allure.attachment_type.PNG)
                        actions.key_down(Keys.ALT).send_keys('e').key_up(Keys.ALT).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='Alt+e(edit)',
                                      attachment_type=allure.attachment_type.PNG)
                        actions.send_keys(Keys.ESCAPE).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='Escape',
                                      attachment_type=allure.attachment_type.PNG)
                        actions.send_keys(Keys.ESCAPE).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='Escape',
                                      attachment_type=allure.attachment_type.PNG)
                        actions.send_keys(Keys.ARROW_DOWN).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                                      attachment_type=allure.attachment_type.PNG)
                    except (StaleElementReferenceException, TimeoutException):
                        pass
                time.sleep(2)
                # Aggregates screen
                for _ in range(2):
                    actions = ActionChains(self.driver)
                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowRight',
                                  attachment_type=allure.attachment_type.PNG)
                for _ in range(2):
                    # ctrl left
                    actions = ActionChains(self.driver)
                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_LEFT).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowLeft',
                                  attachment_type=allure.attachment_type.PNG)
                for _ in range(2):
                    actions = ActionChains(self.driver)
                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowRight',
                                  attachment_type=allure.attachment_type.PNG)

                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_aggregates_list_inside_side_panel_locator = wait.until(
                    EC.presence_of_all_elements_located(self.click_on_aggregates_list_inside_side_panel))
                Element_list_aggregates = [element.text for element in
                                           click_on_aggregates_list_inside_side_panel_locator]
                length_of_element_list_aggregates = len(Element_list_aggregates)
                time.sleep(2)
                print(len(Element_list_aggregates))
                time.sleep(1)
                print("Element_list_of_aggregates:", Element_list_aggregates)
                time.sleep(2)
                actions = ActionChains(self.driver)
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowDown',
                              attachment_type=allure.attachment_type.PNG)
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowUp',
                              attachment_type=allure.attachment_type.PNG)
                for j in range(length_of_element_list_aggregates):
                    try:
                        click_on_transcations_elements_inside_drop_down_locator = wait.until(
                            EC.presence_of_all_elements_located(
                                self.click_on_aggregates_list_inside_side_panel))
                        element = click_on_transcations_elements_inside_drop_down_locator[j]
                        text = element.text
                        actions = ActionChains(self.driver)
                        actions.send_keys(Keys.ARROW_DOWN).perform()
                        allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                                      attachment_type=allure.attachment_type.PNG)
                    except (StaleElementReferenceException, TimeoutException):
                        pass

                for k in range(length_of_element_list_aggregates):
                    try:
                        click_on_transcations_elements_inside_drop_down_locator = wait.until(
                            EC.presence_of_all_elements_located(
                                self.click_on_aggregates_list_inside_side_panel))
                        element = click_on_transcations_elements_inside_drop_down_locator[k]
                        text = element.text
                        actions = ActionChains(self.driver)
                        actions.send_keys(Keys.ARROW_UP).perform()
                        allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                                      attachment_type=allure.attachment_type.PNG)
                    except (StaleElementReferenceException, TimeoutException):
                        pass

                for s in range(length_of_element_list_aggregates):
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ENTER).perform()
                    list_of_aggregates_inside_inside_panel_locator = wait.until(
                        EC.presence_of_all_elements_located(self.list_of_aggregates_inside_inside_panel))
                    Element_list_inside_aggregates = [element.text for element in
                                                      list_of_aggregates_inside_inside_panel_locator]
                    length_of_element_list_aggregates_inner_loop = len(Element_list_inside_aggregates)
                    time.sleep(2)
                    print(len(Element_list_inside_aggregates))
                    time.sleep(1)
                    print("Element_list :", Element_list_inside_aggregates)
                    time.sleep(2)
                    actions = ActionChains(self.driver)
                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowDown',
                                  attachment_type=allure.attachment_type.PNG)
                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                    allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowUp',
                                  attachment_type=allure.attachment_type.PNG)
                    for j in range(length_of_element_list_aggregates_inner_loop):
                        try:
                            click_on_aggregates_list_inside_side_panel_locator = wait.until(
                                EC.presence_of_all_elements_located(
                                    self.list_of_aggregates_inside_inside_panel))
                            element = click_on_aggregates_list_inside_side_panel_locator[j]
                            text = element.text
                            actions = ActionChains(self.driver)
                            actions.send_keys(Keys.ARROW_DOWN).perform()
                            allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                                          attachment_type=allure.attachment_type.PNG)
                        except (StaleElementReferenceException, TimeoutException):
                            pass

                    for k in range(length_of_element_list_aggregates_inner_loop):
                        click_on_aggregates_list_inside_side_panel_locator = wait.until(
                            EC.presence_of_all_elements_located(
                                self.list_of_aggregates_inside_inside_panel))
                        element = click_on_aggregates_list_inside_side_panel_locator[k]
                        print(element)
                        pyautogui.press('up')
                        allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                                      attachment_type=allure.attachment_type.PNG)

                    for z in range(length_of_element_list_aggregates_inner_loop):
                        click_on_aggregates_list_inside_side_panel_dropdown = wait.until(
                            EC.presence_of_all_elements_located(self.click_on_aggregates_list_inside_side_panel))
                        element = click_on_aggregates_list_inside_side_panel_dropdown[z]
                        actions.move_to_element(element).click().perform()
                        time.sleep(2)
                        for _ in range(5):
                            actions.send_keys(Keys.ARROW_DOWN).perform()
                            time.sleep(1)
                            allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                                          attachment_type=allure.attachment_type.PNG)
                        for _ in range(5):
                            actions.send_keys(Keys.ARROW_UP).perform()
                            time.sleep(1)
                            allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                                          attachment_type=allure.attachment_type.PNG)
                        for _ in range(2):
                            actions.send_keys(Keys.ENTER).perform()
                            time.sleep(1)
                            allure.attach(self.driver.get_screenshot_as_png(), name='Enter',
                                          attachment_type=allure.attachment_type.PNG)
                            actions.send_keys(Keys.ESCAPE).perform()
                            time.sleep(1)
                        actions.send_keys(Keys.ARROW_DOWN).perform()
                        time.sleep(1)
                        allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                                      attachment_type=allure.attachment_type.PNG)
                        actions.send_keys(Keys.ENTER).perform()
                        time.sleep(1)
                        allure.attach(self.driver.get_screenshot_as_png(), name='Enter',
                                      attachment_type=allure.attachment_type.PNG)
                        actions.send_keys(Keys.ESCAPE).perform()
                        time.sleep(1)
                        allure.attach(self.driver.get_screenshot_as_png(), name='Escape',
                                      attachment_type=allure.attachment_type.PNG)
                        # alt + e -- edit
                        actions.key_down(Keys.ALT).send_keys('e').key_up(Keys.ALT).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='Alt+e--edit',
                                      attachment_type=allure.attachment_type.PNG)
                        actions.send_keys(Keys.ESCAPE).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='Escape',
                                      attachment_type=allure.attachment_type.PNG)
                        # alt + enter
                        actions.key_down(Keys.ALT).send_keys(Keys.ENTER).key_up(Keys.ALT).perform()
                        time.sleep(2)
                        allure.attach(self.driver.get_screenshot_as_png(), name='alt+enter',
                                      attachment_type=allure.attachment_type.PNG)
                        for _ in range(2):
                            actions.send_keys(Keys.ESCAPE).perform()
                            time.sleep(2)
                            allure.attach(self.driver.get_screenshot_as_png(), name='ToMainPage',
                                          attachment_type=allure.attachment_type.PNG)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                actions.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(1)
            except (ElementClickInterceptedException, TimeoutException,IndexError):
                pass
