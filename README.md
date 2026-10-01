# Web App Test Automation Framework

A Python-based test automation framework combining Selenium UI automation, REST API testing, and SQLite database validation using Pytest.

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
├── README.md
└── requirements.txt

Key Features
UI Test Automation
Selenium WebDriver is used to automate the SauceDemo web application.
The UI test suite covers:
- Valid login
- Invalid login
- Empty login validation
- Missing password validation
- Navigation to the products page
- Adding a product to the cart
- Verifying cart contents
API Test Automation
REST API testing is implemented using Python requests.
The API test suite covers:
- GET user
- Create user
- Invalid user request
- Update user
- Delete user
Database Testing
SQLite is used for database validation.
The database test verifies:
- User existence
- Username
- Email
Page Object Model
The framework uses the Page Object Model to separate page-specific locators and actions from test cases.
Page classes include:
- LoginPage
- ProductsPage
- CartPage
This makes the test framework easier to maintain and reuse.
Pytest Fixtures
Reusable test setup and browser configuration are handled through Pytest fixtures in conftest.py.
Test Results
The complete test suite contains 13 automated tests.
Test Area	Tests	Result
API Testing	5	✅ 5 Passed
UI Testing	7	✅ 7 Passed
Database Testing	1	✅ 1 Passed
Total	13	✅ 13 Passed


How to Run
1. Clone the repository
git clone https://github.com/Vaish-prog/WebApp-Test-Automation.git
cd WebApp-Test-Automation

2. Create a virtual environment
python -m venv .venv

3. Activate the virtual environment
Windows PowerShell:
.venv\Scripts\Activate.ps1

4. Install dependencies
pip install -r requirements.txt

5. Run all tests
pytest tests

Run individual test suites
API tests:
pytest tests/test_api.py

UI tests:
pytest tests/test_login.py

Database tests:
pytest tests/test_database.py

Test Application
The UI automation tests use the SauceDemo application:
https://www.saucedemo.com/
Project Highlights
- Automated web application testing using Selenium
- REST API validation using Python Requests
- Database validation using SQLite
- Page Object Model implementation
- Reusable Pytest fixtures
- Automated execution of UI, API, and database tests
- 13/13 automated tests passing
Author
Vaishnavi Singh
B.Tech CSE (AI & ML)