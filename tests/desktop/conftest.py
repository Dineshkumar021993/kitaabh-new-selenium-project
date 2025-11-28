import time


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="module")
def browser():
    # FULL DESKTOP APP
    # options = Options()
    # options.page_load_strategy = 'normal'  # IT DETERMINES WHETHER THE PAGE IS FULLY LOADED OR NOT
    # # options.binary_location = "D:\\NewSeleniumProject\\drivers\\Application\\Kitaabh 0.0.488.exe"
    # options.binary_location = "D:\\NewSeleniumProject\\drivers\\Application\\Kitaabh-Dev 0.0.832.exe"
    # service_object = Service(
    #     executable_path="D:\\NewSeleniumProject\\drivers\\chromedriver\\chromedriver.exe")
    # driver = webdriver.Chrome(options=options, service=service_object)

    # FULL WEB APPLICATION
    options = Options()
    service_object = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service_object)
    # url = "https://app.kitaabh.com"
    url = "https://d3ldvcrr82x82a.cloudfront.net/"
    driver.get(url)
    driver.maximize_window()
    yield driver  # Provide the driver object to all test cases
    time.sleep(3)
    driver.quit()  # Teardown: Close the driver at the end of the session


# @pytest.fixture(scope="function", autouse=True)
# def ss_before_after(request, browser):
#     # driver, _ = browser
#     test_name = request.node.name
#
#     # Define the screenshot directory
#     screenshot_dir_before = "screenshots/before_each"
#     screenshot_dir_after = "screenshots/after_each"
#
#     # Create the directories if they don't exist
#     os.makedirs(screenshot_dir_before, exist_ok=True)
#     os.makedirs(screenshot_dir_after, exist_ok=True)
#
#     # Capture the screenshot before the test
#     screenshot_path_before = f"{screenshot_dir_before}/{test_name}.png"
#     browser.save_screenshot(screenshot_path_before)
#     allure.attach.file(screenshot_path_before, name="Screenshot Before Test",
#                        attachment_type=allure.attachment_type.PNG)
#     yield
#     # Capture the screenshot after the test
#     screenshot_path_after = f"{screenshot_dir_after}/{test_name}.png"
#     browser.save_screenshot(screenshot_path_after)
#     allure.attach.file(screenshot_path_after, name="Screenshot After Test", attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope="function")
def appium_driver(request, pytestconfig):
    # Desired capabilities for your mobile app
    desired_caps = {
        "platformName": "Android",  # Change to "iOS" if testing on iOS
        "platformVersion": "12.0",  # Change to the desired version
        "deviceName": "kitaabDesktopandMobile",  # Change to your device name
        # Replace with the path to your APK
        # "app": "D:\\kitaab-desktop-app-and-mobile-testing\\drivers\\desktop\\app.apk",
        "app": "D:\\kitaab-desktop-app-and-mobile-testing\\drivers\\Application\\Kitaab(15Feb2024) (1).apk",
        "automationName": "UiAutomator2",
        "appPackage": "in.lotusinsights.kitaab",
        "appActivity": "in.lotusinsights.kitaab.MainActivity"
        # "appActivity": "in.lotusinsights.kitaab.NexusLauncherActivity"
        # Add more desired capabilities as needed
    }

    # Appium server URL
    # Replace with your Appium server URL
    appium_server_url = "http://localhost:4723"

    # Get the test case name
    test_case_name = request.node.name

    # Initialize the Appium driver
    # driver = appium_webdriver.Remote(appium_server_url, desired_caps)

    # def capture_screenshot(name):
    #     driver.save_screenshot(name)
    #     allure.attach(driver.get_screenshot_as_png(), name=os.path.join(report_path, name),
    #                   attachment_type=allure.attachment_type.PNG)
    #
    # # Capture a screenshot before test execution with a unique name
    # before_screenshot_name = f"before_{test_case_name}.png"
    # capture_screenshot(before_screenshot_name)
    #
    # yield driver  # Provide the driver object to all test cases
    #
    # # Capture a screenshot after test execution with a unique name
    # after_screenshot_name = f"after_{test_case_name}.png"
    # capture_screenshot(after_screenshot_name)
    #
    # request.node.screenshot_before = before_screenshot_name
    # request.node.screenshot_after = after_screenshot_name
    #
    # # Teardown: Quit the driver at the end of the session
    # driver.quit()
    # page_counter = [1]

    # def capture_screenshot(name):
    #     driver.save_screenshot(name)
    #     allure.attach(driver.get_screenshot_as_png(), name=os.path.join(report_path, name),
    #                   attachment_type=allure.attachment_type.PNG)
    #
    # yield driver
    #
    # current_page_screenshot_name = f"{test_case_name}_page_{page_counter}.png"
    # capture_screenshot(current_page_screenshot_name)
    # request.node.screenshot_current_page = current_page_screenshot_name
    # page_counter[0] += 1
    #
    # driver.quit()

    # def capture_screenshot(name):
    #     screenshot_path = os.path.join(report_path, name)
    #     driver.save_screenshot(screenshot_path)
    #     allure.attach.file(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)
    #
    # yield driver
    #
    # current_page_screenshot_name = f"{test_case_name}_page_{page_counter[0]}.png"
    # capture_screenshot(current_page_screenshot_name)
    # request.node.screenshot_current_page = current_page_screenshot_name
    # page_counter[0] += 1
    #
    # # Teardown: Quit the driver at the end of the session
    # driver.quit()
