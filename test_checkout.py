import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkout_process(driver):
    # Use the correct URL
    driver.get("https://www.saucedemo.com/v1/")
    
    # Login
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    
    # Add product and go to cart
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))
    ).click()
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    ).click()
    
    # Click checkout
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_action.checkout_button"))
    ).click()

    # Fill in user details
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#first-name"))
    ).send_keys("Kamna")
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#last-name"))
    ).send_keys("Singh")
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#postal-code"))
    ).send_keys("12345")
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='CONTINUE']"))
    ).click()

    # Finish the order
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_action.cart_button"))
    ).click()

    # Assert confirmation message
    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text
    
