from conftest import driver
from locators import Locators
from data import Data, Url, RandomUser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestRegistration:
    def test_registration_success(self, driver): # Успешная регистрация
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_name).send_keys(RandomUser.name)
        driver.find_element(*Locators.input_email).send_keys(RandomUser.email)
        driver.find_element(*Locators.input_password).send_keys(RandomUser.password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_login))
        assert driver.find_element(*Locators.header_login).is_displayed()

    def test_registration_without_name(self, driver): # Регистрация без имени
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_email).send_keys(RandomUser.email)
        driver.find_element(*Locators.input_password).send_keys(RandomUser.password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_registration))

        assert driver.find_element(*Locators.header_registration).is_displayed()

    def test_registration_without_email(self, driver): # Регистрация без email
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_name).send_keys(RandomUser.name)
        driver.find_element(*Locators.input_password).send_keys(RandomUser.password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_registration))
        assert driver.find_element(*Locators.header_registration).is_displayed()

    def test_registration_without_password(self, driver): # Регистрация без пароля
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_name).send_keys(RandomUser.name)
        driver.find_element(*Locators.input_email).send_keys(RandomUser.email)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_registration))
        assert driver.find_element(*Locators.header_registration).is_displayed()

    def test_registration_password_less_6_symbols(self, driver): # Регистрация с паролем менее 6 символов
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_name).send_keys(RandomUser.name)
        driver.find_element(*Locators.input_email).send_keys(RandomUser.email)
        driver.find_element(*Locators.input_password).send_keys(RandomUser.incorrect_password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_incorrect_password))
        assert driver.find_element(*Locators.header_incorrect_password).text == 'Некорректный пароль'

    def test_registration_with_incorrect_email(self, driver): # Регистрация с некорректным email
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_name).send_keys(RandomUser.name)
        driver.find_element(*Locators.input_email).send_keys(RandomUser.incorrect_email)
        driver.find_element(*Locators.input_password).send_keys(RandomUser.password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_exist_user))
        assert driver.find_element(*Locators.header_exist_user).text == 'Такой пользователь уже существует'

    def test_registration_exist_user(self, driver): # Регистрация уже зарегистрированного пользователя
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_name).send_keys(Data.name)
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.header_exist_user))
        assert driver.find_element(*Locators.header_exist_user).text == 'Такой пользователь уже существует'
