UI tests for Stellar Burgers

Корневая папка
data.py
class Data - Валидные данные пользователя
class Url - Список url страниц
class RandomUser - Рандомные данные пользователя

conftest.py
driver - Настройки webdriver

locators.py
class Locators - Локаторы для тестирования

Папка tests
test_registration.py
test_registration_success - Успешная регистрация
test_registration_without_name - Регистрация без имени
test_registration_without_email - Регистрация без email
test_registration_without_password - Регистрация без пароля
test_registration_password_less_6_symbols - Регистрация с паролем менее 6 символов
test_registration_with_incorrect_email - Регистрация с некорректным email
test_registration_exist_user - Регистрация уже зарегистрированного пользователя


test_login.py
test_login_main_page - Вход по кнопке Войти в аккаунт на главной
test_login_private_account_button - Вход через кнопку Личный кабинет на главной
test_login_registration_form_page - Вход через кнопку в форме регистрации
test_login_recovery_password_page - Вход через кнопку в форме восстановления пароля


test_go_to_personal_account.py
test_go_to_personal_account - Переход по клику на Личный кабинет


test_go_to_constructor_from_personal_account.py
test_go_to_constructor_from_personal_account - Переход из личного кабинета в конструктор по клику
test_go_to_logo_from_personal_account - Переход из личного кабинета на логотип Stellar Burgers по клику


test_logout.py
test_logout_from_personal_account - Выход по кнопке выйти в личном кабинете


test_section_constructor.py
test_logout_from_personal_account - Выход по кнопке выйти в личном кабинете