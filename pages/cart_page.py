from selenium.webdriver.common.by import By


class CartPage:

    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(*self.CART_BUTTON).click()

    def get_item_name(self):
        return self.driver.find_element(*self.CART_ITEM).text