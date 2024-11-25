from conftest import driver, login
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogin:
    def test_go_to_constructor_from_personal_account(self, driver, login): # Переход из личного кабинета в конструктор по клику
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_profile))
        driver.find_element(*Locators.constructor_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.assemble_burger))
        assert driver.find_element(*Locators.assemble_burger).is_displayed()

    def test_go_to_logo_from_personal_account(self, driver, login): # Переход из личного кабинета на логотип Stellar Burgers по клику
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_profile))
        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))
        assert driver.find_element(*Locators.order_button).is_enabled()
