from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    _title = (By.CSS_SELECTOR, 'span[class="title"]')
    _cart = (By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    _item_name = (By.CSS_SELECTOR, 'div[class="inventory_item_name"]')
    _add_to_cart = (By.CSS_SELECTOR, 'button[name*="add-to-cart"]')
    _image = (By.CSS_SELECTOR, 'img[class="inventory_item_img"]')
    _menu = (By.CSS_SELECTOR, 'button[id*="menu"]')
    _logout = (By.CSS_SELECTOR, 'a[id*="logout"]')

    def get_title(self):
        return self.get_webelement(self._title).text

    def cart_icon_content(self):
        return self.get_webelement(self._cart).text

    def inventory_items(self):
        webelements = self.get_webelements(self._item_name)
        res = []
        for elem in webelements:
            res.append(elem.text)
        return res

    def image_is_present(self, index_=0):
        try:
            webelements = self.get_webelements(self._image)[index_]
            return True
        except:
            return False

    def font_color(self, index_=0, object_element='title'):
        if object_element == 'title':
            webelements = self.get_webelements(self._item_name)
        else:
            webelements = self.get_webelements(self._add_to_cart)
        rgb_color = webelements[index_].value_of_css_property('color')
        if rgb_color == 'rgba(226, 35, 26, 1)':
            res = 'red'
        else:
            res = None
        return res

    def item_title_format(self, index_=0):
        return self.get_webelements(self._item_name)[index_].text

    def _click_menu_btn(self):
        self.get_webelement(self._menu).click()

    def logout(self):
        self._click_menu_btn()
        self.get_webelement(self._logout).click()
