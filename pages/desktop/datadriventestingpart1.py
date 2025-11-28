from openpyxl.reader.excel import load_workbook
from openpyxl.styles import PatternFill
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import time
from pages.desktop import XLUtils  # Importing the Excel utility file
from selenium.webdriver import ActionChains, Keys

path = "C:\\Users\\Dinesh\\Documents\\datadriventestinglogin.xlsx"

# result_column = None
# column_1 = None
# column_2 = None
# sheet_name = None
# passed_case = None
# failed_case = None


# def set_values(row_start, row_end, result_col,column_first,column_second,Sheet_name,test_case_passed,test_case_failed):
#     global result_column,column_1,column_2,sheet_name,passed_case,failed_case
#     # Assign values directly to the global variables
#     # start_row = row_start
#     # end_row = row_end
#     result_column = result_col
#     column_1 = column_first
#     column_2 = column_second
#     sheet_name = Sheet_name
#     passed_case = test_case_passed
#     failed_case = test_case_failed

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, "emailOrPhoneNum")
        self.password_locator = (By.XPATH, '//input[@id="password"]')
        self.login_button_locator = (By.XPATH, '//button[normalize-space(text())="Sign In"]')
        self.dashboard_locator = (By.XPATH, '((//div[@class="d-flex justify-content-between"])[1]//div)[1]')
        self.avatar_image = (By.XPATH, '//*[@class="avatar-rounded-img"]')
        self.logout_button = (By.XPATH, '//*[@class="btn btn-link text-danger"]')

    def login(self):
        start_row = 31
        end_row = 36
        column_1 = XLUtils.column_letter_to_index('G')
        column_2 = XLUtils.column_letter_to_index('H')
        result_column = XLUtils.column_letter_to_index('I')
        sheet_name = 'dinesh1'
        passed_case = 'Test Passed'
        failed_case = 'Test failed'
        # set_values(31,36,XLUtils.column_letter_to_index('G'),
        #            XLUtils.column_letter_to_index('H'),XLUtils.column_letter_to_index('I'),'dinesh1',
        #            'Test Passed','Test failed')
        # Iterate over rows and fetch data from specific columns (F to G)
        for r in range(start_row, end_row + 1):
            username = XLUtils.readData(path, sheet_name, r, column_1)
            password = XLUtils.readData(path, sheet_name, r, column_2)
            # Enter the username
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
            enter_username = wait.until(EC.presence_of_element_located(self.username_locator))
            enter_username.send_keys(username)

            # Enter the password
            enter_password = wait.until(EC.presence_of_element_located(self.password_locator))
            enter_password.send_keys(password)

            # Click login button
            try:
                Click_login_button = wait.until(
                    EC.element_to_be_clickable(self.login_button_locator))
                self.driver.execute_script("arguments[0].click();", Click_login_button)

                # Verify if login was successful by checking the presence of the dashboard element
                dashboard_element = wait.until(EC.presence_of_element_located(self.dashboard_locator))
                dashboard_element_text = dashboard_element.text
                time.sleep(1)
                print(dashboard_element_text)

                if dashboard_element.is_displayed():
                    print(f"Login successful for row {r}")
                    XLUtils.writeData(path, sheet_name, r, result_column, passed_case)
                    time.sleep(2)  # Optional sleep between iterations for observation

                else:
                    print(f"Login failed for row {r}")
                    XLUtils.writeData(path, sheet_name, r, result_column, failed_case)
                    time.sleep(2)  # Optional sleep between iterations for observation

                wait = WebDriverWait(self.driver, 50, poll_frequency=3,
                                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                avatar_image_locator = wait.until(
                    EC.element_to_be_clickable(self.avatar_image))
                actions = ActionChains(self.driver)
                actions.move_to_element(avatar_image_locator).click().perform()

                logout_button_locator = wait.until(
                    EC.element_to_be_clickable(self.logout_button))
                actions = ActionChains(self.driver)
                actions.move_to_element(logout_button_locator).click().perform()
            except TimeoutException:
                XLUtils.writeData(path, sheet_name, r, result_column, failed_case)
                pass
