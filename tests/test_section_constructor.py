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
            expected_conditions.visibility_of_element_located(Locators.active_div_fillings_in_constructor))
        driver.find_element(*Locators.buns_span).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.active_div_buns_in_constructor))
        assert driver.find_element(*Locators.fluorescent_buns_r2_d3).is_enabled()

    def test_sauces_section(self, driver): # Переход к разделу соусы
        driver.get(Url.main_page)
        driver.find_element(*Locators.fillings_span).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.active_div_fillings_in_constructor))
        driver.find_element(*Locators.sauces_span).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.active_div_sauces_in_constructor))
        assert driver.find_element(*Locators.sauce_spicy_x).is_enabled()

    def test_fillings_section(self, driver): # Переход к разделу начинки
        driver.get(Url.main_page)
        driver.find_element(*Locators.fillings_span).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.active_div_fillings_in_constructor))
        assert driver.find_element(*Locators.meat_of_immortal_shellfish_protostomia).is_enabled()
