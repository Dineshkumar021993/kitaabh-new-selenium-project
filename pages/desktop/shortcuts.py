import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
import pyautogui
from datetime import datetime


def highlight_element(driver, element):
    """Highlights a Selenium WebDriver element."""
    driver.execute_script("arguments[0].style.border='2px solid magenta'", element)
    time.sleep(1)
    driver.execute_script("arguments[0].style.border=''; arguments[0].style.backgroundColor='';", element)


class Dashboard:
    def __init__(self, driver):
        self.driver = driver
        self.click_on_kitaab_image_locator = (
            By.XPATH,
            '//img[@class="c-sidebar-brand-full mobile-logo-width img-fluid inside-logo-full normal-theme-logo"]')
        self.dashboard_highliting = (By.ID, 'KIT0')
        self.masters_highliting = (By.ID, 'KIT1')
        self.transcations_highliting_locator = (By.ID, 'KIT2')
        self.reports_highliting_locator = (By.ID, 'KIT3')
        self.gst_highlighting_locator = (By.ID, 'KIT4')
        self.other_statutory_highlighting_locator = (By.ID, 'KIT5')
        self.Audit_highlighting_locator = (By.ID, 'KIT6')
        self.Record_keeping_highlighting_locator = (By.ID, 'KIT7')

    def click_on_kitaab_image(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_kitaab_image = wait.until(
            EC.element_to_be_clickable(self.click_on_kitaab_image_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_kitaab_image).click().perform()
        time.sleep(2)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        dashboard_highliting_element = wait.until(
            EC.presence_of_element_located(self.dashboard_highliting))
        dashboard_highliting_element.click()
        time.sleep(1.5)
        highlight_element(self.driver, dashboard_highliting_element)
        background = dashboard_highliting_element.value_of_css_property('background')
        print(background)
        time.sleep(2)
        rgba = background.split('(')[1].split(')')[0].split(',')
        r = int(rgba[0].strip())  # Red
        g = int(rgba[1].strip())  # Green
        b = int(rgba[2].strip())  # Blue
        # Convert to hex
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for DASHBOARD before clicking create button:-", hex_color)
        pyautogui.hotkey('alt', 'f3')
        time.sleep(1)
        pyautogui.press('esc')
        highlight_element(self.driver, dashboard_highliting_element)
        time.sleep(1)
        hex_color1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for DASHBOARD after clicking create button:-", hex_color1)
        if hex_color == hex_color1:
            print("Dashboard:- cursor is on the DASHBOARD before and after clicking create button")
        else:
            print("Dashboard:- cursor is not on the DASHBOARD before and after clicking create button")

    def check_masters(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        masters_highliting_element = wait.until(
            EC.element_to_be_clickable(self.masters_highliting))
        actions = ActionChains(self.driver)
        actions.move_to_element(masters_highliting_element).click().perform()
        time.sleep(1.5)
        highlight_element(self.driver, masters_highliting_element)
        background = masters_highliting_element.value_of_css_property('background')
        print(background)
        time.sleep(2)
        rgba = background.split('(')[1].split(')')[0].split(',')
        r = int(rgba[0].strip())  # Red
        g = int(rgba[1].strip())  # Green
        b = int(rgba[2].strip())  # Blue
        # Convert to hex
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for MASTERS before clicking create button:-", hex_color)
        pyautogui.hotkey('alt', 'f3')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        highlight_element(self.driver, masters_highliting_element)
        hex_color1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for MASTERS after clicking create button:-", hex_color1)
        if hex_color == hex_color1:
            print("MASTERS:- cursor is on the MASTERS before and after clicking create button")
        else:
            print("MASTERS:- cursor is not on the MASTERS before and after clicking create button")
        time.sleep(2)

    def click_on_Transcations(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcations_highliting_locator_element = wait.until(
            EC.element_to_be_clickable(self.transcations_highliting_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(transcations_highliting_locator_element).click().perform()
        time.sleep(1.5)
        highlight_element(self.driver, transcations_highliting_locator_element)
        background = transcations_highliting_locator_element.value_of_css_property('background')
        print(background)
        time.sleep(2)
        rgba = background.split('(')[1].split(')')[0].split(',')
        r = int(rgba[0].strip())  # Red
        g = int(rgba[1].strip())  # Green
        b = int(rgba[2].strip())  # Blue
        # Convert to hex
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for TRANSCATIONS before clicking create button:-", hex_color)
        pyautogui.hotkey('alt', 'f3')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        highlight_element(self.driver, transcations_highliting_locator_element)
        hex_color1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for TRANSCATIONS after clicking create button:-", hex_color1)
        if hex_color == hex_color1:
            print("TRANSCATIONS:- cursor is on the TRANSCATIONS before and after clicking create button")
        else:
            print("TRANSCATIONS:- cursor is not on the TRANSCATIONS before and after clicking create button")

    def click_on_Reports(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        reports_highliting_locator_element = wait.until(
            EC.element_to_be_clickable(self.reports_highliting_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(reports_highliting_locator_element).click().perform()
        time.sleep(1.5)
        highlight_element(self.driver, reports_highliting_locator_element)
        background = reports_highliting_locator_element.value_of_css_property('background')
        print(background)
        time.sleep(2)
        rgba = background.split('(')[1].split(')')[0].split(',')
        r = int(rgba[0].strip())  # Red
        g = int(rgba[1].strip())  # Green
        b = int(rgba[2].strip())  # Blue
        # Convert to hex
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for REPORTS before clicking create button:-", hex_color)
        pyautogui.hotkey('alt', 'f3')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        highlight_element(self.driver, reports_highliting_locator_element)
        hex_color1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for REPORTS after clicking create button:-", hex_color1)
        if hex_color == hex_color1:
            print("REPORTS:- cursor is on the REPORTS before and after clicking create button")
        else:
            print("REPORTS:- cursor is not on the REPORTS before and after clicking create button")

    def gst_highlighting_element(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        gst_highlighting_locator_element = wait.until(
            EC.element_to_be_clickable(self.gst_highlighting_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(gst_highlighting_locator_element).click().perform()
        time.sleep(1.5)
        highlight_element(self.driver, gst_highlighting_locator_element)
        background = gst_highlighting_locator_element.value_of_css_property('background')
        print(background)
        time.sleep(2)
        rgba = background.split('(')[1].split(')')[0].split(',')
        r = int(rgba[0].strip())  # Red
        g = int(rgba[1].strip())  # Green
        b = int(rgba[2].strip())  # Blue
        # Convert to hex
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for GST before clicking create button:-", hex_color)
        pyautogui.hotkey('alt', 'f3')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        highlight_element(self.driver, gst_highlighting_locator_element)
        hex_color1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for GST after clicking create button:-", hex_color1)
        if hex_color == hex_color1:
            print("GST:- cursor is on the GST before and after clicking create button")
        else:
            print("GST:- cursor is not on the GST before and after clicking create button")

    def other_statutory_element(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        other_statutory_highlighting_locator_element = wait.until(
            EC.element_to_be_clickable(self.other_statutory_highlighting_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(other_statutory_highlighting_locator_element).click().perform()
        time.sleep(1.5)
        highlight_element(self.driver, other_statutory_highlighting_locator_element)
        background = other_statutory_highlighting_locator_element.value_of_css_property('background')
        print(background)
        time.sleep(2)
        rgba = background.split('(')[1].split(')')[0].split(',')
        r = int(rgba[0].strip())  # Red
        g = int(rgba[1].strip())  # Green
        b = int(rgba[2].strip())  # Blue
        # Convert to hex
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for OTHER STATUTORY before clicking create button:-", hex_color)
        pyautogui.hotkey('alt', 'f3')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        highlight_element(self.driver, other_statutory_highlighting_locator_element)
        hex_color1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for OTHER STATUTORY after clicking create button:-", hex_color1)
        if hex_color == hex_color1:
            print("OTHER STATUTORY:- cursor is on the OTHER STATUTORY before and after clicking create button")
        else:
            print("OTHER STATUTORY:- cursor is not on the OTHER STATUTORY before and after clicking create button")

    def Audit_highliting(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        Audit_highlighting_locator_element = wait.until(
            EC.element_to_be_clickable(self.Audit_highlighting_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(Audit_highlighting_locator_element).click().perform()
        time.sleep(1.5)
        highlight_element(self.driver, Audit_highlighting_locator_element)
        background = Audit_highlighting_locator_element.value_of_css_property('background')
        print(background)
        time.sleep(2)
        rgba = background.split('(')[1].split(')')[0].split(',')
        r = int(rgba[0].strip())  # Red
        g = int(rgba[1].strip())  # Green
        b = int(rgba[2].strip())  # Blue
        # Convert to hex
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for AUDIT before clicking create button:-", hex_color)
        pyautogui.hotkey('alt', 'f3')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        highlight_element(self.driver, Audit_highlighting_locator_element)
        hex_color1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for AUDIT after clicking create button:-", hex_color1)
        if hex_color == hex_color1:
            print("AUDIT:- cursor is on the AUDIT before and after clicking create button")
        else:
            print("AUDIT:- cursor is not on the AUDIT before and after clicking create button")

    def record_keeping_highlighting(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        Record_keeping_highlighting_locator_element = wait.until(
            EC.element_to_be_clickable(self.Record_keeping_highlighting_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(Record_keeping_highlighting_locator_element).click().perform()
        time.sleep(1.5)
        highlight_element(self.driver, Record_keeping_highlighting_locator_element)
        background = Record_keeping_highlighting_locator_element.value_of_css_property('background')
        print(background)
        time.sleep(2)
        rgba = background.split('(')[1].split(')')[0].split(',')
        r = int(rgba[0].strip())  # Red
        g = int(rgba[1].strip())  # Green
        b = int(rgba[2].strip())  # Blue
        # Convert to hex
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for RECORD KEEPING before clicking create button:-", hex_color)
        pyautogui.hotkey('alt', 'f3')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        highlight_element(self.driver, Record_keeping_highlighting_locator_element)
        hex_color1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for RECORD KEEPING after clicking create button:-", hex_color1)
        if hex_color == hex_color1:
            print("RECORD KEEPING:-cursor is on the RECORD KEEPING before and after clicking create button")
        else:
            print("RECORD KEEPING:- cursor is not on the RECORD KEEPING before and after clicking create button")


class LedgersList:
    def __init__(self, driver):
        self.driver = driver
        self.organisation_drop_down_click = (
            By.XPATH, '//i[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"]')
        self.search_organisation_feild = (
            By.XPATH, '//input[@class="p-inputtext p-component form-control h-40px shadow-none select-filter-input"]')
        self.select_organisation = (By.XPATH, '//div[normalize-space(text())="Alpha Adarsh"]')
        self.click_on_back_to = (By.XPATH, '//i[@class="fi fi-bs-angle-left l-h-1 v-align-middle font-size-10"]')
        self.click_on_kitaab_image_locator = (
            By.XPATH,
            '//img[@class="c-sidebar-brand-full mobile-logo-width img-fluid inside-logo-full normal-theme-logo"]')
        self.list_of_ledgers = (By.XPATH, '//td[1]//p')
        self.ledger_33 = (By.XPATH, '//tr[@class="p-highlight p-selectable-row"]')
        self.ledger_info_text = (By.XPATH, '//button[@class="btn btn-link btn-sm text-primary active ps-0 pe-0 me-24"]')
        self.transcations_text = (By.XPATH, '//button[normalize-space(text())="Transactions"]')
        self.ledger_list_advance_tax = (By.XPATH, '//p[normalize-space(text())="Advance Tax - Current Assets"]')
        self.ledger_list_amit = (
            By.XPATH, '//p[normalize-space(text())="Amit Ledger for Gst Classification / Gst Group"]')

    def click_on_kitaab_image(self):
        # select organization
        actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_organisation_drop_down = wait.until(
            EC.element_to_be_clickable(self.organisation_drop_down_click))
        actions.move_to_element(click_on_organisation_drop_down).click().perform()
        time.sleep(3)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        search_organisation_feild_locator = wait.until(
            EC.presence_of_element_located(self.search_organisation_feild))
        search_organisation_feild_locator.send_keys("Alpha Adarsh")
        time.sleep(3)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        select_organisation_selection = wait.until(
            EC.presence_of_element_located(self.select_organisation))
        actions.move_to_element(select_organisation_selection).click().perform()

        # click on back to
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=3)
            click_on_back_to_element = wait.until(
                EC.element_to_be_clickable(self.click_on_back_to))
            actions.move_to_element(click_on_back_to_element).click().perform()
        except TimeoutException:
            pass

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_kitaab_image = wait.until(
            EC.element_to_be_clickable(self.click_on_kitaab_image_locator))
        actions.move_to_element(click_on_kitaab_image).click().perform()
        time.sleep(5)
        pyautogui.press('L')
        time.sleep(5)

    def ledgers_list_count(self):
        # wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        # select_organisation_selection = wait.until(
        #     EC.presence_of_all_elements_located(self.list_of_ledgers))
        # for i in select_organisation_selection:
        #     time.sleep(3)
        #     before_text = i.text
        #     print(before_text)
        #     time.sleep(5)
        #     background = i.value_of_css_property('background')
        #     print(background)
        #     time.sleep(2)
        #     rgba = background.split('(')[1].split(')')[0].split(',')
        #     r = int(rgba[0].strip())  # Red
        #     g = int(rgba[1].strip())  # Green
        #     b = int(rgba[2].strip())  # Blue
        #     # Convert to hex
        #     hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        #     print("colour code for ledgers before clicking create button:-", hex_color)
        #     # pyautogui.hotkey('alt', 'f3')
        #     actions = ActionChains(self.driver)
        #     actions.key_down(Keys.ALT).send_keys(Keys.F3).key_up(Keys.ALT).perform()
        #     time.sleep(1)
        #     pyautogui.press('esc')
        #     time.sleep(1)
        #     after_text = i.text
        #     print(after_text)
        #     time.sleep(1)
        #     hex_color1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        #     print("colour code for ledgers after clicking create button:-", hex_color1)
        #     if before_text == after_text:
        #         print("cursor is at same line before and after esc the create button")
        #     else:
        #         print("cursor is not at same line before and after esc the create button")
        #     if hex_color == hex_color1:
        #         print("cursor is at same line before and after esc the create button")
        #     else:
        #         print("cursor is not at same line before and after esc the create button")
        #     time.sleep(4)

        # for 33
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_33_locator = wait.until(
            EC.presence_of_element_located(self.ledger_33))
        before_text = ledger_33_locator.text
        print(before_text)
        time.sleep(5)
        background = ledger_33_locator.value_of_css_property('background')
        print(background)
        time.sleep(2)
        rgba = background.split('(')[1].split(')')[0].split(',')
        r = int(rgba[0].strip())  # Red
        g = int(rgba[1].strip())  # Green
        b = int(rgba[2].strip())  # Blue

        # Convert to hex
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for ledgers before clicking create button:-", hex_color)
        # pyautogui.hotkey('alt', 'f3')
        actions = ActionChains(self.driver)
        actions.key_down(Keys.ALT).send_keys(Keys.F3).key_up(Keys.ALT).perform()
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        after_text = ledger_33_locator.text
        print(after_text)
        time.sleep(1)
        hex_color1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for ledgers after clicking create button:-", hex_color1)
        if before_text == after_text:
            print("cursor is at same line before and after esc the create button")
        else:
            print("cursor is not at same line before and after esc the create button")
        if hex_color == hex_color1:
            print("cursor is at same line before and after esc the create button")
        else:
            print("cursor is not at same line before and after esc the create button")
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(3)
        # ledger-info text
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_info_text_element = wait.until(
            EC.presence_of_element_located(self.ledger_info_text))
        ledger_info_text_before_click_on_create_button = ledger_info_text_element.text
        time.sleep(2)
        print("ledger_info_after_create_click:", ledger_info_text_before_click_on_create_button)
        time.sleep(1)
        pyautogui.hotkey('alt', 'f3')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(2)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_info_text_element = wait.until(
            EC.presence_of_element_located(self.ledger_info_text))
        ledger_info_text_after_click_on_create_button = ledger_info_text_element.text
        print("ledger_info_after_create_click", ledger_info_text_after_click_on_create_button)
        if ledger_info_text_before_click_on_create_button == ledger_info_text_after_click_on_create_button:
            print("cursor is highlighted at same position before and after clicking create button")
        else:
            print("cursor is not highlighted at same position before and after clicking create button")
        for i in range(2):
            actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcations_text_locator = wait.until(
            EC.presence_of_element_located(self.transcations_text))

        Transcations_text_element_before_create_click = transcations_text_locator.text
        print("Transcation text before click:", Transcations_text_element_before_create_click)
        pyautogui.hotkey('alt', 'f3')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcations_text_locator = wait.until(
            EC.presence_of_element_located(self.transcations_text))
        Transcations_text_element_after_create_click = transcations_text_locator.text
        print("Transcation text after click:", Transcations_text_element_after_create_click)
        if Transcations_text_element_before_create_click == Transcations_text_element_after_create_click:
            print("cursor is highlighted at same position before and after clicking create button")
        else:
            print("cursor is not highlighted at same position before and after clicking create button")
        pyautogui.press('esc')

        for i in range(2):
            actions.send_keys(Keys.ARROW_DOWN).perform()

        # stock in hand
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_33_locator = wait.until(
            EC.presence_of_element_located(self.ledger_33))
        before_text = ledger_33_locator.text
        print(before_text)
        time.sleep(5)
        background = ledger_33_locator.value_of_css_property('background')
        print(background)
        time.sleep(2)
        rgba = background.split('(')[1].split(')')[0].split(',')
        r = int(rgba[0].strip())  # Red
        g = int(rgba[1].strip())  # Green
        b = int(rgba[2].strip())  # Blue

        # Convert to hex
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for ledgers before clicking create button:-", hex_color)
        # pyautogui.hotkey('alt', 'f3')
        actions = ActionChains(self.driver)
        actions.key_down(Keys.ALT).send_keys(Keys.F3).key_up(Keys.ALT).perform()
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        after_text = ledger_33_locator.text
        print(after_text)
        time.sleep(1)
        hex_color1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for ledgers after clicking create button:-", hex_color1)
        if before_text == after_text:
            print("cursor is at same line before and after esc the create button")
        else:
            print("cursor is not at same line before and after esc the create button")
        if hex_color == hex_color1:
            print("cursor is at same line before and after esc the create button")
        else:
            print("cursor is not at same line before and after esc the create button")
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(4)
        # ledger-info text-for stock in hand
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            ledger_info_text_element1 = wait.until(
                EC.presence_of_element_located(self.ledger_info_text))
            ledger_info_text_before_click_on_create_button1 = ledger_info_text_element1.text
            time.sleep(2)
            print("ledger_info_after_create_click", ledger_info_text_before_click_on_create_button1)
            time.sleep(1)
            pyautogui.hotkey('alt', 'f3')
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(2)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            ledger_info_text_element1 = wait.until(
                EC.presence_of_element_located(self.ledger_info_text))
            ledger_info_text_after_click_on_create_button1 = ledger_info_text_element1.text
            print("ledger_info_after_create_click", ledger_info_text_after_click_on_create_button1)
            if ledger_info_text_before_click_on_create_button1 == ledger_info_text_after_click_on_create_button1:
                print("cursor is highlighted at same position before and after clicking create button")
            else:
                print("cursor is not highlighted at same position before and after clicking create button")
            for i in range(2):
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            transcations_text_locator1 = wait.until(
                EC.presence_of_element_located(self.transcations_text))
            Transcations_text_element_before_create_click1 = transcations_text_locator1.text
            print("Transcation text before click:", Transcations_text_element_before_create_click1)
            pyautogui.hotkey('alt', 'f3')
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(1)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            transcations_text_locator1 = wait.until(
                EC.presence_of_element_located(self.transcations_text))
            Transcations_text_element_after_create_click1 = transcations_text_locator1.text
            print("Transcation text after click:", Transcations_text_element_after_create_click1)
            if Transcations_text_element_before_create_click1 == Transcations_text_element_after_create_click1:
                print("cursor is highlighted at same position before and after clicking create button")
            else:
                print("cursor is not highlighted at same position before and after clicking create button")
            pyautogui.press('esc')

        except StaleElementReferenceException:
            pass
        for i in range(2):
            actions.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(4)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledger_list_advance_tax_locator = wait.until(
            EC.presence_of_element_located(self.ledger_list_advance_tax))
        before_text_advance_tax = ledger_list_advance_tax_locator.text
        print(before_text_advance_tax)
        time.sleep(5)
        background = ledger_list_advance_tax_locator.value_of_css_property('background')
        print(background)
        time.sleep(2)
        rgba = background.split('(')[1].split(')')[0].split(',')
        r = int(rgba[0].strip())  # Red
        g = int(rgba[1].strip())  # Green
        b = int(rgba[2].strip())  # Blue

        # Convert to hex
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for ledgers before clicking create button:-", hex_color)
        # pyautogui.hotkey('alt', 'f3')
        actions = ActionChains(self.driver)
        actions.key_down(Keys.ALT).send_keys(Keys.F3).key_up(Keys.ALT).perform()
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(1)
        after_text_advance_tax = ledger_list_advance_tax_locator.text
        print(after_text_advance_tax)
        time.sleep(1)
        hex_color1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print("colour code for ledgers after clicking create button:-", hex_color1)
        if before_text_advance_tax == after_text_advance_tax:
            print("cursor is at same line before and after esc the create button")
        else:
            print("cursor is not at same line before and after esc the create button")
        if hex_color == hex_color1:
            print("cursor is at same line before and after esc the create button")
        else:
            print("cursor is not at same line before and after esc the create button")

        actions.send_keys(Keys.ENTER).perform()
        time.sleep(4)
        # ledger-info text-for advance tax
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            ledger_info_text_element2 = wait.until(
                EC.presence_of_element_located(self.ledger_info_text))
            ledger_info_text_before_click_on_create_button2 = ledger_info_text_element2.text
            time.sleep(2)
            print("ledger_info_after_create_click", ledger_info_text_before_click_on_create_button2)
            time.sleep(1)
            pyautogui.hotkey('alt', 'f3')
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(2)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            ledger_info_text_element2 = wait.until(
                EC.presence_of_element_located(self.ledger_info_text))
            ledger_info_text_after_click_on_create_button2 = ledger_info_text_element2.text
            print("ledger_info_after_create_click", ledger_info_text_after_click_on_create_button2)
            if ledger_info_text_before_click_on_create_button2 == ledger_info_text_after_click_on_create_button2:
                print("cursor is highlighted at same position before and after clicking create button")
            else:
                print("cursor is not highlighted at same position before and after clicking create button")
            for i in range(2):
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            transcations_text_locator2 = wait.until(
                EC.presence_of_element_located(self.transcations_text))
            Transcations_text_element_before_create_click2 = transcations_text_locator2.text
            print("Transcation text before click:", Transcations_text_element_before_create_click2)
            pyautogui.hotkey('alt', 'f3')
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(1)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            transcations_text_locator2 = wait.until(
                EC.presence_of_element_located(self.transcations_text))
            Transcations_text_element_after_create_click2 = transcations_text_locator2.text
            print("Transcation text after click:", Transcations_text_element_after_create_click2)
            if Transcations_text_element_before_create_click2 == Transcations_text_element_after_create_click2:
                print("cursor is highlighted at same position before and after clicking create button")
            else:
                print("cursor is not highlighted at same position before and after clicking create button")
            pyautogui.press('esc')
        except StaleElementReferenceException:
            pass

        for i in range(4):
            actions.send_keys(Keys.ARROW_DOWN).perform()

        # Amit ledgers
        time.sleep(4)
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            ledger_list_amit_locator = wait.until(
                EC.presence_of_element_located(self.ledger_list_amit))
            before_text_amit_ledger = ledger_list_amit_locator.text
            print("Amit ledger before create button click:", before_text_amit_ledger)
            time.sleep(5)
            background = ledger_list_advance_tax_locator.value_of_css_property('background')
            print(background)
            time.sleep(2)
            rgba = background.split('(')[1].split(')')[0].split(',')
            r = int(rgba[0].strip())  # Red
            g = int(rgba[1].strip())  # Green
            b = int(rgba[2].strip())  # Blue

            # Convert to hex
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers before clicking create button:-", hex_color)
            # pyautogui.hotkey('alt', 'f3')
            actions = ActionChains(self.driver)
            actions.key_down(Keys.CONTROL).send_keys("r").key_up(Keys.CONTROL).perform()
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(1)
            after_text_amit_ledger = ledger_list_amit_locator.text
            print("Amit ledger after text:", after_text_amit_ledger)
            time.sleep(1)
            hex_color1 = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers after clicking create button:-", hex_color1)
            if before_text_advance_tax == after_text_advance_tax:
                print("cursor is at same line before and after esc the create button")
            else:
                print("cursor is not at same line before and after esc the create button")
            if hex_color == hex_color1:
                print("cursor is at same line before and after esc the create button")
            else:
                print("cursor is not at same line before and after esc the create button")

            actions.send_keys(Keys.ENTER).perform()
            time.sleep(4)
            # ledger-info text-for advance tax
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            ledger_info_text_element2 = wait.until(
                EC.presence_of_element_located(self.ledger_info_text))
            ledger_info_text_before_click_on_create_button3 = ledger_info_text_element2.text
            time.sleep(2)
            print("ledger_info_after_create_click", ledger_info_text_before_click_on_create_button3)
            time.sleep(1)
            pyautogui.hotkey('alt', 'f3')
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(2)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            ledger_info_text_element3 = wait.until(
                EC.presence_of_element_located(self.ledger_info_text))
            ledger_info_text_after_click_on_create_button3 = ledger_info_text_element3.text
            print("ledger_info_after_create_click", ledger_info_text_after_click_on_create_button3)
            if ledger_info_text_before_click_on_create_button3 == ledger_info_text_after_click_on_create_button3:
                print("cursor is highlighted at same position before and after clicking create button")
            else:
                print("cursor is not highlighted at same position before and after clicking create button")
            for i in range(2):
                actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            transcations_text_locator3 = wait.until(
                EC.presence_of_element_located(self.transcations_text))
            Transcations_text_element_before_create_click3 = transcations_text_locator3.text
            print("Transcation text before click:", Transcations_text_element_before_create_click3)
            pyautogui.hotkey('alt', 'f3')
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(1)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            transcations_text_locator3 = wait.until(
                EC.presence_of_element_located(self.transcations_text))
            Transcations_text_element_after_create_click3 = transcations_text_locator3.text
            print("Transcation text after click:", Transcations_text_element_after_create_click3)
            if Transcations_text_element_before_create_click3 == Transcations_text_element_after_create_click3:
                print("cursor is highlighted at same position before and after clicking create button")
            else:
                print("cursor is not highlighted at same position before and after clicking create button")
            pyautogui.press('esc')
        except StaleElementReferenceException:
            pass
        time.sleep(5)




















