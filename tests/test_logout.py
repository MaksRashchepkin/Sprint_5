from conftest import driver
from locators import Locators
from data import Data, Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogin:
    def test_logout_from_personal_account(self, driver): # Выход по кнопке выйти в личном кабинете
        driver.get(Url.login_page)
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.logout_button))
        driver.find_element(*Locators.logout_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_login))
        assert driver.find_element(*Locators.header_login).is_displayed()
