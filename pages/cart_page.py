from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    _quantity_field = (By.CSS_SELECTOR, 'div[class="cart_quantity"]')

    def quantity_field_content(self):
        return self.get_webelement(self._quantity_field).text
