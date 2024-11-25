from time import sleep

import pytest
from selenium import webdriver
from data import Data, Url
from locators import Locators
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(1)
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

