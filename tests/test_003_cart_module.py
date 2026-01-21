import json
import pytest
from pages.login_module import LoginPage
from pages.cart_module import  CartModule
from pathlib import Path

base_url = "https://www.saucedemo.com"

BASE_DIR = Path(__file__).resolve().parent.parent
test_data_path = BASE_DIR / "utils" / "test_login.json"

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


# -------------------------------
# TC_CART_001
# -------------------------------
@pytest.mark.cart
@pytest.mark.tc_cart_001
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_add_all_products_to_cart_via_add_to_cart_button_on_inventory_page(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    cart_module = CartModule(driver)
    cart_element_count, cart_badge_element_number, remove_count = cart_module.add_to_cart_inventory_page()
    assert cart_element_count == cart_badge_element_number == remove_count


# -------------------------------
# TC_CART_002
# -------------------------------
@pytest.mark.cart
@pytest.mark.tc_cart_002
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_add_all_products_to_cart_via_add_to_cart_button_on_inventory_item_page(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    cart_module = CartModule(driver)
    cart_element_count,  cart_badge_element_number, remove_count = cart_module.add_to_cart_inventory_item_page()
    assert cart_element_count ==  cart_badge_element_number == remove_count


# -------------------------------
# TC_CART_003
# -------------------------------
@pytest.mark.cart
@pytest.mark.tc_cart_003
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_remove_all_products_to_cart_via_remove_button_on_inventory_page(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    cart_module = CartModule(driver)
    cart_module.add_to_cart_inventory_page()
    inventory_product_elements_count, cart_badge_element_number, remove_count, add_to_cart_count = cart_module.remove_from_cart_inventory_page()
    assert inventory_product_elements_count == remove_count == add_to_cart_count and (cart_badge_element_number == 0)


# # -------------------------------
# TC_CART_004
# -------------------------------
@pytest.mark.cart
@pytest.mark.tc_cart_004
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_remove_all_products_to_cart_via_remove_button_on_inventory_item_page(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    cart_module = CartModule(driver)
    cart_module.add_to_cart_inventory_item_page()
    inventory_product_elements_count, cart_badge_element_number, remove_count, add_to_cart_count = cart_module.remove_from_cart_inventory_item_page()
    assert inventory_product_elements_count == remove_count  == add_to_cart_count and (cart_badge_element_number == 0)


# # -------------------------------
# TC_CART_005
# -------------------------------
@pytest.mark.cart
@pytest.mark.tc_cart_005
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_remove_item_from_the_cart_on_your_cart_page(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    cart_module = CartModule(driver)
    cart_badge_element_number, cart_status = cart_module.remove_element_from_cart_page()
    assert cart_badge_element_number == 0 and cart_status == "Empty"
