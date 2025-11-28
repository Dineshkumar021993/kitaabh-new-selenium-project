import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException, MoveTargetOutOfBoundsException
import allure


def highlight_element(driver, element):
    """Highlights a Selenium WebDriver element."""
    driver.execute_script("arguments[0].style.border='3px solid magenta'", element)
    time.sleep(1)
    driver.execute_script("arguments[0].style.border=''; arguments[0].style.backgroundColor='';", element)


class CostCentreKeyboardNavigationList:
    def __init__(self, driver):
        self.driver = driver
        self.search_feild_in_cost_centers_list = (By.XPATH, '//*[@id="search1"]')
        self.cost_centre_list = (By.XPATH,
                                 '//*[normalize-space(text())="Cost Centre Name"]//ancestor::thead//following-sibling::tbody//tr//td[1]//p')
        self.click_on_first_element = (By.XPATH,
                                       '(//*[normalize-space(text())="Cost Centre Name"]//ancestor::thead//following-sibling::tbody//tr//td[1]//p)[1]')
        self.element_list_in_summary = (
            By.XPATH, '(//thead[@class="p-datatable-thead"])[2]//following-sibling::tbody//tr/td[1]//span[2]')
        self.paginator_in_summary_in_side_panel = (By.XPATH, '(//span[@class="p-paginator-icon pi pi-angle-right"])[2]')
        self.income_and_expense_allocation = (By.XPATH, '//*[normalize-space(text())="Income & Expense Allocation"]')
        self.click_on_incomes_in_reports = (
            By.XPATH, '(//*[@class="p-treetable-toggler-icon pi pi-fw pi-chevron-right"])[1]')
        # doubt in xpath
        self.elements_in_incomes = (
            By.XPATH, '//thead[@class="p-treetable-thead"]//following-sibling::tbody//tr//following-sibling::tr//td[1]')
        self.click_on_paginator = (By.XPATH, '//*[@class="p-paginator-icon pi pi-angle-right"]')

    def cost_center_keyboard_navigation(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        search_feild_in_cost_centers_list_locator = wait.until(
            EC.presence_of_element_located(self.search_feild_in_cost_centers_list))
        allure.attach(self.driver.get_screenshot_as_png(), name='search',
                      attachment_type=allure.attachment_type.PNG)
        if self.driver.switch_to.active_element == search_feild_in_cost_centers_list_locator:
            print("The cursor is already focused on the input field by default.")
        else:
            print("The cursor is not focused on the input field by default.")
        # create
        actions = ActionChains(self.driver)
        actions.key_down(Keys.ALT).send_keys('c').key_up(Keys.ALT).perform()
        time.sleep(1)
        actions.send_keys(Keys.ESCAPE).perform()
        time.sleep(1)

        # Edit
        actions.key_down(Keys.ALT).send_keys('e').key_up(Keys.ALT).perform()
        time.sleep(1)
        actions.send_keys(Keys.ESCAPE).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        cost_centre_list_locator = wait.until(
            EC.presence_of_all_elements_located(self.cost_centre_list))
        Element_list_cost_centre_list = [element.text for element in cost_centre_list_locator]
        length_of_element_list_cost_centre_10 = len(Element_list_cost_centre_list)
        time.sleep(2)
        print(len(Element_list_cost_centre_list))
        time.sleep(1)
        print("Element_list of Cost Centre List 10:", Element_list_cost_centre_list)
        time.sleep(2)

        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
        time.sleep(2)

        # ctrl up
        actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
        time.sleep(2)

        for i in range(length_of_element_list_cost_centre_10):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                cost_centre_list_locator = wait.until(
                    EC.presence_of_all_elements_located(self.cost_centre_list))
                element = cost_centre_list_locator[i]
                text = element.text
                print("first page Arrow down:", text)
                actions.send_keys(Keys.ARROW_DOWN).perform()
            except StaleElementReferenceException:
                pass
            time.sleep(3)
            # Arrow up
        for j in range(length_of_element_list_cost_centre_10):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                cost_centre_list_locator = wait.until(
                    EC.presence_of_all_elements_located(self.cost_centre_list))
                element = cost_centre_list_locator[j]
                text = element.text
                print("first page Arrow up:", text)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_UP).perform()
            except StaleElementReferenceException:
                pass

        # wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        # cost_centre_list_locator = wait.until(
        #     EC.presence_of_all_elements_located(self.cost_centre_list))
        # for index, element in enumerate(cost_centre_list_locator):
        #     print(f"\033[33mindex of main page: {index}\033[0m")
        #     wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        #     click_on_paginator_locator = wait.until(
        #         EC.element_to_be_clickable(self.click_on_paginator))
        #     actions = ActionChains(self.driver)
        #     actions.move_to_element(click_on_paginator_locator).click().perform()
        #
        #     # Ctrl + Arrow Down
        #     actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).perform()
        #     time.sleep(1)
        #     allure.attach(self.driver.get_screenshot_as_png(), name='CtrlDown',
        #                   attachment_type=allure.attachment_type.PNG)
        #
        #     # Ctrl + Arrow Up
        #     actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
        #     time.sleep(1)
        #     allure.attach(self.driver.get_screenshot_as_png(), name='CtrlUp',
        #                   attachment_type=allure.attachment_type.PNG)
        #     for p in range(length_of_element_list_cost_centre_10):
        #         try:
        #             wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        #             cost_centre_list_locator = wait.until(
        #                 EC.presence_of_all_elements_located(self.cost_centre_list))
        #             element = cost_centre_list_locator[p]
        #             text = element.text
        #             print(f"\033[36mText of group element when -Arrow Down- which is clicked: {text}\033[0m")
        #             actions.send_keys(Keys.ARROW_DOWN).perform()
        #             allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDownAll',
        #                           attachment_type=allure.attachment_type.PNG)
        #         except IndexError:
        #             pass
        #     # Move back up
        #     for q in range(length_of_element_list_cost_centre_10):
        #         try:
        #             wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        #             cost_centre_list_locator = wait.until(
        #                 EC.presence_of_all_elements_located(self.cost_centre_list))
        #             element = cost_centre_list_locator[q]
        #             text = element.text
        #             print(f"\033[34mText of group element when - Arrow Up - which is clicked: {text}\033[0m")
        #             actions.send_keys(Keys.ARROW_UP).perform()
        #             allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUpAll',
        #                           attachment_type=allure.attachment_type.PNG)
        #         except IndexError:
        #             pass
        #     time.sleep(4)
        #     # Send Home key action
        # actions.send_keys(Keys.HOME).perform()
        # time.sleep(2)

        # click on first element
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_first_element_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_first_element))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_first_element_locator).click().perform()
        time.sleep(3)
        # pratice cost centres
        for k in range(length_of_element_list_cost_centre_10):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                cost_centre_list_locator = wait.until(
                    EC.presence_of_all_elements_located(self.cost_centre_list))
                element = cost_centre_list_locator[k]
                text = element.text
                print(text)
                time.sleep(1)
                actions.key_down(Keys.ALT).send_keys(Keys.DOWN).key_up(Keys.ALT).perform()
                time.sleep(1)
            except (StaleElementReferenceException,IndexError):
                pass
        for s in range(length_of_element_list_cost_centre_10):
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                cost_centre_list_locator = wait.until(
                    EC.presence_of_all_elements_located(self.cost_centre_list))
                element = cost_centre_list_locator[s]
                text = element.text
                print(text)
                actions.key_down(Keys.ALT).send_keys(Keys.UP).key_up(Keys.ALT).perform()
                time.sleep(1)
            except StaleElementReferenceException:
                pass
        # click again click edit button after opening side panel
        # Edit
        actions.key_down(Keys.ALT).send_keys('e').key_up(Keys.ALT).perform()
        time.sleep(1)
        actions.send_keys(Keys.ESCAPE).perform()
        time.sleep(2)

        # side panel
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        cost_centre_list_locator = wait.until(
            EC.presence_of_all_elements_located(self.cost_centre_list))
        for index, elementinmainpage in enumerate(cost_centre_list_locator):
            print(f"\033[33mindex of main page: {index}\033[0m")
            actions.move_to_element(elementinmainpage).click().perform()
            # control right arrow
            for _ in range(6):
                actions.key_down(Keys.CONTROL).send_keys(Keys.RIGHT).key_up(Keys.CONTROL).perform()
                time.sleep(1)
            for _ in range(6):
                actions.key_down(Keys.CONTROL).send_keys(Keys.LEFT).key_up(Keys.CONTROL).perform()
                time.sleep(1)
            for _ in range(1):
                actions.key_down(Keys.CONTROL).send_keys(Keys.RIGHT).key_up(Keys.CONTROL).perform()
                time.sleep(1)
            # summary
            #  list control up and control down
            actions.key_down(Keys.CONTROL).send_keys(Keys.DOWN).key_up(Keys.CONTROL).perform()
            time.sleep(1)
            actions.key_down(Keys.CONTROL).send_keys(Keys.UP).key_up(Keys.CONTROL).perform()
            time.sleep(1)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            element_list_in_summary_locator = wait.until(
                EC.presence_of_all_elements_located(self.element_list_in_summary))
            Element_list_cost_centre_list_summary = [element.text for element in element_list_in_summary_locator]
            length_of_element_list_cost_centre_summary = len(Element_list_cost_centre_list_summary)

            # paginator also
            for u in range(length_of_element_list_cost_centre_summary):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    element_list_in_summary_locator = wait.until(
                        EC.presence_of_all_elements_located(self.element_list_in_summary))
                    element_summary_arrow_down = element_list_in_summary_locator[u]
                    text_element_summary_arrow_down = element_summary_arrow_down.text
                    print("summary page Arrow down:", text_element_summary_arrow_down)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1)
                except StaleElementReferenceException:
                    pass
            time.sleep(3)

            # Arrow up
            for t in range(length_of_element_list_cost_centre_summary):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    element_list_in_summary_locator = wait.until(
                        EC.presence_of_all_elements_located(self.element_list_in_summary))
                    element_summary_arrow_up = element_list_in_summary_locator[t]
                    text_element_summary_arrow_up = element_summary_arrow_up.text
                    print("summary page Arrow up:", text_element_summary_arrow_up)
                    actions.send_keys(Keys.ARROW_UP).perform()
                    time.sleep(1)
                except StaleElementReferenceException:
                    pass

            # for remaining pages
            for index1, element in enumerate(element_list_in_summary_locator):
                print(f"\033[33mindex of main page: {index1}\033[0m")
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                paginator_in_summary_in_side_panel_locator = wait.until(
                    EC.element_to_be_clickable(self.paginator_in_summary_in_side_panel))
                actions = ActionChains(self.driver)
                actions.move_to_element(paginator_in_summary_in_side_panel_locator).click().perform()
                time.sleep(2)
                for r in range(length_of_element_list_cost_centre_summary):
                    try:
                        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                        element_list_in_summary_locator = wait.until(
                            EC.presence_of_all_elements_located(self.element_list_in_summary))
                        element_summary_arrow_down = element_list_in_summary_locator[r]
                        text_element_summary_arrow_down = element_summary_arrow_down.text
                        print("summary page Arrow down:", text_element_summary_arrow_down)
                        # for enter and escape ,if I click escape it directly landing to main page
                        # actions.send_keys(Keys.ENTER).perform()
                        # time.sleep(1)
                        # actions.send_keys(Keys.ESCAPE).perform()
                        # time.sleep(1)
                        actions.send_keys(Keys.ARROW_DOWN).perform()
                        time.sleep(1)
                        # allure.attach(self.driver.get_screenshot_as_png(), name='ArrowDown',
                        #               attachment_type=allure.attachment_type.PNG)                
                    except StaleElementReferenceException:
                        # self.logger.error("StaleElementReferenceException caught.")
                        pass
                time.sleep(3)

                # Arrow up
                for w in range(length_of_element_list_cost_centre_summary):
                    try:
                        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                        element_list_in_summary_locator = wait.until(
                            EC.presence_of_all_elements_located(self.element_list_in_summary))
                        element_summary_arrow_up = element_list_in_summary_locator[w]
                        text_element_summary_arrow_up = element_summary_arrow_up.text
                        print("summary page Arrow up:", text_element_summary_arrow_up)
                        actions.send_keys(Keys.ARROW_UP).perform()
                        time.sleep(1)
                    # allure.attach(self.driver.get_screenshot_as_png(), name='ArrowUp',
                    #               attachment_type=allure.attachment_type.PNG)
                    except StaleElementReferenceException:
                        pass
