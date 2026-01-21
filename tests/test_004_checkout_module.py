import json
import pytest
from pages.login_module import LoginPage
from pages.checkout_module import CheckModule
from pathlib import Path

base_url = "https://www.saucedemo.com"

BASE_DIR = Path(__file__).resolve().parent.parent
test_data_path = BASE_DIR / "utils" / "test_login.json"

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


# -------------------------------
# TC_CHECKOUT_001
# -------------------------------
@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.tc_checkout_001
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_proceed_to_checkout_from_cart(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    checkout_module = CheckModule(driver)
    current_url = checkout_module.get_checkout_page()
    expected_url = "https://www.saucedemo.com/checkout-step-one.html"
    assert current_url == expected_url


# -------------------------------
# TC_CHECKOUT_002
# -------------------------------
@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.tc_checkout_002
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_complete_checkout_with_valid_user_information(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    checkout_module = CheckModule(driver)
    username = "John"
    lastname = "Doe"
    postalcode = "12345"
    current_url, current_error = checkout_module.fill_the_form(username, lastname, postalcode)
    expected_error ="None"
    expected_url = "https://www.saucedemo.com/checkout-step-two.html"
    assert current_url == expected_url and expected_error == current_error


# -------------------------------
# TC_CHECKOUT_003
# -------------------------------
@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.tc_checkout_003
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_view_order_overview_before_confirmation(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    checkout_module = CheckModule(driver)
    username = "John"
    lastname = "Doe"
    postalcode = "12345"
    checkout_module.fill_the_form(username, lastname, postalcode)
    info_len = checkout_module.cart_overview()
    assert info_len > 0


# -------------------------------
# TC_CHECKOUT_004
# -------------------------------
@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.tc_checkout_004
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_complete_order(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    checkout_module = CheckModule(driver)
    username = "John"
    lastname = "Doe"
    postalcode = "12345"
    checkout_module.fill_the_form(username, lastname, postalcode)
    checkout_module.cart_overview()
    current_url = checkout_module.complete_order()
    expected_url = "https://www.saucedemo.com/checkout-complete.html"
    assert current_url == expected_url


# -------------------------------
# TC_CHECKOUT_005
# -------------------------------
@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.tc_checkout_005
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_complete_order_confirmation_message(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    checkout_module = CheckModule(driver)
    username = "John"
    lastname = "Doe"
    postalcode = "12345"
    checkout_module.fill_the_form(username, lastname, postalcode)
    checkout_module.cart_overview()
    checkout_module.complete_order()
    actual_confirmation_message = checkout_module.confirmation_message()
    expected_confirmation_message = "Thank you for your order!"
    assert actual_confirmation_message == expected_confirmation_message

# -------------------------------
# TC_CHECKOUT_006
# -------------------------------
@pytest.mark.checkout
@pytest.mark.tc_checkout_006
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_cannot_complete_checkout_without_valid_username(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    checkout_module = CheckModule(driver)
    username = ""
    lastname = "Doe"
    postalcode = "12345"
    current_url, current_error = checkout_module.fill_the_form(username, lastname, postalcode)
    expected_error = "Error: First Name is required"
    expected_url = "https://www.saucedemo.com/checkout-step-two.html"
    assert current_url != expected_url and expected_error == current_error


# -------------------------------
# TC_CHECKOUT_007
# -------------------------------
@pytest.mark.checkout
@pytest.mark.tc_checkout_007
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_cannot_complete_checkout_without_valid_lastname(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    checkout_module = CheckModule(driver)
    username = "John"
    lastname = ""
    postalcode = "12345"
    current_url, current_error = checkout_module.fill_the_form(username, lastname, postalcode)
    expected_error = "Error: Last Name is required"
    expected_url = "https://www.saucedemo.com/checkout-step-two.html"
    assert current_url != expected_url and expected_error == current_error


# -------------------------------
# TC_CHECKOUT_008
# -------------------------------
@pytest.mark.checkout
@pytest.mark.tc_checkout_008
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_cannot_complete_checkout_without_valid_postcode(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    checkout_module = CheckModule(driver)
    username = "John"
    lastname = "Doe"
    postalcode = ""
    current_url, current_error = checkout_module.fill_the_form(username, lastname, postalcode)
    expected_error = "Error: Postal Code is required"
    expected_url = "https://www.saucedemo.com/checkout-step-two.html"
    assert current_url != expected_url and expected_error == current_error


# -------------------------------
# TC_CHECKOUT_009
# -------------------------------
@pytest.mark.checkout
@pytest.mark.tc_checkout_009
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_cannot_complete_checkout_without_information(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    checkout_module = CheckModule(driver)
    username = ""
    lastname = ""
    postalcode = ""
    current_url, current_error = checkout_module.fill_the_form(username, lastname, postalcode)
    expected_error = "Error: First Name is required"
    expected_url = "https://www.saucedemo.com/checkout-step-two.html"
    assert current_url != expected_url and expected_error == current_error

