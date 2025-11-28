import pytest
import allure
from playwright.sync_api import sync_playwright,TimeoutError as PlaywrightTimeoutError


def attach_screenshot(page, name):
    """Take a screenshot and attach to Allure report."""
    allure.attach(page.screenshot(), name=name, attachment_type=allure.attachment_type.PNG)


@allure.title("Create Opening Balance with Full Workflow")
@allure.description("Test creates opening balance and captures screenshot at every step")
@allure.severity(allure.severity_level.CRITICAL)
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://d3ldvcrr82x82a.cloudfront.net/#/login")
    page.get_by_role("textbox", name="Email Address or Mobile Number").click()
    page.get_by_role("textbox", name="Email Address or Mobile Number").click()
    page.get_by_role("textbox", name="Email Address or Mobile Number").fill("venu.k@kitaab.biz")
    page.get_by_test_id("password-input").click()
    page.get_by_test_id("password-input").click()
    page.get_by_test_id("password-input").fill("Venu@123")
    page.get_by_test_id("sign-in-verify").click()
    page.get_by_role("button", name=" GST Alt + G Your GST").click()
    page.get_by_role("button", name=" E-Way Bill W").click()
    page.get_by_role("textbox", name="From Date").click()
    page.get_by_role("button", name="October").click()
    page.get_by_text("Apr").click()
    page.get_by_text("1", exact=True).nth(2).click()
    page.get_by_role("button", name=" Fetch").click()
    page.locator("#header-org-dropdown div").nth(1).click()
    page.get_by_text("29AAGCB1286Q000").nth(1).click()
    page.get_by_role("button", name=" E-Way Bill W").click()
    page.get_by_role("textbox", name="From Date").click()
    page.get_by_role("button", name="October").click()
    page.get_by_text("Apr").click()
    page.get_by_text("1", exact=True).first.click()
    page.get_by_role("button", name=" Fetch").click()
    page.get_by_role("combobox", name="Select").click()
    page.get_by_text("Expired").click()
    page.locator("div").filter(has_text=re.compile(r"^E-Way BillLogin Credentials$")).first.click()
    page.get_by_role("row", name="Outward Tax Invoice Sales 10/09/2025 Sale-912309350 zyna 37AACCL6889R1ZC vizag").locator("div").nth(2).click()
    page.get_by_role("row", name=" Outward Tax Invoice Sales").get_by_role("button").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("combobox", name="Select").click()
    page.get_by_text("Generated", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
