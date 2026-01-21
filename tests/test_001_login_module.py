import json
import pytest
from pages.login_module import LoginPage
from selenium.webdriver.common.by import By
from pathlib import Path

base_url = "https://www.saucedemo.com"

BASE_DIR = Path(__file__).resolve().parent.parent
test_data_path = BASE_DIR / "utils" / "test_login.json"

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


# -------------------------------
# TC_LOGIN_001
# -------------------------------
@pytest.mark.login
@pytest.mark.smoke
@pytest.mark.tc_login_001
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_logs_in_with_valid_credentials(driver,test_list_item):
    username = test_list_item["username"]
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, password)
    current_url = driver.current_url
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert current_url == expected_url


# -------------------------------
# TC_LOGIN_002
# -------------------------------
@pytest.mark.login
@pytest.mark.tc_login_002
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_cannot_log_in_with_invalid_username(driver,test_list_item):
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login("kalabakbalbala4", password)
    current_url = driver.current_url
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert current_url != expected_url
    current_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    current_error_text = current_error.text
    expected_error_text = "Epic sadface: Username and password do not match any user in this service"
    assert current_error_text == expected_error_text


# -------------------------------
# TC_LOGIN_003
# -------------------------------
@pytest.mark.login
@pytest.mark.tc_login_003
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_cannot_log_in_with_invalid_password(driver,test_list_item):
    login_page = LoginPage(driver)
    username = test_list_item["username"]
    login_page.open_page(base_url)
    login_page.login(username, "hebelehubele")
    current_url = driver.current_url
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert current_url != expected_url
    current_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    current_error_text = current_error.text
    expected_error_text = "Epic sadface: Username and password do not match any user in this service"
    assert current_error_text == expected_error_text


# -------------------------------
# TC_LOGIN_004
# -------------------------------
@pytest.mark.login
@pytest.mark.tc_login_004
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_cannot_log_in_with_empty_username(driver,test_list_item):
    password = test_list_item["password"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login("", password)
    current_url = driver.current_url
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert current_url != expected_url
    current_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    current_error_text = current_error.text
    expected_error_text = "Epic sadface: Username is required"
    assert current_error_text == expected_error_text


# -------------------------------
# TC_LOGIN_005
# -------------------------------
@pytest.mark.login
@pytest.mark.tc_login_005
@pytest.mark.parametrize("test_list_item", test_list)
def test_user_cannot_log_in_with_empty_password(driver,test_list_item):
    username = test_list_item["username"]
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.login(username, "")
    current_url = driver.current_url
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert current_url != expected_url
    current_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    current_error_text = current_error.text
    expected_error_text = "Epic sadface: Password is required"
    assert current_error_text == expected_error_text


# -------------------------------
# TC_LOGIN_006
# -------------------------------
@pytest.mark.login
@pytest.mark.tc_login_006
@pytest.mark.parametrize("test_list_item", test_list)
def test_locked_user_cannot_log_in(driver,test_list_item):
    login_page = LoginPage(driver)
    password = test_list_item["password"]
    login_page.open_page(base_url)
    login_page.login("locked_out_user", password)
    current_url = driver.current_url
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert current_url != expected_url
    current_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    current_error_text = current_error.text
    expected_error_text = "Epic sadface: Sorry, this user has been locked out."
    assert current_error_text == expected_error_text


# -------------------------------
# TC_LOGIN_007
# -------------------------------
@pytest.mark.login
@pytest.mark.tc_login_007
@pytest.mark.parametrize("test_list_item", test_list)
def test_sql_injection_attempt_on_username_field(driver, test_list_item):
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    password = test_list_item["password"]
    login_page.login("admin' OR '1'='1", "anything")
    current_url = driver.current_url
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert current_url != expected_url
    current_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    current_error_text = current_error.text
    expected_error_text = "Epic sadface: Username and password do not match any user in this service"
    assert current_error_text == expected_error_text