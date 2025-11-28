import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException, MoveTargetOutOfBoundsException
import allure


class GroupsKeyBoardNavigation:
    def __init__(self, driver):
        self.driver = driver
        self.search_feild_in_groups_list = (By.XPATH,
                                            '//*[@class="p-inputtext p-component form-control h-40px shadow-none filter-search-inp figma-bg"]')
        self.groups_list_10_elements = (
            By.XPATH,
            '//*[normalize-space(text())="Group Name"]//ancestor::thead//following-sibling::tbody//tr//td[1]//p')
        self.click_on_paginator = (By.XPATH, '//*[@class="p-paginator-icon pi pi-angle-right"]')
        self.click_on_20_drop_down = (
            By.XPATH, '//span[@class="p-dropdown-trigger-icon p-clickable pi pi-chevron-down"]')
        self.click_on_actual_drop_down_20 = (By.XPATH, '//li[normalize-space(text())="20"]')
        self.groups_list_20_elements = (
            By.XPATH,
            '//span[normalize-space(text())="Group Name"]//ancestor::thead//following-sibling::tbody//tr//td[1]//p')

    def groups_list_keyboard_navigation(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        search_feild_groups_list_locator = wait.until(
            EC.presence_of_element_located(self.search_feild_in_groups_list))
        allure.attach(self.driver.get_screenshot_as_png(), name='search',
                      attachment_type=allure.attachment_type.PNG)
        if self.driver.switch_to.active_element == search_feild_groups_list_locator:
            print("The cursor is already focused on the input field by default.")
        else:
            print("The cursor is not focused on the input field by default.")

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        groups_list_10_elements_locator = wait.until(
            EC.presence_of_all_elements_located(self.groups_list_10_elements))
        Element_list_groups_10 = [element.text for element in groups_list_10_elements_locator]
        length_of_element_list_groups_10 = len(Element_list_groups_10)
        time.sleep(2)
        print(len(Element_list_groups_10))
        time.sleep(1)
        print("Element_list of Groups List 10:", Element_list_groups_10)
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
        for i in range(length_of_element_list_groups_10):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.groups_list_10_elements))
                element = ledger_list_10_locator[i]
                text = element.text
                print("first page Arrow down:", text)
                actions.send_keys(Keys.ARROW_DOWN).perform()
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                # self.logger.error("StaleElementReferenceException caught.")
                pass
        # Arrow up
        for i in range(length_of_element_list_groups_10):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledger_list_10_locator = wait.until(
                    EC.presence_of_all_elements_located(self.groups_list_10_elements))
                element = ledger_list_10_locator[i]
                text = element.text
                print("first page Arrow up:", text)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_UP).perform()
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                              attachment_type=allure.attachment_type.PNG)
            except StaleElementReferenceException:
                pass

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        groups_list_10_elements_locator = wait.until(
            EC.presence_of_all_elements_located(self.groups_list_10_elements))

        for index, element in enumerate(groups_list_10_elements_locator):
            print(f"\033[33mindex of main page: {index}\033[0m")
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_paginator_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_paginator))

            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_paginator_locator).click().perform()

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
            for i in range(length_of_element_list_groups_10):
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                groups_list_10_elements_locator = wait.until(
                    EC.presence_of_all_elements_located(self.groups_list_10_elements))

                element = groups_list_10_elements_locator[i]
                text = element.text
                print(f"\033[36mText of group element when -Arrow Down- which is clicked: {text}\033[0m")

                actions.send_keys(Keys.ARROW_DOWN).perform()
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDownAll',
                              attachment_type=allure.attachment_type.PNG)
            # Move back up
            for k in range(length_of_element_list_groups_10):
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                groups_list_10_elements_locator = wait.until(
                    EC.presence_of_all_elements_located(self.groups_list_10_elements))
                element = groups_list_10_elements_locator[k]
                text = element.text
                print(f"\033[34mText of group element when - Arrow Up - which is clicked: {text}\033[0m")
                actions.send_keys(Keys.ARROW_UP).perform()
                allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUpAll',
                              attachment_type=allure.attachment_type.PNG)
            time.sleep(4)
            # Send Home key action
        actions.send_keys(Keys.HOME).perform()
        time.sleep(2)

    def groups_list_20(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_20_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_20_drop_down))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_20_drop_down_locator).click().perform()
        allure.attach(self.driver.get_screenshot_as_png(), name='Ledger20DropDown',
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(2)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_actual_drop_down_20_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_actual_drop_down_20))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_actual_drop_down_20_locator).click().perform()
        allure.attach(self.driver.get_screenshot_as_png(), name='Ledger20DropDownLick',
                      attachment_type=allure.attachment_type.PNG)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        groups_list_20_elements_locator = wait.until(
            EC.presence_of_all_elements_located(self.groups_list_20_elements))
        Element_list_groups_20 = [element.text for element in groups_list_20_elements_locator]
        length_of_element_list_group_20 = len(Element_list_groups_20)
        time.sleep(2)
        print(len(Element_list_groups_20))
        time.sleep(1)
        print("Element_list of Group List 20:", Element_list_groups_20)
        time.sleep(2)
        # ctrl down
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowDown',
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(1)
        # ctrl up
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowUp',
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(1)
        for i in range(length_of_element_list_group_20):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                groups_list_20_elements_locator = wait.until(
                    EC.presence_of_all_elements_located(self.groups_list_20_elements))
                element = groups_list_20_elements_locator[i]
                text = element.text
                print(f"\033[34mElements in first page for 20 elements Arrow Down: {text}\033[0m")
                actions.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(1)
                # allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                #               attachment_type=allure.attachment_type.PNG)
                # time.sleep(1)
            except (StaleElementReferenceException, IndexError):
                pass
        # Arrow up
        for j in range(length_of_element_list_group_20):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                groups_list_20_elements_locator = wait.until(
                    EC.presence_of_all_elements_located(self.groups_list_20_elements))
                element = groups_list_20_elements_locator[j]
                text = element.text
                print(text)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_UP).perform()
                time.sleep(1)
                print(f"\033[35mElements in first page for 20 elements Arrow up: {text}\033[0m")
                # allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                #               attachment_type=allure.attachment_type.PNG)
                # time.sleep(1)
            except (StaleElementReferenceException, IndexError):
                pass
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        groups_list_20_elements_locator = wait.until(
            EC.presence_of_all_elements_located(self.groups_list_20_elements))
        for index, element in enumerate(groups_list_20_elements_locator):
            print(f"\033[33mindex of main page for 20 elements: {index}\033[0m")
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_paginator_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_paginator))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_paginator_locator).click().perform()
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
            for i in range(length_of_element_list_group_20):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    groups_list_20_elements_locator = wait.until(
                        EC.presence_of_all_elements_located(self.groups_list_20_elements))
                    element = groups_list_20_elements_locator[i]
                    text = element.text
                    print(text)
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    # allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                    #               attachment_type=allure.attachment_type.PNG)
                except (StaleElementReferenceException, MoveTargetOutOfBoundsException,IndexError):
                    pass
            for k in range(length_of_element_list_group_20):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    groups_list_20_elements_locator = wait.until(
                        EC.presence_of_all_elements_located(self.groups_list_20_elements))
                    element = groups_list_20_elements_locator[k]
                    text = element.text
                    print(text)
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_UP).perform()
                    # allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                    #               attachment_type=allure.attachment_type.PNG)
                except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
                    pass
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.HOME).perform()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='Home',
                      attachment_type=allure.attachment_type.PNG)

    def groups_list_50(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_20_drop_down_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_20_drop_down))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_20_drop_down_locator).click().perform()
        allure.attach(self.driver.get_screenshot_as_png(), name='Ledger20DropDown',
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(2)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_actual_drop_down_20_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_actual_drop_down_20))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_actual_drop_down_20_locator).click().perform()
        allure.attach(self.driver.get_screenshot_as_png(), name='Ledger20DropDownLick',
                      attachment_type=allure.attachment_type.PNG)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        groups_list_20_elements_locator = wait.until(
            EC.presence_of_all_elements_located(self.groups_list_20_elements))
        Element_list_groups_20 = [element.text for element in groups_list_20_elements_locator]
        length_of_element_list_group_20 = len(Element_list_groups_20)
        time.sleep(2)
        print(len(Element_list_groups_20))
        time.sleep(1)
        print("Element_list of Group List 20:", Element_list_groups_20)
        time.sleep(2)
        # ctrl down
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowDown',
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(1)
        # ctrl up
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='CtrlArrowUp',
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(1)
        for i in range(length_of_element_list_group_20):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                groups_list_20_elements_locator = wait.until(
                    EC.presence_of_all_elements_located(self.groups_list_20_elements))
                element = groups_list_20_elements_locator[i]
                text = element.text
                print(f"\033[34mElements in first page for 20 elements Arrow Down: {text}\033[0m")
                actions.send_keys(Keys.ARROW_DOWN).perform()
                time.sleep(1)
                # allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                #               attachment_type=allure.attachment_type.PNG)
                # time.sleep(1)
            except (StaleElementReferenceException, IndexError):
                pass
        # Arrow up
        for j in range(length_of_element_list_group_20):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                groups_list_20_elements_locator = wait.until(
                    EC.presence_of_all_elements_located(self.groups_list_20_elements))
                element = groups_list_20_elements_locator[j]
                text = element.text
                print(text)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_UP).perform()
                time.sleep(1)
                print(f"\033[35mElements in first page for 20 elements Arrow up: {text}\033[0m")
                # allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                #               attachment_type=allure.attachment_type.PNG)
                # time.sleep(1)
            except (StaleElementReferenceException, IndexError):
                pass
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        groups_list_20_elements_locator = wait.until(
            EC.presence_of_all_elements_located(self.groups_list_20_elements))
        for index, element in enumerate(groups_list_20_elements_locator):
            print(f"\033[33mindex of main page for 20 elements: {index}\033[0m")
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_paginator_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_paginator))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_on_paginator_locator).click().perform()
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
            for i in range(length_of_element_list_group_20):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    groups_list_20_elements_locator = wait.until(
                        EC.presence_of_all_elements_located(self.groups_list_20_elements))
                    element = groups_list_20_elements_locator[i]
                    text = element.text
                    print(text)
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    # allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                    #               attachment_type=allure.attachment_type.PNG)
                except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
                    pass
            for k in range(length_of_element_list_group_20):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    groups_list_20_elements_locator = wait.until(
                        EC.presence_of_all_elements_located(self.groups_list_20_elements))
                    element = groups_list_20_elements_locator[k]
                    text = element.text
                    print(text)
                    actions = ActionChains(self.driver)
                    actions.send_keys(Keys.ARROW_UP).perform()
                    # allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                    #               attachment_type=allure.attachment_type.PNG)
                except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
                    pass
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.HOME).perform()
        # actions = ActionChains(self.driver)
        # actions.send_keys(Keys.ESCAPE).perform()
        # time.sleep(5)

        allure.attach(self.driver.get_screenshot_as_png(), name='Home',
                      attachment_type=allure.attachment_type.PNG)


class SidePanel:
    def __init__(self, driver):
        self.driver = driver
        self.groups_list_10_elements = (
            By.XPATH,
            '//*[normalize-space(text())="Group Name"]//ancestor::thead//following-sibling::tbody//tr//td[1]//p')
        self.click_on_paginator = (By.XPATH, '//*[@class="p-paginator-icon pi pi-angle-right"]')
        self.list_inside_sub_groups_and_ledgers = (By.XPATH, '//td[@class="text-elipsis-width"]')
        self.group_transcations = (By.XPATH, '(//tbody[@class="p-datatable-tbody"])[2]//tr//td[2]')
        self.group_transcations_inside = (By.XPATH, '//*[@class="m-0 table-td-elipsis font-size-14 text-primary"]')
        self.group_transcations_inside_ledgers = (By.XPATH, '//*[@class="font-size-14 mb-0"]')
        self.click_on_compare_in_balances = (By.XPATH, '//*[@class="btn btn-outline-primary b-r-8"]')
        self.list_of_organisation_name_in_compare = (By.XPATH,
                                                     '//div[@class="MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiAutocomplete-paper css-t4hinj"]//li')
        self.groups_list_in_compare = (By.XPATH,
                                       '//*[@class="MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 MuiAutocomplete-paper css-t4hinj"]//li')

    def subgroups_and_ledgers_and_group_transcations(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        groups_list_10_elements_locator = wait.until(
            EC.presence_of_all_elements_located(self.groups_list_10_elements))
        Element_list = [element.text for element in groups_list_10_elements_locator]
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
                    EC.presence_of_all_elements_located(self.groups_list_10_elements))
                element_on_main_page = ledger_list_elements[i]
                time.sleep(2)
                # element.send_keys(Keys.ENTER)
                actions = ActionChains(self.driver)
                # actions.move_to_element(element).click().perform()
                # element.click()
                self.driver.execute_script("arguments[0].click();", element_on_main_page)
                time.sleep(2)
                # # for all
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                groups_list_10_elements_locator = wait.until(
                    EC.presence_of_all_elements_located(self.groups_list_10_elements))
                for index, element in enumerate(groups_list_10_elements_locator):
                    print(f"\033[33mindex of main page for 20 elements: {index}\033[0m")
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    click_on_paginator_locator = wait.until(
                        EC.element_to_be_clickable(self.click_on_paginator))
                    actions = ActionChains(self.driver)
                    actions.move_to_element(click_on_paginator_locator).click().perform()
                    for k in range(length_of_element_list):
                        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                        groups_list_10_elements_locator = wait.until(
                            EC.presence_of_all_elements_located(self.groups_list_10_elements))
                        element = groups_list_10_elements_locator[k]
                        text = element.text
                        print(text)
                        actions.key_down(Keys.ALT).send_keys(Keys.ARROW_DOWN).key_up(Keys.ALT).perform()
                        time.sleep(1)
                    for s in range(length_of_element_list):
                        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                        groups_list_10_elements_locator = wait.until(
                            EC.presence_of_all_elements_located(self.groups_list_10_elements))
                        element = groups_list_10_elements_locator[s]
                        text = element.text
                        print(text)
                        actions.key_down(Keys.ALT).send_keys(Keys.ARROW_UP).key_up(Keys.ALT).perform()
                        time.sleep(1)
                time.sleep(3)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(3)
                actions.send_keys(Keys.HOME).perform()
                time.sleep(3)
                self.driver.execute_script("arguments[0].click();", element_on_main_page)
                time.sleep(2)
                # ctrl right
                for _ in range(5):
                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                for _ in range(5):
                    # ctrl left
                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_LEFT).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                for _ in range(2):
                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
                # sub groups and ledgers
                try:
                    wait = WebDriverWait(self.driver, 10, poll_frequency=3)
                    list_inside_sub_groups_and_ledgers_locator = wait.until(
                        EC.presence_of_all_elements_located(self.list_inside_sub_groups_and_ledgers))
                    for index, element in enumerate(groups_list_10_elements_locator):
                        print(f"\033[33mindex of main page for 20 elements: {index}\033[0m")
                        wait = WebDriverWait(self.driver, 10, poll_frequency=3)
                        list_inside_sub_groups_and_ledgers_locator = wait.until(
                            EC.presence_of_all_elements_located(self.list_inside_sub_groups_and_ledgers))
                        Element_list_sub_groups = [element.text for element in
                                                   list_inside_sub_groups_and_ledgers_locator]
                        length_of_element_list_subgroups = len(Element_list_sub_groups)
                        time.sleep(2)
                        print(len(Element_list_sub_groups))
                        time.sleep(1)
                        print("Element_list of sub groups 10:", Element_list_sub_groups)
                        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
                        time.sleep(1)
                        allure.attach(self.driver.get_screenshot_as_png(), name='ControlArrowDown',
                                      attachment_type=allure.attachment_type.PNG)
                        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
                        time.sleep(1)
                        for j in range(length_of_element_list_subgroups):
                            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                            list_inside_sub_groups_and_ledgers_locator = wait.until(
                                EC.presence_of_all_elements_located(self.list_inside_sub_groups_and_ledgers))
                            element = list_inside_sub_groups_and_ledgers_locator[j]
                            text = element.text
                            print(text)
                            actions.send_keys(Keys.ARROW_DOWN).perform()
                            time.sleep(1)
                        for s in range(length_of_element_list_subgroups):
                            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                            list_inside_sub_groups_and_ledgers_locator = wait.until(
                                EC.presence_of_all_elements_located(self.list_inside_sub_groups_and_ledgers))
                            element = list_inside_sub_groups_and_ledgers_locator[s]
                            text = element.text
                            print(text)

                            actions.send_keys(Keys.ARROW_UP).perform()
                            time.sleep(1)

                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                    # group transcations
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    group_transcations_locators = wait.until(
                        EC.presence_of_all_elements_located(self.group_transcations))
                    Element_list_group_transcations = [element.text for element in
                                                       group_transcations_locators]
                    length_of_element_list_group_transcations = len(Element_list_group_transcations)
                    time.sleep(2)
                    print(len(Element_list_group_transcations))
                    time.sleep(1)
                    print("Element_list of sub groups 10:", Element_list_group_transcations)
                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                    actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                    for j in range(length_of_element_list_group_transcations):
                        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                        list_inside_sub_groups_and_ledgers_locator = wait.until(
                            EC.presence_of_all_elements_located(self.group_transcations))
                        element = list_inside_sub_groups_and_ledgers_locator[j]
                        text = element.text
                        actions.send_keys(Keys.ARROW_DOWN).perform()
                        print(text)

                        time.sleep(1)
                    for s in range(length_of_element_list_group_transcations):
                        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                        list_inside_sub_groups_and_ledgers_locator = wait.until(
                            EC.presence_of_all_elements_located(self.group_transcations))
                        element = list_inside_sub_groups_and_ledgers_locator[s]
                        text = element.text
                        print(text)
                        actions.send_keys(Keys.ARROW_UP).perform()
                        time.sleep(1)
                    for k in range(length_of_element_list_group_transcations):
                        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                        list_inside_sub_groups_and_ledgers_locator = wait.until(
                            EC.presence_of_all_elements_located(self.group_transcations))
                        element = list_inside_sub_groups_and_ledgers_locator[k]
                        text = element.text
                        print(text)
                        actions.send_keys(Keys.ENTER).perform()
                        time.sleep(1)
                        actions.send_keys(Keys.ARROW_DOWN).perform()
                        time.sleep(1)
                        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                        group_transcations_inside_locators = wait.until(
                            EC.presence_of_all_elements_located(self.group_transcations_inside))
                        Element_list_group_transcations_inside = [element.text for element in
                                                                  group_transcations_inside_locators]
                        length_of_element_list_group_transcations_inside = len(Element_list_group_transcations_inside)

                        for u in range(length_of_element_list_group_transcations_inside):
                            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                            group_transcations_inside_locators = wait.until(
                                EC.presence_of_all_elements_located(self.group_transcations_inside))
                            element = group_transcations_inside_locators[u]
                            text = element.text
                            print(text)
                            actions.send_keys(Keys.ARROW_DOWN).perform()
                            time.sleep(1)
                        for y in range(length_of_element_list_group_transcations_inside):
                            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                            group_transcations_inside_locators = wait.until(
                                EC.presence_of_all_elements_located(self.group_transcations_inside))
                            element = group_transcations_inside_locators[y]
                            text = element.text
                            print(text)
                            actions.send_keys(Keys.ARROW_UP).perform()
                            time.sleep(1)
                        for h in range(length_of_element_list_group_transcations_inside):
                            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                            group_transcations_inside_locators = wait.until(
                                EC.presence_of_all_elements_located(self.group_transcations_inside))
                            element = group_transcations_inside_locators[h]
                            text = element.text
                            print(text)
                            actions.send_keys(Keys.ENTER).perform()
                            time.sleep(1)
                            actions.send_keys(Keys.ESCAPE).perform()
                            time.sleep(1)
                        # Ledgers
                        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                        group_transcations_inside_ledgers_locators = wait.until(
                            EC.presence_of_all_elements_located(self.group_transcations_inside_ledgers))
                        Element_list_group_transcations_inside_ledgers = [element.text for element in
                                                                          group_transcations_inside_ledgers_locators]
                        length_of_element_list_group_transcations_inside_ledgers = len(
                            Element_list_group_transcations_inside_ledgers)

                        for u in range(length_of_element_list_group_transcations_inside_ledgers):
                            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                            group_transcations_inside_locators = wait.until(
                                EC.presence_of_all_elements_located(self.group_transcations_inside_ledgers))
                            element = group_transcations_inside_locators[u]
                            text = element.text
                            print(text)
                            actions.send_keys(Keys.ARROW_DOWN).perform()
                            time.sleep(1)
                        for y in range(length_of_element_list_group_transcations_inside_ledgers):
                            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                            group_transcations_inside_locators = wait.until(
                                EC.presence_of_all_elements_located(self.group_transcations_inside_ledgers))
                            element = group_transcations_inside_locators[y]
                            text = element.text
                            print(text)
                            actions.send_keys(Keys.ARROW_UP).perform()
                            time.sleep(1)
                        for h in range(length_of_element_list_group_transcations_inside_ledgers):
                            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                            group_transcations_inside_locators = wait.until(
                                EC.presence_of_all_elements_located(self.group_transcations_inside_ledgers))
                            element = group_transcations_inside_locators[h]
                            text = element.text
                            print(text)
                            actions.send_keys(Keys.ENTER).perform()
                            time.sleep(1)
                            actions.send_keys(Keys.ESCAPE).perform()
                            time.sleep(1)
                        # customer details
                        actions.send_keys(Keys.ENTER).perform()
                        time.sleep(1)
                        for _ in range(2):
                            actions.send_keys(Keys.ESCAPE).perform()
                            time.sleep(1)
                        # actions.send_keys(Keys.ARROW_UP).perform()
                        # time.sleep(1)
                        # actions.send_keys(Keys.ENTER).perform()
                        # time.sleep(1)
                        # for _ in range(2):
                        #     actions.send_keys(Keys.ESCAPE).perform()
                        #     time.sleep(1)
                        # actions.send_keys(Keys.ARROW_DOWN).perform()
                        # time.sleep(1)
                except (TimeoutException, IndexError):
                    pass
                # # balances
                # # compare
                # # click on compare
                # wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                # click_on_compare_in_balances_locator = wait.until(
                #     EC.element_to_be_clickable(self.click_on_compare_in_balances))
                # actions = ActionChains(self.driver)
                # actions.move_to_element(click_on_compare_in_balances_locator).click().perform()
                #
                # wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                # list_of_organisation_name_in_compare_locator = wait.until(
                #     EC.presence_of_all_elements_located(self.list_of_organisation_name_in_compare))
                #
                # Element_list_of_organisations_in_compare = [element.text for element in
                #                                             list_of_organisation_name_in_compare_locator]
                # length_of_element_list_of_organisations_in_compare = len(Element_list_of_organisations_in_compare)
                # time.sleep(2)
                # print(length_of_element_list_of_organisations_in_compare)
                #
                # for j in range(length_of_element_list_of_organisations_in_compare):
                #     wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                #     list_of_organisation_name_in_compare_locator = wait.until(
                #         EC.presence_of_all_elements_located(self.list_of_organisation_name_in_compare))
                #     element = list_of_organisation_name_in_compare_locator[j]
                #     text = element.text
                #     actions.send_keys(Keys.ARROW_DOWN).perform()
                #     print(text)
                #     time.sleep(1)
                # for s in range(length_of_element_list_of_organisations_in_compare):
                #     wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                #     list_of_organisation_name_in_compare_locator = wait.until(
                #         EC.presence_of_all_elements_located(self.list_of_organisation_name_in_compare))
                #     element = list_of_organisation_name_in_compare_locator[s]
                #     text = element.text
                #     print(text)
                #     actions.send_keys(Keys.ARROW_UP).perform()
                #     time.sleep(1)
                # actions.send_keys(Keys.ENTER).perform()
                # time.sleep(1)
                # # select group
                # wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                # groups_list_in_compare_locator = wait.until(
                #     EC.presence_of_all_elements_located(self.groups_list_in_compare))
                #
                # Element_list_of_groups_in_compare = [element.text for element in
                #                                      groups_list_in_compare_locator]
                # length_of_element_list_of_groups_in_compare = len(Element_list_of_groups_in_compare)
                # time.sleep(2)
                # print(length_of_element_list_of_groups_in_compare)
                #
                # for j in range(length_of_element_list_of_organisations_in_compare):
                #     wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                #     groups_list_in_compare_locator = wait.until(
                #         EC.presence_of_all_elements_located(self.groups_list_in_compare))
                #     element = groups_list_in_compare_locator[j]
                #     text = element.text
                #     actions.send_keys(Keys.ARROW_DOWN).perform()
                #     print(text)
                #     time.sleep(1)
                # for s in range(length_of_element_list_of_organisations_in_compare):
                #     wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                #     groups_list_in_compare_locator = wait.until(
                #         EC.presence_of_all_elements_located(self.groups_list_in_compare))
                #     element = groups_list_in_compare_locator[s]
                #     text = element.text
                #     print(text)
                #     actions.send_keys(Keys.ARROW_UP).perform()
                #     time.sleep(1)
                # for _ in range(2):
                #     actions.send_keys(Keys.TAB).perform()
                #     time.sleep(1)
                # actions.send_keys(Keys.BACKSPACE).perform()
                # time.sleep(1)
                # actions.send_keys(Keys.ENTER).perform()
                # time.sleep(1)
                # # reclick escape to  click escape
                # actions.move_to_element(click_on_compare_in_balances_locator).click().perform()
                # time.sleep(1)
                # actions.send_keys(Keys.ESCAPE).perform()
                # time.sleep(1)
            except StaleElementReferenceException:
                pass
