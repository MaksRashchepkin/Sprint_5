from conftest import driver
from locators import Locators
from data import Data, Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogin:
    def test_go_to_constructor_from_personal_account(self, driver): # Переход из личного кабинета в конструктор по клику
        driver.get(Url.login_page)
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_profile))
        driver.find_element(*Locators.constructor_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.assemble_burger))
        assert driver.find_element(*Locators.assemble_burger).is_displayed()

    def test_go_to_logo_from_personal_account(self, driver): # Переход из личного кабинета на логотип Stellar Burgers по клику
        driver.get(Url.login_page)
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_profile))
        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))
        assert driver.find_element(*Locators.order_button).is_enabled()
