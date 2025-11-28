from pages.desktop.login_page import LoginPage
from pages.desktop.Newsales03 import Sales


def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)
    # Navigate to the login page

    login_page.enter_username()
    login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()


def test_new_sales_03(browser):
    sales_page_landing = Sales(browser)
    sales_page_landing.change_organisation()
    sales_page_landing.Click_CreateButton_On_MainPage()
    sales_page_landing.Click_accounting_transcations_in_create_sales()
    sales_page_landing.Click_accounting_transcations_sales_in_create_sales()
    sales_page_landing.check_inventory_button()
    sales_page_landing.customer_details_dropdown()
    sales_page_landing.click_on_list()
    sales_page_landing.click_on_godown_list()
    sales_page_landing.order_no_list_overall()
    sales_page_landing.effective_date()
    sales_page_landing.items_and_ledgers()
    sales_page_landing.check_item_name_list_in_stock_items()
    sales_page_landing.mouse_hover_on_sales_ledger()
    sales_page_landing.check_unit_dropdown_in_add_stock_item()
    # sales_page_landing.rupee_list()
    # sales_page_landing.rate_feild()
    sales_page_landing.order_no()
    sales_page_landing.create_new_order_no()
    sales_page_landing.godown_in_quantity_and_prices()
    sales_page_landing.batch_no_total()
    sales_page_landing.Actual_quantity()
    sales_page_landing.Actual_quantity()
    sales_page_landing.unit_price_column()
    sales_page_landing.discount()

