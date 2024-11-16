from conftest import driver
from locators import Locators
from data import Data, Url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogin:
    def test_login_main_page(self, driver): # Вход по кнопке Войти в аккаунт на главной
        driver.get(Url.main_page)
        driver.find_element(*Locators.login_button_main_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_login))
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))
        assert driver.find_element(*Locators.order_button).text == 'Оформить заказ'

    def test_login_private_account_button(self, driver): # Вход через кнопку Личный кабинет на главной
        driver.get(Url.main_page)
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_login))
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))
        assert driver.find_element(*Locators.order_button).text == 'Оформить заказ'

    def test_login_registration_form_page(self, driver): # Вход через кнопку в форме регистрации
        driver.get(Url.registration_page)
        driver.find_element(*Locators.login_button_registration_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_login))
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))
        assert driver.find_element(*Locators.order_button).text == 'Оформить заказ'

    def test_login_recovery_password_page(self, driver): # Вход через кнопку в форме восстановления пароля
        driver.get(Url.recovery_password_page)
        driver.find_element(*Locators.login_button_recovery_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_login))
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))
        assert driver.find_element(*Locators.order_button).text == 'Оформить заказ'
