import pytest
from selenium import webdriver
import time
from locators import Locators
from data import Data, Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(3)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get(Url.login_page)
    driver.find_element(*Locators.input_email).send_keys(Data.email)
    driver.find_element(*Locators.input_password).send_keys(Data.password)
    driver.find_element(*Locators.login_button_login_page).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.order_button))
    assert driver.find_element(*Locators.order_button).is_enabled()
    return login

