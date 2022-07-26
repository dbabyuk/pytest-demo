from selenium.webdriver.common.by import By

WAIT_TIME = 1


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(WAIT_TIME)

    _title = (By.CSS_SELECTOR, 'span[class="title"]')
    _item_name = (By.CSS_SELECTOR, 'div[class="inventory_item_name"]')
    _item_price = (By.CSS_SELECTOR, 'div[class="inventory_item_price"]')
    _cart = (By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    _cart_btn = (By.CSS_SELECTOR, 'div[class*="item"] button')

    def get_webelement(self, locator):
        return self.driver.find_element(*locator)

    def get_webelements(self, locator):
        return self.driver.find_elements(*locator)

    def get_title(self):
        return self.get_webelement(self._title).text

    def item_title_name(self, index_=0):
        return self.get_webelements(self._item_name)[index_].text

    def item_price(self, index_=0):
        return self.get_webelements(self._item_price)[index_].text

    def cart_icon_content(self) -> str:
        """Returns cart text content"""
        return self.get_webelement(self._cart).text

    def add_or_remove_item(self, index_=0):
        """Clicks on "ADD TO CART / REMOVE" button"""
        self.get_webelements(self._cart_btn)[index_].click()

