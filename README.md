# Web App Test Automation Framework

A Python-based test automation framework for testing web applications using Selenium, Pytest, API testing, and SQLite database validation.

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Requests
- SQLite
- Page Object Model (POM)
- Git & GitHub

## Project Structure

```text
WebApp-Test-Automation/
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   └── cart_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_api.py
│   └── test_database.py
│
├── utils/
│   └── database.py
│
├── .gitignore
└── README.md

Testing Areas
1. UI Automation
Selenium WebDriver is used to automate the SauceDemo web application.
The tests cover:
- Valid login
- Invalid login
- Empty username/password validation
- Navigation to the products page
- Adding a product to the cart
- Verifying cart items
2. API Testing
API tests are implemented using Python requests.
The framework tests:
- GET user
- POST/create user
- Invalid user request
- PUT/update user
- DELETE user
3. Database Testing
SQLite is used for database validation.
The database test verifies:
- User existence
- Username
- Email
4. Page Object Model
The framework follows the Page Object Model design pattern.
Page classes include:
- LoginPage
- ProductsPage
- CartPage
This separates page locators and actions from test cases and improves maintainability.
Running the Tests
Activate the virtual environment and run:
pytest tests

To run only the API tests:
pytest tests/test_api.py

To run only the UI tests:
pytest tests/test_login.py

To run database tests:
pytest tests/test_database.py

Test Results
The complete test suite contains:
- 5 API tests
- 7 UI tests
- 1 database test
Total:
13 tests
All tests pass successfully.
13 passed

Author
Vaishnavi Singh
B.Tech CSE (AI & ML)

