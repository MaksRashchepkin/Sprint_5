from conftest import driver
from locators import Locators
from data import Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogin:
    def test_buns_section(self, driver): # Переход к разделу булки
        driver.get(Url.main_page)
        driver.find_element(*Locators.fillings_span).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.fillings_span))
        driver.find_element(*Locators.buns_span).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.buns_span))
        assert driver.find_element(*Locators.active_div_in_constructor).text == 'Булки'

    def test_sauces_section(self, driver): # Переход к разделу соусы
        driver.get(Url.main_page)
        driver.find_element(*Locators.sauces_span).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.sauces_span))
        assert driver.find_element(*Locators.active_div_in_constructor).text == 'Соусы'

    def test_fillings_section(self, driver): # Переход к разделу начинки
        driver.get(Url.main_page)
        driver.find_element(*Locators.fillings_span).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.fillings_span))
        assert driver.find_element(*Locators.active_div_in_constructor).text == 'Начинки'
