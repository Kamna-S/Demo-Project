from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.product_names = (By.CLASS_NAME, "inventory_item_name")
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def sort_products_low_to_high(self):
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_visible_text("Price (low to high)")

    def get_all_product_names(self):
        return [elem.text for elem in self.driver.find_elements(*self.product_names)]

    def add_first_product_to_cart(self):
        self.driver.find_elements(*self.add_to_cart_buttons)[0].click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
