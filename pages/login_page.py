from selenium.webdriver.common.by import By

WAIT_TIME = 3

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(WAIT_TIME)

    _username = (By.ID, 'user-name')
    _password = (By.ID, 'password')
    _login_button = (By.ID, 'login-button')

    def enter_username(self, username):
        webelement = self.driver.find_element(*self._username)
        webelement.send_keys(username)

    def enter_password(self, password):
        webelement = self.driver.find_element(*self._password)
        webelement.send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*self._login_button).click()

