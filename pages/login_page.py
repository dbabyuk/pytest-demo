from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    _username = (By.ID, 'user-name')
    _password = (By.ID, 'password')
    _login_button = (By.ID, 'login-button')

    def enter_username(self, username):
        self.get_webelement(self._username).send_keys(username)

    def enter_password(self, password):
        self.get_webelement(self._password).send_keys(password)

    def click_login_btn(self):
        self.get_webelement(self._login_button).click()

