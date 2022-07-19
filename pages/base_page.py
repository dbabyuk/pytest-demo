

WAIT_TIME = 3


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(WAIT_TIME)

    def get_webelement(self, locator):
        return self.driver.find_element(*locator)

    def get_webelements(self, locator):
        return self.driver.find_elements(*locator)
