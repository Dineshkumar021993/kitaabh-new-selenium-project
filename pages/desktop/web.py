import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
import allure
import pyautogui
import webcolors
from datetime import datetime
import pyautogui

def highlight_element(driver, element):
    """Highlights a Selenium WebDriver element."""
    driver.execute_script("arguments[0].style.border='2px solid magenta'", element)
    time.sleep(1)
    driver.execute_script("arguments[0].style.border=''; arguments[0].style.backgroundColor='lightblue';", element)


class Ledgers:
    def __init__(self, driver):
        self.driver = driver
        self.click_on_create_button = (By.XPATH, '//a[@class="btn btn-primary dropdown-toggle h-36px new-btn-tooltip"]')
        self.tool_tip = (By.XPATH, '//*[normalize-space(text())="Create New ( F3 )"]')
        self.refresh_button = (By.XPATH, '//i[@class="fi fi-bs-refresh"]')
        self.refresh_button_tool_tip = (By.XPATH, '//*[normalize-space(text())="Refresh ( Ctrl + R )"]')
        self.click_on_accounting_vouchers = (By.XPATH, '//*[@id="MODULE1"]')
        self.click_on_sales = (By.XPATH, '//*[@id="SUB_MODULE0"]')
        self.godown_text_in_main_page = (By.XPATH, '(//p[@class="text-color-3 mb-0 f-500"])[1]')
        self.click_on_alter_particulars = (By.XPATH, '//*[@id="vchParticularsButton"]')
        self.godown_list_inside_alter_particulars = (
            By.XPATH, '(//*[@class="list-inside-div overflow-elipsis"])[1]//ancestor::ul//div')
        self.click_on_configurations = (By.XPATH,'//span[normalize-space(text())="Configurations"]')
        self.click_on_general = (By.XPATH,'//*[@id="VCHCDOUBLE"]')
        self.click_on_payment_voucher = (By.ID,"SUB_MODULE2")
        self.transcation_date_list = (By.XPATH,'//*[normalize-space(text())="Current Date"]//ancestor::ul//div')
        self.input_feild_voucher_date = (By.XPATH,'//input[@name="entryDate"]')
        self.click_on_kitaab_image = (By.XPATH,'//*[@class="c-sidebar-brand-full mobile-logo-width img-fluid inside-logo-full normal-theme-logo"]')
        self.click_on_yes_button = (By.XPATH,'//button[@id="ACCEP"]')
        self.click_on_transcations = (By.XPATH,'//button[@id="KIT2"]')
        self.voucher_date_in_sales_list = (By.XPATH,'(//input[@class="p-inputtext p-component p-filled"])[1]')

    def click_on_ledgers(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_create_button_locator = wait.until(
            EC.visibility_of_element_located(self.click_on_create_button))
        highlight_element(self.driver, click_on_create_button_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(
            click_on_create_button_locator).perform()

        # tool tip
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        tool_tip_locator = wait.until(
            EC.visibility_of_element_located(self.tool_tip))
        highlight_element(self.driver, tool_tip_locator)
        text = tool_tip_locator.text
        if tool_tip_locator.is_displayed():
            print(f"\033[93mTool tip for create button {text} is displayed\033[0m")
            Expected_text = "Create New ( F3 )"
            if text == Expected_text:
                print(f"\033[92mBoth {text} and {Expected_text} are equal\033[0m")
            else:
                print(f"both {text} and {Expected_text} are not  equal")
        else:
            print("Tool tip not displayed")
        # refresh button tool tip
        refresh_button_locator = wait.until(EC.visibility_of_element_located(self.refresh_button))
        highlight_element(self.driver, refresh_button_locator)
        actions.move_to_element(refresh_button_locator).perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        refresh_button_tool_tip_locator = wait.until(
            EC.visibility_of_element_located(self.refresh_button_tool_tip))
        highlight_element(self.driver, refresh_button_tool_tip_locator)
        text = refresh_button_tool_tip_locator.text
        if refresh_button_tool_tip_locator.is_displayed():
            print(f"\033[92mTool tip for refresh button {text} is displayed\033[0m")
            Expected_text = "Refresh ( Ctrl + R )"
            if text == Expected_text:
                print(f"\033[94mBoth {text} and {Expected_text} are equal\033[0m")
            else:
                print(f"both {text} and {Expected_text} are not  equal")
        else:
            print("Tool tip not displayed")

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_create_button_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_create_button))
        highlight_element(self.driver, click_on_create_button_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(
            click_on_create_button_locator).click().perform()

        # click on accounting vouchers and sales
        click_on_accounting_vouchers_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_accounting_vouchers))
        highlight_element(self.driver, click_on_accounting_vouchers_locator)
        click_on_accounting_vouchers_locator.click()
        time.sleep(2)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_sales_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_sales))
        highlight_element(self.driver, click_on_sales_locator)
        click_on_sales_locator.click()
        time.sleep(2)
        # click on particulars
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_alter_particulars_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_alter_particulars))
        highlight_element(self.driver, click_on_alter_particulars_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(click_on_alter_particulars_locator).click().perform()

        wait = WebDriverWait(self.driver, 50, poll_frequency=3, ignored_exceptions=[Exception])
        godown_list_inside_alter_particulars_lists = wait.until(
            EC.presence_of_all_elements_located(self.godown_list_inside_alter_particulars))
        print(len(godown_list_inside_alter_particulars_lists))

        Element_list = [element.text for element in godown_list_inside_alter_particulars_lists]
        length_of_element_list = len(Element_list)
        print(f"\033[92mElement_list:\033[0m",Element_list)

        for i in range(length_of_element_list):
            # Re-locate all elements in each iteration to avoid stale element reference
            wait = WebDriverWait(self.driver, 50, poll_frequency=3, ignored_exceptions=[Exception])
            godown_list_inside_alter_particulars_lists = wait.until(
                EC.presence_of_all_elements_located(self.godown_list_inside_alter_particulars))
            element1 = godown_list_inside_alter_particulars_lists[i]
            text_inside_godown_drop_down = element1.text
            actions = ActionChains(self.driver)
            actions.move_to_element(element1).perform()
            time.sleep(1)
            toop_tip_text = element1.get_attribute("title")
            print(f"\033[92mThe tool tip displayed is:\033[0m", toop_tip_text)
            time.sleep(0.5)
            highlight_element(self.driver, element1)
            actions.move_to_element(element1).click().perform()
            time.sleep(1)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(3)
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            godown_text_in_main_page_locator = wait.until(
                EC.presence_of_element_located(self.godown_text_in_main_page))
            highlight_element(self.driver, godown_text_in_main_page_locator)
            text_godown_main_page = godown_text_in_main_page_locator.text.split(' : ')[1]
            print(f"\033[93mText in godown main page:\033[0m", text_godown_main_page)
            time.sleep(2)
            if text_godown_main_page == text_inside_godown_drop_down:
                print(f"\033[94mBoth {text_godown_main_page} and {text_inside_godown_drop_down} are equal\033[0m")
            else:
                print(f"Both {text_godown_main_page} and {text_inside_godown_drop_down} are not equal")
            actions.send_keys(Keys.TAB).perform()
            wait = WebDriverWait(self.driver, 50, poll_frequency=3)
            click_on_alter_particulars_locator = wait.until(
                EC.element_to_be_clickable(self.click_on_alter_particulars))
            highlight_element(self.driver, click_on_alter_particulars_locator)
            actions.move_to_element(click_on_alter_particulars_locator).click().perform()
            time.sleep(2)

    def check_underline(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_create_button_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_create_button))
        highlight_element(self.driver, click_on_create_button_locator)
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnCreateButton", attachment_type=allure.attachment_type.PNG)
        actions = ActionChains(self.driver)
        actions.move_to_element(
            click_on_create_button_locator).click().perform()

        # click on accounting vouchers and sales
        click_on_accounting_vouchers_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_accounting_vouchers))
        highlight_element(self.driver, click_on_accounting_vouchers_locator)
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnAccountingVouchers",
                      attachment_type=allure.attachment_type.PNG)
        click_on_accounting_vouchers_locator.click()
        time.sleep(2)

        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_payment_voucher_locator = wait.until(
            EC.element_to_be_clickable(self.click_on_payment_voucher))
        highlight_element(self.driver, click_on_payment_voucher_locator)
        allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnSalesVoucher",
                      attachment_type=allure.attachment_type.PNG)
        click_on_payment_voucher_locator.click()
        time.sleep(2)

        # wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        # click_on_configurations_locator = wait.until(
        #     EC.presence_of_element_located(self.click_on_configurations))
        # highlight_element(self.driver, click_on_configurations_locator)
        # allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnConfigurationLocator",
        #               attachment_type=allure.attachment_type.PNG)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(
        #     click_on_configurations_locator).click().perform()



    def voucher_date_transcations(self):
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        click_on_general_locator = wait.until(
            EC.presence_of_element_located(self.click_on_general))

        color = click_on_general_locator.value_of_css_property("color")
        print(f"color:", color)
        # name = webcolors.rgb_to_name(color)
        # print(name)
        Bordercolor = click_on_general_locator.value_of_css_property("border-color")
        print(f"Bordercolor: {Bordercolor}")
        textdecorationcolor = click_on_general_locator.value_of_css_property("font-size")
        print(f"decorationcolor:", textdecorationcolor)
        wait = WebDriverWait(self.driver, 50, poll_frequency=3)
        transcation_date_list_locator = wait.until(
            EC.presence_of_all_elements_located(self.transcation_date_list))
        Element_list = [element.text for element in transcation_date_list_locator]
        length_of_element_list = len(Element_list)

        for i in range(length_of_element_list):
            transcation_date_list_locator = wait.until(
                EC.presence_of_all_elements_located(self.transcation_date_list))
            if i == 0:
                current_date = transcation_date_list_locator[0]
                highlight_element(self.driver, current_date)
                time.sleep(2)
                current_date.click()
                allure.attach(self.driver.get_screenshot_as_png(), name="CurrentDate",
                              attachment_type=allure.attachment_type.PNG)
                time.sleep(1)
                pyautogui.press('esc')
                time.sleep(2)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                input_feild_voucher_date_locator = wait.until(
                    EC.presence_of_element_located(self.input_feild_voucher_date))
                highlight_element(self.driver, input_feild_voucher_date_locator)
                allure.attach(self.driver.get_screenshot_as_png(), name="InputfeildVoucherDate",
                              attachment_type=allure.attachment_type.PNG)
                voucher_date_attribute_value = input_feild_voucher_date_locator.get_attribute("value")
                time.sleep(1)
                current_date1 = datetime.now().date()
                current_date_formatted = current_date1.strftime("%d/%m/%Y")
                print("Current Date:", current_date_formatted)
                if current_date_formatted == voucher_date_attribute_value:
                    print(f"Both {voucher_date_attribute_value} and {current_date_formatted} are same")
                else:
                    print(f"Both {voucher_date_attribute_value} and {current_date_formatted} are not same")
                time.sleep(2)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_configurations_locator = wait.until(
                    EC.presence_of_element_located(self.click_on_configurations))
                highlight_element(self.driver, click_on_configurations_locator)
                allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnConfiguration",
                              attachment_type=allure.attachment_type.PNG)
                actions = ActionChains(self.driver)
                actions.move_to_element(
                    click_on_configurations_locator).click().perform()
                time.sleep(2)
            if i == 1:
                Date_of_last_voucher = transcation_date_list_locator[1]
                highlight_element(self.driver, Date_of_last_voucher)
                Date_of_last_voucher.click()
                allure.attach(self.driver.get_screenshot_as_png(), name="DateOfLastVoucher",
                              attachment_type=allure.attachment_type.PNG)
                time.sleep(2)
                pyautogui.press('esc')
                time.sleep(2)
                voucher_date_attribute_value_date_of_last_voucher = (input_feild_voucher_date_locator
                                                                     .get_attribute("value"))
                time.sleep(2)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_kitaab_image_locator = wait.until(
                    EC.element_to_be_clickable(self.click_on_kitaab_image))
                highlight_element(self.driver, click_on_kitaab_image_locator)
                allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnKitaabImage",
                              attachment_type=allure.attachment_type.PNG)
                click_on_kitaab_image_locator.click()
                time.sleep(2)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_yes_button_locator = wait.until(
                    EC.presence_of_element_located(self.click_on_yes_button))
                highlight_element(self.driver, click_on_yes_button_locator)
                allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnYesButton",
                              attachment_type=allure.attachment_type.PNG)
                actions.move_to_element(click_on_yes_button_locator).click().perform()
                time.sleep(2)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_transcations_locator = wait.until(
                    EC.presence_of_element_located(self.click_on_transcations))
                highlight_element(self.driver, click_on_transcations_locator)
                allure.attach(self.driver.get_screenshot_as_png(), name="ClickOnTranscations",
                              attachment_type=allure.attachment_type.PNG)
                click_on_transcations_locator.click()
                time.sleep(2)
                pyautogui.press('s')
                time.sleep(2)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                voucher_date_in_sales_list_locator = wait.until(
                    EC.presence_of_element_located(self.voucher_date_in_sales_list))
                highlight_element(self.driver, voucher_date_in_sales_list_locator)
                allure.attach(self.driver.get_screenshot_as_png(), name="VoucherDateSalesList",
                              attachment_type=allure.attachment_type.PNG)
                Attribute_value_of_voucher_date_in_sales_list = (voucher_date_in_sales_list_locator.
                                                                 get_attribute("value"))
                time.sleep(1)
                if Attribute_value_of_voucher_date_in_sales_list==voucher_date_attribute_value_date_of_last_voucher:
                    print(f"Both {Attribute_value_of_voucher_date_in_sales_list} and "
                          f"{voucher_date_attribute_value_date_of_last_voucher} are equal")
                else:
                    print(f"Both {Attribute_value_of_voucher_date_in_sales_list} and "
                          f"{voucher_date_attribute_value_date_of_last_voucher} are not equal")
                time.sleep(1)
                self.driver.get("https://kitaabdev.finsights.biz/#/vouchers/new-create-sales")
                time.sleep(2)
                wait = WebDriverWait(self.driver, 50, poll_frequency=3)
                click_on_configurations_locator = wait.until(
                    EC.presence_of_element_located(self.click_on_configurations))
                highlight_element(self.driver, click_on_configurations_locator)
                actions.move_to_element(
                    click_on_configurations_locator).click().perform()
            if i == 2:
                none = transcation_date_list_locator[2]
                highlight_element(self.driver, none)
                none.click()
                time.sleep(2)
                allure.attach(self.driver.get_screenshot_as_png(), name="ClickNone",
                              attachment_type=allure.attachment_type.PNG)
                time.sleep(2)
                pyautogui.press("esc")






























            
