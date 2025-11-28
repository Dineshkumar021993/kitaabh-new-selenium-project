import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import pyautogui


class AllAccountingTranscations:
    def __init__(self, driver):
        self.driver = driver
        self.organisation_drop_down_click = (
            By.XPATH, '//i[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"]')
        self.search_organisation_feild = (
            By.XPATH, '//input[@class="p-inputtext p-component form-control h-40px shadow-none select-filter-input"]')
        self.select_organisation = (By.XPATH, '//div[normalize-space(text())="Alpha Adarsh"]')
        self.transcations_list_locator = (By.XPATH,
                                          '//*[normalize-space(text())="Particulars"]//ancestor::thead//following-sibling::tbody//tr/td[2]//span[2]')

    def all_transcations_list(self):
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_organisation_drop_down = wait.until(
                EC.element_to_be_clickable(self.organisation_drop_down_click))
            actions = ActionChains(self.driver)
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
            pyautogui.hotkey('alt', 't')
            time.sleep(2)
            pyautogui.press('l')
            time.sleep(5)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            transcations_list_locator_elements = wait.until(
                EC.presence_of_all_elements_located(self.transcations_list_locator))
            Element_list = [element.text for element in transcations_list_locator_elements]
            length_of_element_list = len(Element_list)
            print("Element_list:", Element_list)
            for i in range(length_of_element_list):
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                transcations_list_locator_elements = wait.until(
                    EC.presence_of_all_elements_located(self.transcations_list_locator))
                element = transcations_list_locator_elements[i]
                color = element.value_of_css_property("color")
                rgba = color.split('(')[1].split(')')[0].split(',')
                r = int(rgba[0].strip())  # Red
                g = int(rgba[1].strip())  # Green
                b = int(rgba[2].strip())  # Blue
                # Convert to hex
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for transcations before clicking create button:-", hex_color)
                before_text = element.text
                print("text before clicking create button", before_text)
                pyautogui.hotkey('alt', 'f3')
                time.sleep(1)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for transcations after clicking create button:-", hex_color)
                after_text = element.text
                print("text after clicking create button", after_text)
                time.sleep(3)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                time.sleep(2)
                for _ in range(2):
                    pyautogui.hotkey('alt', 'down')
                    time.sleep(0.5)
                time.sleep(1)
                for _ in range(2):
                    pyautogui.hotkey('alt', 'up')
                    time.sleep(1)
                time.sleep(1)
                pyautogui.hotkey('alt', 'enter')
                time.sleep(0.5)  # Adding a small delay if needed between presses
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.5)
            pyautogui.press('esc')
            time.sleep(2)
            pyautogui.press('s')
        except StaleElementReferenceException:
            pass

    def sales(self):
        time.sleep(4)
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            transcations_list_locator_elements = wait.until(
                EC.presence_of_all_elements_located(self.transcations_list_locator))
            Element_list = [element.text for element in transcations_list_locator_elements]
            length_of_element_list = len(Element_list)
            print("Element_list of Sales List:", Element_list)
            for i in range(length_of_element_list):
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                transcations_list_locator_elements = wait.until(
                    EC.presence_of_all_elements_located(self.transcations_list_locator))
                element = transcations_list_locator_elements[i]
                color = element.value_of_css_property("color")
                rgba = color.split('(')[1].split(')')[0].split(',')
                r = int(rgba[0].strip())  # Red
                g = int(rgba[1].strip())  # Green
                b = int(rgba[2].strip())  # Blue
                # Convert to hex
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for sales before clicking create button:-", hex_color)
                before_text = element.text
                print("text before in sales clicking create button", before_text)
                pyautogui.hotkey('alt', 'f3')
                time.sleep(1)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for sales after clicking create button:-", hex_color)
                after_text = element.text
                print("text after in sales clicking create button", after_text)
                time.sleep(3)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                time.sleep(2)
                for _ in range(2):
                    pyautogui.hotkey('alt', 'down')
                    time.sleep(0.5)
                time.sleep(1)
                for _ in range(2):
                    pyautogui.hotkey('alt', 'up')
                    time.sleep(1)
                time.sleep(1)
                pyautogui.hotkey('alt', 'enter')
                time.sleep(0.5)  # Adding a small delay if needed between presses
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.5)

            pyautogui.press('esc')
            time.sleep(2)
            pyautogui.press('p')
        except StaleElementReferenceException:
            pass
        time.sleep(4)

    def purchase(self):
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            transcations_list_locator_elements = wait.until(
                EC.presence_of_all_elements_located(self.transcations_list_locator))
            Element_list = [element.text for element in transcations_list_locator_elements]
            length_of_element_list = len(Element_list)
            print("Element_list of purchase List:", Element_list)
            for i in range(length_of_element_list):
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                transcations_list_locator_elements = wait.until(
                    EC.presence_of_all_elements_located(self.transcations_list_locator))
                element = transcations_list_locator_elements[i]
                color = element.value_of_css_property("color")
                rgba = color.split('(')[1].split(')')[0].split(',')
                r = int(rgba[0].strip())  # Red
                g = int(rgba[1].strip())  # Green
                b = int(rgba[2].strip())  # Blue
                # Convert to hex
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for purchases before clicking create button:-", hex_color)
                before_text = element.text
                print("text before in purchases clicking create button", before_text)
                pyautogui.hotkey('alt', 'f3')
                time.sleep(1)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for purchases after clicking create button:-", hex_color)
                after_text = element.text
                print("text after in purchases clicking create button", after_text)
                time.sleep(3)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                time.sleep(2)
                for _ in range(2):
                    pyautogui.hotkey('alt', 'down')
                    time.sleep(0.5)
                time.sleep(1)
                for _ in range(2):
                    pyautogui.hotkey('alt', 'up')
                    time.sleep(1)
                time.sleep(1)
                pyautogui.hotkey('alt', 'enter')
                time.sleep(0.5)  # Adding a small delay if needed between presses
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.5)
        except StaleElementReferenceException:
            pass

        pyautogui.press('esc')
        time.sleep(2)
        pyautogui.press('y')
        time.sleep(4)

    def payments(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcations_list_locator_elements = wait.until(
            EC.presence_of_all_elements_located(self.transcations_list_locator))
        Element_list = [element.text for element in transcations_list_locator_elements]
        length_of_element_list = len(Element_list)
        print("Element_list of payments List:", Element_list)
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                transcations_list_locator_elements = wait.until(
                    EC.presence_of_all_elements_located(self.transcations_list_locator))
                element = transcations_list_locator_elements[i]
                color = element.value_of_css_property("color")
                rgba = color.split('(')[1].split(')')[0].split(',')
                r = int(rgba[0].strip())  # Red
                g = int(rgba[1].strip())  # Green
                b = int(rgba[2].strip())  # Blue
                # Convert to hex
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for payments before clicking create button:-", hex_color)
                before_text = element.text
                print("text before in payments clicking create button", before_text)
                pyautogui.hotkey('alt', 'f3')
                time.sleep(1)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for purchases after clicking create button:-", hex_color)
                after_text = element.text
                print("text after in purchases clicking create button", after_text)
                time.sleep(3)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                time.sleep(2)
                for _ in range(2):
                    pyautogui.hotkey('alt', 'down')
                    time.sleep(0.5)
                time.sleep(1)
                for _ in range(2):
                    pyautogui.hotkey('alt', 'up')
                    time.sleep(1)
                time.sleep(1)
                pyautogui.hotkey('alt', 'enter')
                time.sleep(0.5)  # Adding a small delay if needed between presses
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.5)
            except StaleElementReferenceException:
                pass

        pyautogui.press('esc')
        time.sleep(2)
        pyautogui.press('j')
        time.sleep(4)

    def journals(self):
        try:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            transcations_list_locator_elements = wait.until(
                EC.presence_of_all_elements_located(self.transcations_list_locator))
            Element_list = [element.text for element in transcations_list_locator_elements]
            length_of_element_list = len(Element_list)
            print("Element_list of journals List:", Element_list)
            for i in range(length_of_element_list):
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                transcations_list_locator_elements = wait.until(
                    EC.presence_of_all_elements_located(self.transcations_list_locator))
                element = transcations_list_locator_elements[i]
                color = element.value_of_css_property("color")
                rgba = color.split('(')[1].split(')')[0].split(',')
                r = int(rgba[0].strip())  # Red
                g = int(rgba[1].strip())  # Green
                b = int(rgba[2].strip())  # Blue
                # Convert to hex
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for journal before clicking create button:-", hex_color)
                before_text = element.text
                print("text before in journal clicking create button", before_text)
                pyautogui.hotkey('alt', 'f3')
                time.sleep(1)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for journals after clicking create button:-", hex_color)
                after_text = element.text
                print("text after in journal clicking create button", after_text)
                time.sleep(3)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                time.sleep(2)
                for _ in range(2):
                    pyautogui.hotkey('alt', 'down')
                    time.sleep(0.5)
                time.sleep(1)
                for _ in range(2):
                    pyautogui.hotkey('alt', 'up')
                    time.sleep(1)
                time.sleep(1)
                pyautogui.hotkey('alt', 'enter')
                time.sleep(0.5)  # Adding a small delay if needed between presses
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.5)
        except StaleElementReferenceException:
            pass

        pyautogui.press('esc')
        time.sleep(2)
        pyautogui.press('r')
        time.sleep(4)

    def receipt(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcations_list_locator_elements = wait.until(
            EC.presence_of_all_elements_located(self.transcations_list_locator))
        Element_list = [element.text for element in transcations_list_locator_elements]
        length_of_element_list = len(Element_list)
        print("Element_list of receipt List:", Element_list)
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                transcations_list_locator_elements = wait.until(
                    EC.presence_of_all_elements_located(self.transcations_list_locator))
                element = transcations_list_locator_elements[i]
                color = element.value_of_css_property("color")
                rgba = color.split('(')[1].split(')')[0].split(',')
                r = int(rgba[0].strip())  # Red
                g = int(rgba[1].strip())  # Green
                b = int(rgba[2].strip())  # Blue
                # Convert to hex
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for receipt before clicking create button:-", hex_color)
                before_text = element.text
                print("text before in receipt clicking create button", before_text)
                pyautogui.hotkey('alt', 'f3')
                time.sleep(1)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for receipt after clicking create button:-", hex_color)
                after_text = element.text
                print("text after in receipt clicking create button", after_text)
                time.sleep(3)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                time.sleep(2)
            except StaleElementReferenceException:
                pass

            for _ in range(2):
                pyautogui.hotkey('alt', 'down')
                time.sleep(0.5)
            time.sleep(1)
            for _ in range(2):
                pyautogui.hotkey('alt', 'up')
                time.sleep(1)
            time.sleep(1)
            pyautogui.hotkey('alt', 'enter')
            time.sleep(0.5)  # Adding a small delay if needed between presses
            for _ in range(2):
                pyautogui.press('esc')
                time.sleep(0.5)

        pyautogui.press('esc')
        time.sleep(2)
        pyautogui.press('n')
        time.sleep(4)

    def contra(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcations_list_locator_elements = wait.until(
            EC.presence_of_all_elements_located(self.transcations_list_locator))
        Element_list = [element.text for element in transcations_list_locator_elements]
        length_of_element_list = len(Element_list)
        print("Element_list of contra List:", Element_list)
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                transcations_list_locator_elements = wait.until(
                    EC.presence_of_all_elements_located(self.transcations_list_locator))
                element = transcations_list_locator_elements[i]
                color = element.value_of_css_property("color")
                rgba = color.split('(')[1].split(')')[0].split(',')
                r = int(rgba[0].strip())  # Red
                g = int(rgba[1].strip())  # Green
                b = int(rgba[2].strip())  # Blue
                # Convert to hex
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for contra before clicking create button:-", hex_color)
                before_text = element.text
                print("text before in contra clicking create button", before_text)
                pyautogui.hotkey('alt', 'f3')
                time.sleep(1)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for contra after clicking create button:-", hex_color)
                after_text = element.text
                print("text after in contra clicking create button", after_text)
                time.sleep(3)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                time.sleep(2)
            except StaleElementReferenceException:
                pass

            for _ in range(2):
                pyautogui.hotkey('alt', 'down')
                time.sleep(0.5)
            time.sleep(1)
            for _ in range(2):
                pyautogui.hotkey('alt', 'up')
                time.sleep(1)
            time.sleep(1)
            pyautogui.hotkey('alt', 'enter')
            time.sleep(0.5)  # Adding a small delay if needed between presses
            for _ in range(2):
                pyautogui.press('esc')
                time.sleep(0.5)

        pyautogui.press('esc')
        time.sleep(2)
        pyautogui.press('d')
        time.sleep(4)

    def debit_note(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcations_list_locator_elements = wait.until(
            EC.presence_of_all_elements_located(self.transcations_list_locator))
        Element_list = [element.text for element in transcations_list_locator_elements]
        length_of_element_list = len(Element_list)
        print("Element_list of debit note List:", Element_list)
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                transcations_list_locator_elements = wait.until(
                    EC.presence_of_all_elements_located(self.transcations_list_locator))
                element = transcations_list_locator_elements[i]
                color = element.value_of_css_property("color")
                rgba = color.split('(')[1].split(')')[0].split(',')
                r = int(rgba[0].strip())  # Red
                g = int(rgba[1].strip())  # Green
                b = int(rgba[2].strip())  # Blue
                # Convert to hex
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for debit note before clicking create button:-", hex_color)
                before_text = element.text
                print("text before in debit note clicking create button", before_text)
                pyautogui.hotkey('alt', 'f3')
                time.sleep(1)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for debit note after clicking create button:-", hex_color)
                after_text = element.text
                print("text after in debit note clicking create button", after_text)
                time.sleep(3)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                time.sleep(2)
            except StaleElementReferenceException:
                pass

            for _ in range(2):
                pyautogui.hotkey('alt', 'down')
                time.sleep(0.5)
            time.sleep(1)
            for _ in range(2):
                pyautogui.hotkey('alt', 'up')
                time.sleep(1)
            time.sleep(1)
            pyautogui.hotkey('alt', 'enter')
            time.sleep(0.5)  # Adding a small delay if needed between presses
            for _ in range(2):
                pyautogui.press('esc')
                time.sleep(0.5)

        pyautogui.press('esc')
        time.sleep(2)
        pyautogui.press('c')
        time.sleep(4)

    def credit_note(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcations_list_locator_elements = wait.until(
            EC.presence_of_all_elements_located(self.transcations_list_locator))
        Element_list = [element.text for element in transcations_list_locator_elements]
        length_of_element_list = len(Element_list)
        print("Element_list of credit note List:", Element_list)
        for i in range(length_of_element_list):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                transcations_list_locator_elements = wait.until(
                    EC.presence_of_all_elements_located(self.transcations_list_locator))
                element = transcations_list_locator_elements[i]
                color = element.value_of_css_property("color")
                rgba = color.split('(')[1].split(')')[0].split(',')
                r = int(rgba[0].strip())  # Red
                g = int(rgba[1].strip())  # Green
                b = int(rgba[2].strip())  # Blue
                # Convert to hex
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for credit note before clicking create button:-", hex_color)
                before_text = element.text
                print("text before in credit note clicking create button", before_text)
                pyautogui.hotkey('alt', 'f3')
                time.sleep(1)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for credit note after clicking create button:-", hex_color)
                after_text = element.text
                print("text after in credit  note clicking create button", after_text)
                time.sleep(3)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                time.sleep(2)
            except StaleElementReferenceException:
                pass

            for _ in range(2):
                pyautogui.hotkey('alt', 'down')
                time.sleep(0.5)
            time.sleep(1)
            for _ in range(2):
                pyautogui.hotkey('alt', 'up')
                time.sleep(1)
            time.sleep(1)
            pyautogui.hotkey('alt', 'enter')
            time.sleep(0.5)  # Adding a small delay if needed between presses
            for _ in range(2):
                pyautogui.press('esc')
                time.sleep(0.5)
