from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    _title = (By.CSS_SELECTOR, 'span[class="title"]')
    _menu = (By.CSS_SELECTOR, 'button[id*="menu"]')
    _logout = (By.CSS_SELECTOR, 'a[id*="logout"]')

    def get_title(self):
        webelement = self.driver.find_element(*self._title)
        return webelement.text

    def _click_menu_btn(self):
        self.driver.find_element(*self._menu).click()

    def logout(self):
        self._click_menu_btn()
        self.driver.find_element(*self._logout).click()
