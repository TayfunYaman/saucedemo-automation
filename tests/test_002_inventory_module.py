import json
import pytest
from pages.login_module import LoginPage
from pages.inventory_page import InventoryModule
from pathlib import Path

base_url = "https://www.saucedemo.com"

BASE_DIR = Path(__file__).resolve().parent.parent
test_data_path = BASE_DIR / "utils" / "test_login.json"

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


# -------------------------------
# TC_INVENTORY_001
# -------------------------------
@pytest.mark.inventory
@pytest.mark.smoke
@pytest.mark.tc_inventory_001
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_see_product_list_after_successful_login(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    inventory_module = InventoryModule(driver)
    product_list = inventory_module.product_check()
    assert len(product_list) > 0


# -------------------------------
# TC_INVENTORY_002
# -------------------------------
@pytest.mark.inventory
@pytest.mark.tc_inventory_002
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_sort_products_by_price_low_high(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    inventory_module = InventoryModule(driver)
    actual_products = inventory_module.sort_products("lohi")
    sorted_products = sorted(actual_products, reverse=False)
    assert actual_products == sorted_products


# -------------------------------
# TC_INVENTORY_003
# -------------------------------
@pytest.mark.inventory
@pytest.mark.tc_inventory_003
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_sort_products_by_price_high_low(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    inventory_module = InventoryModule(driver)
    actual_products = inventory_module.sort_products("hilo")
    sorted_products = sorted(actual_products, reverse=True)
    assert actual_products == sorted_products


# -------------------------------
# TC_INVENTORY_004
# -------------------------------
@pytest.mark.inventory
@pytest.mark.tc_inventory_004
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_sort_products_by_name_a_z(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    inventory_module = InventoryModule(driver)
    inventory_module.sort_products("za")
    actual_products = inventory_module.sort_products("za")
    sorted_products = sorted(actual_products, reverse=True)
    assert actual_products == sorted_products
    actual_products = inventory_module.sort_products("az")
    sorted_products = sorted(actual_products, reverse=False)
    assert actual_products == sorted_products


# -------------------------------
# TC_INVENTORY_005
# -------------------------------
@pytest.mark.inventory
@pytest.mark.tc_inventory_005
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_sort_products_by_name_z_a(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    inventory_module = InventoryModule(driver)
    actual_products = inventory_module.sort_products("za")
    sorted_products = sorted(actual_products, reverse=True)
    assert actual_products == sorted_products


# -------------------------------
# TC_INVENTORY_006
# -------------------------------
@pytest.mark.inventory
@pytest.mark.tc_inventory_006
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_iew_product_item_page_via_product_name(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    inventory_module = InventoryModule(driver)
    item_page_names, inventory_page_names = inventory_module.item_page_via_name()
    assert item_page_names == inventory_page_names


# -------------------------------
# TC_INVENTORY_007
# -------------------------------
@pytest.mark.inventory
@pytest.mark.tc_inventory_007
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_can_iew_product_item_page_via_product_picture(driver, test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    inventory_module = InventoryModule(driver)
    item_page_names, inventory_page_names = inventory_module.item_page_via_name()
    print( item_page_names, inventory_page_names)
    assert item_page_names == inventory_page_names


