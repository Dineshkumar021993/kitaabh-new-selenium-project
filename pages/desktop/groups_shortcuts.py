import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import pyautogui


class Ledgers:
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
        self.ledgers_list = (By.XPATH, '//tbody//tr//td[1]//p')
        self.ledgers_side_panel_list = (By.XPATH, '//div[@class="btn-group btn-tabs-list"]//button')
        self.cross_button_in_side_panel = (By.XPATH, '//*[@class="fa fa-times c-pointer"]')

    def click_on_kitaab_image(self):
        # select organization
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
        pyautogui.press('l')
        time.sleep(5)

    def ledgers_list_elements(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        ledgers_list_elements = wait.until(
            EC.presence_of_all_elements_located(self.ledgers_list))
        for i in ledgers_list_elements:
            try:
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                ledgers_list_elements = wait.until(
                    EC.presence_of_all_elements_located(self.ledgers_list))
                color = i.value_of_css_property("color")
                rgba = color.split('(')[1].split(')')[0].split(',')
                r = int(rgba[0].strip())  # Red
                g = int(rgba[1].strip())  # Green
                b = int(rgba[2].strip())  # Blue
                # Convert to hex
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for ledgers before clicking create button:-", hex_color)
                before_text = i.text
                print("text before clicking create button", before_text)
                pyautogui.hotkey('alt', 'f3')
                # actions = ActionChains(self.driver)
                # actions.key_down(Keys.ALT).send_keys("f3").key_up(Keys.ALT).perform()
                time.sleep(1)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                print("colour code for ledgers after clicking create button:-", hex_color)
                after_text = i.text
                print("text after clicking create button", after_text)
                time.sleep(3)
                actions = ActionChains(self.driver)
                actions.move_to_element(i).click().perform()
            except StaleElementReferenceException:
                pass

            time.sleep(2)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            ledgers_side_panel_list_elements = wait.until(
                EC.presence_of_all_elements_located(self.ledgers_side_panel_list))

            Element_list = [element.text for element in ledgers_side_panel_list_elements]
            length_of_element_list = len(Element_list)
            print("Element_list:", Element_list)

            for j in range(length_of_element_list):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledgers_side_panel_list_elements = wait.until(
                        EC.presence_of_all_elements_located(self.ledgers_side_panel_list))
                    element1 = ledgers_side_panel_list_elements[j]
                    color = element1.value_of_css_property("color")
                    rgba = color.split('(')[1].split(')')[0].split(',')
                    r = int(rgba[0].strip())  # Red
                    g = int(rgba[1].strip())  # Green
                    b = int(rgba[2].strip())  # Blue
                    # Convert to hex
                    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                    print("colour code for ledgers before clicking create button:-", hex_color)
                    time.sleep(1)
                    text_side_panel_before = element1.text
                    print("Text before clicking create button is:", text_side_panel_before)
                    pyautogui.hotkey('alt', 'f3')
                    time.sleep(1)
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    cross_button_in_side_panel_locator = wait.until(
                        EC.element_to_be_clickable(self.cross_button_in_side_panel))
                    actions = ActionChains(self.driver)
                    actions.move_to_element(cross_button_in_side_panel_locator).click().perform()
                    time.sleep(1)
                    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                    print("colour code for ledgers after clicking create button:-", hex_color)

                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    ledgers_side_panel_list_elements = wait.until(
                        EC.presence_of_all_elements_located(self.ledgers_side_panel_list))
                    element1 = ledgers_side_panel_list_elements[j]
                    actions.move_to_element(element1).click().perform()
                except StaleElementReferenceException:
                    pass
            pyautogui.press('esc')
            time.sleep(1)


class Groups:
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
        self.click_on_groups_list = (By.XPATH, '//tbody//tr//td[1]//p')
        self.groups_side_panel_list = (By.XPATH, '//div[@class="btn-group btn-tabs-list"]//button')
        self.cross_button_in_side_panel = (By.XPATH, '//*[@class="fa fa-times c-pointer"]')

    def groups_list(self):
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
        pyautogui.press('g')
        time.sleep(5)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        groups_lists_elements = wait.until(
            EC.presence_of_all_elements_located(self.click_on_groups_list))
        for i in groups_lists_elements:
            groups_lists_elements = wait.until(
                EC.presence_of_all_elements_located(self.click_on_groups_list))
            color = i.value_of_css_property("color")
            rgba = color.split('(')[1].split(')')[0].split(',')
            r = int(rgba[0].strip())  # Red
            g = int(rgba[1].strip())  # Green
            b = int(rgba[2].strip())  # Blue
            # Convert to hex
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers before clicking create button:-", hex_color)
            before_text = i.text
            print("text before clicking create button", before_text)
            pyautogui.hotkey('alt', 'f3')
            # actions = ActionChains(self.driver)
            # actions.key_down(Keys.ALT).send_keys("f3").key_up(Keys.ALT).perform()
            time.sleep(1)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(2)
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers after clicking create button:-", hex_color)
            after_text = i.text
            print("text after clicking create button", after_text)
            time.sleep(3)
            actions = ActionChains(self.driver)
            actions.move_to_element(i).click().perform()
            time.sleep(2)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            groups_side_panel_list_elements = wait.until(
                EC.presence_of_all_elements_located(self.groups_side_panel_list))

            Element_list = [element.text for element in groups_side_panel_list_elements]
            length_of_element_list = len(Element_list)
            print("Element_list:", Element_list)

            for j in range(length_of_element_list):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    groups_side_panel_list_elements = wait.until(
                        EC.presence_of_all_elements_located(self.groups_side_panel_list))
                    element1 = groups_side_panel_list_elements[j]
                    color = element1.value_of_css_property("color")
                    rgba = color.split('(')[1].split(')')[0].split(',')
                    r = int(rgba[0].strip())  # Red
                    g = int(rgba[1].strip())  # Green
                    b = int(rgba[2].strip())  # Blue
                    # Convert to hex
                    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                    print("colour code for ledgers before clicking create button:-", hex_color)
                    time.sleep(1)
                    text_side_panel_before = element1.text
                    print("Text before clicking create button is:", text_side_panel_before)
                    pyautogui.hotkey('alt', 'f3')
                    time.sleep(1)
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    cross_button_in_side_panel_locator = wait.until(
                        EC.element_to_be_clickable(self.cross_button_in_side_panel))
                    actions.move_to_element(cross_button_in_side_panel_locator).click().perform()
                    time.sleep(1)
                    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                    print("colour code for ledgers after clicking create button:-", hex_color)

                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    groups_side_panel_list_elements = wait.until(
                        EC.presence_of_all_elements_located(self.groups_side_panel_list))
                    element1 = groups_side_panel_list_elements[j]
                    actions.move_to_element(element1).click().perform()
                except StaleElementReferenceException:
                    pass
            pyautogui.press('esc')
            time.sleep(1)


class CostCentres:
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
        self.click_on_groups_list = (By.XPATH, '//tbody//tr//td[1]//p')
        self.groups_side_panel_list = (By.XPATH, '//div[@class="btn-group btn-tabs-list"]//button')
        self.cross_button_in_side_panel = (By.XPATH, '//*[@class="fa fa-times c-pointer"]')
        self.cost_centre_main_page_list = (By.XPATH, '//tbody//tr//td[1]//p')
        self.cost_centre_side_panel_list = (By.XPATH, '//div[@class="btn-group btn-tabs-list"]//button')

    def click_on_kitaab_image(self):
        # select organization
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

        # # click on back to
        # try:
        #     wait = WebDriverWait(self.driver, 10, poll_frequency=3)
        #     click_on_back_to_element = wait.until(
        #         EC.element_to_be_clickable(self.click_on_back_to))
        #     actions.move_to_element(click_on_back_to_element).click().perform()
        # except TimeoutException:
        #     pass
        # wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        # click_on_kitaab_image = wait.until(
        #     EC.element_to_be_clickable(self.click_on_kitaab_image_locator))
        # actions.move_to_element(click_on_kitaab_image).click().perform()
        # time.sleep(5)
        pyautogui.press('c')
        time.sleep(5)

    def cost_centres_list(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        cost_centre_main_page_list_elements = wait.until(
            EC.presence_of_all_elements_located(self.cost_centre_main_page_list))
        for i in cost_centre_main_page_list_elements:
            cost_centre_main_page_list_elements = wait.until(
                EC.presence_of_all_elements_located(self.cost_centre_main_page_list))
            color = i.value_of_css_property("color")
            rgba = color.split('(')[1].split(')')[0].split(',')
            r = int(rgba[0].strip())  # Red
            g = int(rgba[1].strip())  # Green
            b = int(rgba[2].strip())  # Blue
            # Convert to hex
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers before clicking create button:-", hex_color)
            before_text = i.text
            print("text before clicking create button", before_text)
            pyautogui.hotkey('alt', 'f3')
            # actions = ActionChains(self.driver)
            # actions.key_down(Keys.ALT).send_keys("f3").key_up(Keys.ALT).perform()
            time.sleep(1)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(2)
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers after clicking create button:-", hex_color)
            after_text = i.text
            print("text after clicking create button", after_text)
            time.sleep(3)
            actions = ActionChains(self.driver)
            actions.move_to_element(i).click().perform()
            time.sleep(2)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            cost_centre_side_panel_list_elements = wait.until(
                EC.presence_of_all_elements_located(self.cost_centre_side_panel_list))

            Element_list = [element.text for element in cost_centre_side_panel_list_elements]
            length_of_element_list = len(Element_list)
            print("Element_list:", Element_list)

            for j in range(length_of_element_list):
                try:
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    cost_centre_side_panel_list_elements = wait.until(
                        EC.presence_of_all_elements_located(self.cost_centre_side_panel_list))
                    element1 = cost_centre_side_panel_list_elements[j]
                    color = element1.value_of_css_property("color")
                    rgba = color.split('(')[1].split(')')[0].split(',')
                    r = int(rgba[0].strip())  # Red
                    g = int(rgba[1].strip())  # Green
                    b = int(rgba[2].strip())  # Blue
                    # Convert to hex
                    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                    print("colour code for ledgers before clicking create button:-", hex_color)
                    time.sleep(1)
                    text_side_panel_before = element1.text
                    print("Text before clicking create button is:", text_side_panel_before)
                    pyautogui.hotkey('alt', 'f3')
                    time.sleep(1)
                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    cross_button_in_side_panel_locator = wait.until(
                        EC.element_to_be_clickable(self.cross_button_in_side_panel))
                    actions.move_to_element(cross_button_in_side_panel_locator).click().perform()
                    time.sleep(1)
                    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                    print("colour code for ledgers after clicking create button:-", hex_color)

                    wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                    cost_centre_side_panel_list_elements = wait.until(
                        EC.presence_of_all_elements_located(self.cost_centre_side_panel_list))
                    element1 = cost_centre_side_panel_list_elements[j]
                    actions.move_to_element(element1).click().perform()

                except StaleElementReferenceException:
                    pass
            pyautogui.press('esc')
            time.sleep(1)


# class AllAccountingMasters:
#     def __init__(self, driver):
#         self.driver = driver
#         self.all_masters_list = (
#             By.XPATH, '//div[@class="col-xxl-12 col-xl-12 col-lg-12 col-md-12 col-sm-12 mb-0"]//button//div[1]//div[2]')
#         self.list_of_main_page = (By.XPATH, '//tbody//tr//td[1]//p')
#         self.list_of_side_panel = (By.XPATH, '//div[@class="btn-group btn-tabs-list"]//button')
#         self.cross_button_in_side_panel = (By.XPATH, '//*[@class="fa fa-times c-pointer"]')
#         self.organisation_drop_down_click = (
#             By.XPATH, '//i[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"]')
#         self.search_organisation_feild = (
#             By.XPATH, '//input[@class="p-inputtext p-component form-control h-40px shadow-none select-filter-input"]')
#         self.select_organisation = (By.XPATH, '//div[normalize-space(text())="Alpha Adarsh"]')
#
#     def click_on_kitaab_image(self):
#         # select organization
#         wait = WebDriverWait(self.driver, 50, poll_frequency=3)
#         click_on_organisation_drop_down = wait.until(
#             EC.element_to_be_clickable(self.organisation_drop_down_click))
#         actions = ActionChains(self.driver)
#         actions.move_to_element(click_on_organisation_drop_down).click().perform()
#         time.sleep(3)
#         wait = WebDriverWait(self.driver, 50, poll_frequency=3)
#         search_organisation_feild_locator = wait.until(
#             EC.presence_of_element_located(self.search_organisation_feild))
#         search_organisation_feild_locator.send_keys("Alpha Adarsh")
#         time.sleep(3)
#
#         wait = WebDriverWait(self.driver, 50, poll_frequency=3)
#         select_organisation_selection = wait.until(
#             EC.presence_of_element_located(self.select_organisation))
#         actions.move_to_element(select_organisation_selection).click().perform()

# def all_accounting_masters(self):
#     wait = WebDriverWait(self.driver, 50, poll_frequency=3)
#     all_masters_list_elements = wait.until(
#         EC.presence_of_all_elements_located(self.all_masters_list))
#
#     Element_list1 = [element.text for element in all_masters_list_elements]
#     length_of_element_list1 = len(Element_list1)
#     print("Element_list1", Element_list1)
#
#     for i in range(length_of_element_list1):
#         wait = WebDriverWait(self.driver, 50, poll_frequency=3)
#         all_masters_list_elements = wait.until(
#             EC.presence_of_all_elements_located(self.all_masters_list))
#         element1 = all_masters_list_elements[i]
#         element1.click()
#
#         wait = WebDriverWait(self.driver, 50, poll_frequency=3)
#         list_of_main_page_elements = wait.until(
#             EC.presence_of_all_elements_located(self.list_of_main_page))
#
#         for j in list_of_main_page_elements:
#             color = j.value_of_css_property("color")
#             rgba = color.split('(')[1].split(')')[0].split(',')
#             r = int(rgba[0].strip())  # Red
#             g = int(rgba[1].strip())  # Green
#             b = int(rgba[2].strip())  # Blue
#
#             # Convert to hex
#             hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
#             print("Colour code for ledgers before clicking create button:", hex_color)
#
#             before_text = j.text
#             print("Text before clicking create button:", before_text)
#
#             pyautogui.hotkey('alt', 'f3')
#             time.sleep(1)
#
#             actions = ActionChains(self.driver)
#             actions.send_keys(Keys.ESCAPE).perform()
#             time.sleep(2)
#
#             hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
#             print("Colour code for ledgers after clicking create button:", hex_color)
#
#             after_text = j.text
#             print("Text after clicking create button:", after_text)
#
#             time.sleep(3)
#             actions = ActionChains(self.driver)
#             actions.move_to_element(j).click().perform()
#             time.sleep(2)
#
#         # pyautogui.press('esc')
#
#         # side panel
#         wait = WebDriverWait(self.driver, 50, poll_frequency=3)
#         list_of_side_panel_elements = wait.until(
#             EC.presence_of_all_elements_located(self.list_of_side_panel))
#
#         Element_list2 = [element.text for element in list_of_side_panel_elements]
#         length_of_element_list2 = len(Element_list2)
#         print("Element_list:", Element_list2)
#
#         for k in range(length_of_element_list2):
#             try:
#                 wait = WebDriverWait(self.driver, 50, poll_frequency=3)
#                 list_of_side_panel_elements = wait.until(
#                     EC.presence_of_all_elements_located(self.list_of_side_panel))
#
#                 element2 = list_of_side_panel_elements[k]
#                 color = element2.value_of_css_property("color")
#                 rgba = color.split('(')[1].split(')')[0].split(',')
#                 r = int(rgba[0].strip())  # Red
#                 g = int(rgba[1].strip())  # Green
#                 b = int(rgba[2].strip())  # Blue
#
#                 # Convert to hex
#                 hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
#                 print("Colour code for ledgers before clicking create button:", hex_color)
#
#                 time.sleep(1)
#                 text_side_panel_before = element2.text
#                 print("Text before clicking create button is:", text_side_panel_before)
#
#                 pyautogui.hotkey('alt', 'f3')
#                 time.sleep(1)
#
#                 wait = WebDriverWait(self.driver, 50, poll_frequency=3)
#                 cross_button_in_side_panel_locator = wait.until(
#                     EC.element_to_be_clickable(self.cross_button_in_side_panel))
#
#                 actions = ActionChains(self.driver)
#                 actions.move_to_element(cross_button_in_side_panel_locator).click().perform()
#                 time.sleep(1)
#
#                 hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
#                 print("Colour code for ledgers after clicking create button:", hex_color)
#
#                 wait = WebDriverWait(self.driver, 50, poll_frequency=3)
#                 list_of_side_panel_elements = wait.until(
#                     EC.presence_of_all_elements_located(self.list_of_side_panel))
#
#                 element2 = list_of_side_panel_elements[k]
#                 actions.move_to_element(element2).click().perform()
#
#             except StaleElementReferenceException:
#                 pass
#             pyautogui.press('esc')


class CostCategories:
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
        self.cross_button_in_side_panel = (By.XPATH, '//*[@class="fa fa-times c-pointer"]')
        self.cost_categories_list = (By.XPATH, '//tbody//tr//td[1]//p')
        self.cost_categories_side_panel = (By.XPATH, '//div[@class="btn-group btn-tabs-list"]//button')

    def click_on_kitaab_image(self):
        # select organization
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
        pyautogui.press('e')
        time.sleep(5)

    def cost_categories_list_elements(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        cost_categories_list_elements = wait.until(
            EC.presence_of_all_elements_located(self.cost_categories_list))
        for i in cost_categories_list_elements:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            cost_categories_list_elements = wait.until(
                EC.presence_of_all_elements_located(self.cost_categories_list))
            color = i.value_of_css_property("color")
            rgba = color.split('(')[1].split(')')[0].split(',')
            r = int(rgba[0].strip())  # Red
            g = int(rgba[1].strip())  # Green
            b = int(rgba[2].strip())  # Blue
            # Convert to hex
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers before clicking create button:-", hex_color)
            before_text = i.text
            print("text before clicking create button", before_text)
            pyautogui.hotkey('alt', 'f3')
            # actions = ActionChains(self.driver)
            # actions.key_down(Keys.ALT).send_keys("f3").key_up(Keys.ALT).perform()
            time.sleep(1)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers after clicking create button:-", hex_color)
            after_text = i.text
            print("text after clicking create button", after_text)
            time.sleep(1.5)
            actions = ActionChains(self.driver)
            actions.move_to_element(i).click().perform()
            time.sleep(2)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)


class CostCentreClass:
    def __init__(self, driver):
        self.driver = driver
        self.organisation_drop_down_click = (
            By.XPATH, '//i[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"]')
        self.search_organisation_feild = (
            By.XPATH, '//input[@class="p-inputtext p-component form-control h-40px shadow-none select-filter-input"]')
        self.select_organisation = (By.XPATH, '//div[normalize-space(text())="Alpha Adarsh"]')
        self.cost_centre_class_list = (By.XPATH, '//tbody//tr//td[1]//p')

    def click_on_kitaab_image(self):
        # select organization
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
        pyautogui.press('s')
        time.sleep(5)

    def cost_center_class_list_elements(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        cost_centre_class_list_elements = wait.until(
            EC.presence_of_all_elements_located(self.cost_centre_class_list))
        for i in cost_centre_class_list_elements:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            cost_centre_class_list_elements = wait.until(
                EC.presence_of_all_elements_located(self.cost_centre_class_list))
            color = i.value_of_css_property("color")
            rgba = color.split('(')[1].split(')')[0].split(',')
            r = int(rgba[0].strip())  # Red
            g = int(rgba[1].strip())  # Green
            b = int(rgba[2].strip())  # Blue
            # Convert to hex
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers before clicking create button:-", hex_color)
            before_text = i.text
            print("text before clicking create button", before_text)
            pyautogui.hotkey('alt', 'f3')
            # actions = ActionChains(self.driver)
            # actions.key_down(Keys.ALT).send_keys("f3").key_up(Keys.ALT).perform()
            time.sleep(1)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers after clicking create button:-", hex_color)
            after_text = i.text
            print("text after clicking create button", after_text)
            time.sleep(1.5)
            actions = ActionChains(self.driver)
            actions.move_to_element(i).click().perform()
            time.sleep(2)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)


class Currency:
    def __init__(self, driver):
        self.driver = driver
        self.organisation_drop_down_click = (
            By.XPATH, '//i[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"]')
        self.search_organisation_feild = (
            By.XPATH, '//input[@class="p-inputtext p-component form-control h-40px shadow-none select-filter-input"]')
        self.select_organisation = (By.XPATH, '//div[normalize-space(text())="Alpha Adarsh"]')
        self.currency_list = (By.XPATH, '//tbody//tr//td[1]//p')

    def click_on_kitaab_image(self):
        # select organization
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
        pyautogui.press('y')
        time.sleep(5)

    def currency_list_elements(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        currency_list_lists = wait.until(
            EC.presence_of_all_elements_located(self.currency_list))
        for i in currency_list_lists:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            currency_list_lists = wait.until(
                EC.presence_of_all_elements_located(self.currency_list))
            color = i.value_of_css_property("color")
            rgba = color.split('(')[1].split(')')[0].split(',')
            r = int(rgba[0].strip())  # Red
            g = int(rgba[1].strip())  # Green
            b = int(rgba[2].strip())  # Blue
            # Convert to hex
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers before clicking create button:-", hex_color)
            before_text = i.text
            print("text before clicking create button", before_text)
            pyautogui.hotkey('alt', 'f3')
            # actions = ActionChains(self.driver)
            # actions.key_down(Keys.ALT).send_keys("f3").key_up(Keys.ALT).perform()
            time.sleep(1)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers after clicking create button:-", hex_color)
            after_text = i.text
            print("text after clicking create button", after_text)
            time.sleep(1.5)
            actions = ActionChains(self.driver)
            actions.move_to_element(i).click().perform()
            time.sleep(2)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)


class TranscationTypeList:
    def __init__(self, driver):
        self.driver = driver
        self.organisation_drop_down_click = (
            By.XPATH, '//i[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"]')
        self.search_organisation_feild = (
            By.XPATH, '//input[@class="p-inputtext p-component form-control h-40px shadow-none select-filter-input"]')
        self.select_organisation = (By.XPATH, '//div[normalize-space(text())="Alpha Adarsh"]')
        self.transcation_type_list = (By.XPATH, '//tbody//tr//td[1]//p')

    def click_on_kitaab_image(self):
        # select organization
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
        pyautogui.press('t')
        time.sleep(5)

    def transcation_type_list_elements(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcation_type_lists = wait.until(
            EC.presence_of_all_elements_located(self.transcation_type_list))
        for i in transcation_type_lists:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            transcation_type_lists = wait.until(
                EC.presence_of_all_elements_located(self.transcation_type_list))
            color = i.value_of_css_property("color")
            rgba = color.split('(')[1].split(')')[0].split(',')
            r = int(rgba[0].strip())  # Red
            g = int(rgba[1].strip())  # Green
            b = int(rgba[2].strip())  # Blue
            # Convert to hex
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers before clicking create button:-", hex_color)
            before_text = i.text
            print("text before clicking create button", before_text)
            pyautogui.hotkey('alt', 'f3')
            # actions = ActionChains(self.driver)
            # actions.key_down(Keys.ALT).send_keys("f3").key_up(Keys.ALT).perform()
            time.sleep(1)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers after clicking create button:-", hex_color)
            after_text = i.text
            print("text after clicking create button", after_text)
            time.sleep(1.5)
            actions = ActionChains(self.driver)
            actions.move_to_element(i).click().perform()
            time.sleep(2)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)


class RateOfExchange:
    def __init__(self, driver):
        self.driver = driver
        self.organisation_drop_down_click = (
            By.XPATH, '//i[@class="fi fi-bs-angle-down font-size-10 ms-2 l-h-1 v-align-middle text-color-1"]')
        self.search_organisation_feild = (
            By.XPATH, '//input[@class="p-inputtext p-component form-control h-40px shadow-none select-filter-input"]')
        self.select_organisation = (By.XPATH, '//div[normalize-space(text())="Alpha Adarsh"]')
        self.rate_of_exchange = (By.XPATH, '//tbody//tr//td[1]//p')

    def click_on_kitaab_image(self):
        # select organization
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
        pyautogui.press('x')
        time.sleep(5)

    def rate_of_exchange_elements(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        rate_of_exchange_lists = wait.until(
            EC.presence_of_all_elements_located(self.rate_of_exchange))
        for i in rate_of_exchange_lists:
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            rate_of_exchange_lists = wait.until(
                EC.presence_of_all_elements_located(self.rate_of_exchange))
            color = i.value_of_css_property("color")
            rgba = color.split('(')[1].split(')')[0].split(',')
            r = int(rgba[0].strip())  # Red
            g = int(rgba[1].strip())  # Green
            b = int(rgba[2].strip())  # Blue
            # Convert to hex
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers before clicking create button:-", hex_color)
            before_text = i.text
            print("text before clicking create button", before_text)
            pyautogui.hotkey('alt', 'f3')
            # actions = ActionChains(self.driver)
            # actions.key_down(Keys.ALT).send_keys("f3").key_up(Keys.ALT).perform()
            time.sleep(1)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            print("colour code for ledgers after clicking create button:-", hex_color)
            after_text = i.text
            print("text after clicking create button", after_text)
            time.sleep(1.5)
            # actions = ActionChains(self.driver)
            # actions.move_to_element(i).click().perform()
            # time.sleep(2)
            # actions.send_keys(Keys.ESCAPE).perform()
            # time.sleep(1)
