from pages.desktop.groups_shortcuts import Groups
from pages.desktop.login_page import LoginPage
from pages.desktop.groups_shortcuts import CostCentres

from pages.desktop.groups_shortcuts import CostCategories
from pages.desktop.groups_shortcuts import CostCentreClass
from pages.desktop.groups_shortcuts import Currency
from pages.desktop.groups_shortcuts import Ledgers
from pages.desktop.groups_shortcuts import TranscationTypeList
from pages.desktop.groups_shortcuts import RateOfExchange


def test_successful_login(browser):
    # Initialize LoginPage
    login_page = LoginPage(browser)

    # Navigate to the login page
    login_page.enter_username()
    login_page.click_NextButton()
    login_page.enter_password()
    login_page.click_login_button()


def test_ledgers_list(browser):
    ledgers = Ledgers(browser)
    ledgers.click_on_kitaab_image()
    ledgers.ledgers_list_elements()


def test_groups_list(browser):
    groups_list = Groups(browser)
    groups_list.groups_list()


def test_cost_centres_list(browser):
    cost_centres_list = CostCentres(browser)
    cost_centres_list.click_on_kitaab_image()
    cost_centres_list.cost_centres_list()


# def test_all_accounting_masters(browser):
#     all_accounting_masters_lists = AllAccountingMasters(browser)
#     all_accounting_masters_lists.click_on_kitaab_image()
#     all_accounting_masters_lists.all_accounting_masters()

def test_cost_categories(browser):
    cost_categories_list = CostCategories(browser)
    cost_categories_list.click_on_kitaab_image()
    cost_categories_list.cost_categories_list_elements()


def test_cost_centre_class(browser):
    cost_centre_class_list = CostCentreClass(browser)
    cost_centre_class_list.click_on_kitaab_image()
    cost_centre_class_list.cost_center_class_list_elements()


def test_currency(browser):
    currency_lists = Currency(browser)
    currency_lists.click_on_kitaab_image()
    currency_lists.currency_list_elements()


def test_transcation_type(browser):
    transcation_type_list = TranscationTypeList(browser)
    transcation_type_list.click_on_kitaab_image()
    transcation_type_list.transcation_type_list_elements()


def test_rate_of_exchange(browser):
    rate_of_exchange = RateOfExchange(browser)
    rate_of_exchange.click_on_kitaab_image()
    rate_of_exchange.rate_of_exchange_elements()
