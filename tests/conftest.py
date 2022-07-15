from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.main_page import MainPage


URL_UI = "https://saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture(scope='module')
def driver_instance():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(URL_UI)
    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def login_procedure(driver_instance):
    login_page = LoginPage(driver_instance)
    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login_btn()


@pytest.fixture(scope='module')
def main_page(driver_instance, login_procedure):
    main_page_instance = MainPage(driver_instance)
    yield main_page_instance
    main_page_instance.logout()
