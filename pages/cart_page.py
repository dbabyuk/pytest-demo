from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    _quantity_field = (By.CSS_SELECTOR, 'div[class="cart_quantity"]')
    _product_items = (By.CSS_SELECTOR, 'div[class="cart_item"]')
    _continue_shopping_btn = (By.CSS_SELECTOR, 'button[id="continue-shopping"]')

    def quantity_field_content(self):
        return self.get_webelement(self._quantity_field).text

    def product_items_are_present(self) -> bool:
        try:
            webelements = self.get_webelements(self._product_items)
            if webelements == []:
                return False
            return True
        except:
            return False

    def continue_shopping(self):
        self.get_webelement(self._continue_shopping_btn).click()
