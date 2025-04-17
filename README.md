
# 🧪 SauceDemo Automation – Test Plan Document

## 📌 Project Overview
This automation project covers the functional testing of the [SauceDemo](https://www.saucedemo.com/) web application. The goal is to validate core features like login, product sorting, cart operations, and checkout using Selenium, PyTest, and HTML reporting tools.

---

## 🧪 Test Scenarios

| Test ID | Scenario Description              | Expected Outcome                             | Test Type |
|---------|-----------------------------------|-----------------------------------------------|-----------|
| TC001   | Login with valid credentials      | User should be redirected to the inventory page | Positive  |
| TC002   | Login with invalid password       | Error message should be displayed             | Negative  |
| TC003   | Product filtering (Low to High)   | Products should be sorted in ascending price  | Positive  |
| TC004   | Add to Cart                       | Item should be added to the cart              | Positive  |
| TC005   | Checkout with valid user details  | Checkout should complete successfully         | Positive  |
| TC006   | Checkout with missing information | Error message should be shown                 | Negative  |

---

## 📋 Positive & Negative Test Cases

### ✅ TC001 – Login with Valid Credentials
**Steps**:
- Navigate to [https://www.saucedemo.com/](https://www.saucedemo.com/)
- Enter username: `standard_user`
- Enter password: `secret_sauce`
- Click login

**Expected**: Redirect to `inventory.html`  
**Type**: Positive

---

### ❌ TC002 – Login with Invalid Credentials
**Steps**:
- Enter username: `standard_user`
- Enter password: `wrong_pass`
- Click login

**Expected**: Error message: `Epic sadface: Username and password do not match`  
**Type**: Negative

---

### ✅ TC003 – Filter Products by Price (Low to High)
**Steps**:
- Login
- Select filter dropdown
- Choose `Price (low to high)`

**Expected**: Product list sorted by price ascending  
**Type**: Positive

---

### ✅ TC004 – Add Product to Cart
**Steps**:
- Login
- Click "Add to cart" on any product
- Open cart

**Expected**: Product appears in cart  
**Type**: Positive

---

### ✅ TC005 – Checkout with Valid Details
**Steps**:
- Add item to cart
- Click checkout
- Enter First name, Last name, Zip
- Continue and finish

**Expected**: “Thank you for your order!” confirmation  
**Type**: Positive

---

### ❌ TC006 – Checkout Without Filling Fields
**Steps**:
- Add item
- Click checkout
- Leave fields empty
- Click continue

**Expected**: Error: “Error: First Name is required”  
**Type**: Negative

---

## 🧪 Test Data

### Login Credentials

| Username        | Password      | Type    |
|----------------|---------------|---------|
| standard_user   | secret_sauce  | Valid   |
| standard_user   | wrong_pass    | Invalid |
| locked_out_user | secret_sauce  | Invalid |

### Checkout Info

| First Name | Last Name | Zip Code | Valid? |
|------------|-----------|----------|--------|
| Kamna      | Singh     | 12345    | Yes    |
|            | Singh     | 12345    | No     |

---

## 🖥️ Environment Setup Instructions

### 🔧 Prerequisites
- Python 3.8+
- pip (Python package manager)
- Google Chrome
- ChromeDriver (compatible version)

---

### 📁 Folder Structure
```
VE3/
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
├── tests/
│   ├── test_login.py
│   ├── test_checkout.py
│   ├── test_cart.py
│   ├── test_filter.py
├── screenshots/
├── reports/
├── conftest.py
├── requirements.txt
```

---

### 📦 Installation

```bash
pip install -r requirements.txt
```

**requirements.txt** should include:
```
selenium
pytest
pytest-html
```

---

### ▶️ To Run Tests with HTML Report:

```bash
pytest --html=reports/report.html --self-contained-html
```
![image](https://github.com/user-attachments/assets/b78abefc-ffc9-4b9c-81f2-cfef567815f6)

---
