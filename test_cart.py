import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture(scope="function", autouse=True)
def take_screenshot_on_failure(driver, request):
    """
    This fixture will automatically capture a screenshot if the test fails
    and attach it to the Allure report.
    """
    yield
    if request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )

@allure.story('Product Filtering')
@allure.severity(allure.severity_level.NORMAL)
def test_product_filtering(driver):
    """
    Test case to verify product filtering by price (low to high) on the Saucedemo website.
    """

    # Step 1: Login
    driver.get("https://www.saucedemo.com/v1/")
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    allure.step("User logged in successfully")

    # Step 2: Sort products by price (Low to High)
    inventory = InventoryPage(driver)
    inventory.sort_products_low_to_high()
    allure.step("Applied 'Price (low to high)' filter to the products")

    # Step 3: Get and print product names
    product_names = inventory.get_all_product_names()
    allure.step("Retrieved the list of product names after sorting")

    # Print product names
    print("\n==================== Product Names (Low to High) ====================")
    for i, name in enumerate(product_names, 1):
        print(f"{i}. {name}")
    print("=========================================================")

    # Assertion
    assert len(product_names) > 0, "No products found after_"
