
import random

class Data:
    name = 'Maksim' # Логин
    email = 'Rashchepkin_Maksim_12_321@gmail.com' # Email
    password = '123456' # Пароль

class Url:
    main_page = 'https://stellarburgers.nomoreparties.site/' # Главная страница
    login_page = f"{main_page}login" # Страница входа
    registration_page = f"{main_page}register" # Страница регистрации
    profile_page = f"{main_page}account/profile"  # Страница профиля
    recovery_password_page = f"{main_page}forgot-password" # Страница восстановления пароля


class RandomUser:
    name = f"UserName{random.randint(1, 999)}" # Рандом логин
    email = f"UserEmail{random.randint(100, 999)}@gmail.com" # Рандом email
    password = f"pas{random.randint(100, 999)}" # Рандом пароль
    incorrect_password = f"q{random.randint(1000, 9999)}" # Рандом пароль менее 6-ти символов
    incorrect_email = f"@gmail.com{random.randint(100, 999)}UserEmail"  # Некорректный email
