from selenium.webdriver.support.ui import Select
from pages.login_page import LoginPage
import time

def test_product_filtering(driver):
    # Step 1: Login
    driver.get("https://www.saucedemo.com/v1/")
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    # Step 2: Apply filter "Price (low to high)"
    dropdown = driver.find_element("class name", "product_sort_container")
    sort = Select(dropdown)
    sort.select_by_visible_text("Price (low to high)")

    # Step 3: Wait a moment (optional)
    time.sleep(2)

    # Step 4: Get product name elements
    product_elements = driver.find_elements("class name", "inventory_item_name")
    
    # Step 5: Extract names and store in list
    product_names = [element.text for element in product_elements]

    # Step 6: Print the names clearly
    print("\n==================== Product Names (Low to High) ====================")
    for index, name in enumerate(product_names, start=1):
        print(f"{index}. {name}")
    print("=====================================================================")

    # Optional Assertion
    assert len(product_names) > 0
