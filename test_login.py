import json
import pytest
from pages.login_page import LoginPage

with open('./data/credentials.json') as f:
    creds = json.load(f)

@pytest.mark.parametrize("user", creds["valid"])
def test_valid_login(driver, user):
    driver.get("https://www.saucedemo.com/v1/")
    login = LoginPage(driver)
    login.login(user["username"], user["password"])
    assert "inventory.html" in driver.current_url

@pytest.mark.parametrize("user", creds["invalid"])
def test_invalid_login(driver, user):
    driver.get("https://www.saucedemo.com/v1/")
    login = LoginPage(driver)
    login.login(user["username"], user["password"])
    assert "inventory.html" not in driver.current_url
