from conftest import driver, login
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogin:
    def test_go_to_personal_account(self, driver, login): # Переход по клику на Личный кабинет
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_profile))
        assert driver.find_element(*Locators.logout_button).is_enabled()
