from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    PAGE_TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_page_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        ).text

    def add_backpack_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_BACKPACK)
        ).click()

    def get_cart_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        ).text