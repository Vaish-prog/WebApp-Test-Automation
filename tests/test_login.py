from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert "inventory.html" in driver.current_url


def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    error_message = login_page.get_error_message()

    assert "Username and password do not match" in error_message


def test_empty_login(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.click_login()

    error_message = login_page.get_error_message()

    assert "Username is required" in error_message


def test_missing_password(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.click_login()

    error_message = login_page.get_error_message()

    assert "Password is required" in error_message


def test_navigation(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    products_page = ProductsPage(driver)

    assert products_page.get_page_title() == "Products"


def test_add_product_to_cart(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == "1"
def test_cart_item(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()

    cart_page = CartPage(driver)

    cart_page.open_cart()

    assert cart_page.get_item_name() == "Sauce Labs Backpack"