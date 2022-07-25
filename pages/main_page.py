from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    _image = (By.CSS_SELECTOR, 'img[class="inventory_item_img"]')
    _menu = (By.CSS_SELECTOR, 'button[id*="menu"]')
    _logout = (By.CSS_SELECTOR, 'a[id*="logout"]')
    _cart_btn = (By.CSS_SELECTOR, 'div[class*="item"] button')

    def click_cart_icon(self):
        """Clicks cart icon"""
        self.get_webelement(self._cart).click()

    def inventory_items(self):
        webelements = self.get_webelements(self._item_name)
        res = []
        for elem in webelements:
            res.append(elem.text)
        return res

    def image_is_present(self, index_: int = 0) -> bool:
        try:
            webelements = self.get_webelements(self._image)[index_]
            return True
        except:
            return False

    def font_color(self, index_=0, object_element='title'):
        if object_element == 'title':
            webelements = self.get_webelements(self._item_name)
        else:
            webelements = self.get_webelements(self._cart_btn)
        rgb_color = webelements[index_].value_of_css_property('color')
        if rgb_color == 'rgba(226, 35, 26, 1)':
            res = 'red'
        else:
            res = 'black'
        return res

    def _click_menu_btn(self):
        self.get_webelement(self._menu).click()

    def logout(self):
        self._click_menu_btn()
        self.get_webelement(self._logout).click()

    def item_text(self, index_=0):
        return self.get_webelements(self._cart_btn)[index_].text
