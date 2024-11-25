from selenium.webdriver.common.by import By

class Locators:
    login_button_main_page = By.XPATH, ".//button[text()='Войти в аккаунт']" # Кнопка Войти в аккаунт на главной странице
    input_email = By.XPATH, ".//label[text()='Email']/following-sibling::input" # Поле ввода email
    input_password = By.XPATH, ".//label[text()='Пароль']/following-sibling::input" # Поле ввода password
    login_button_login_page = By.XPATH, ".//button[text()='Войти']" # Кнопка Войти на странице входа
    registration_button = By.XPATH, ".//button[text()='Зарегистрироваться']" # Кнопка Зарегистрироваться на странице регистрация
    input_name = By.XPATH, ".//label[text()='Имя']/following-sibling::input" # Поле ввода имя
    header_login = By.XPATH, ".//h2[text()='Вход']" # Заголовок Вход
    header_registration = By.XPATH, ".//h2[text()='Регистрация']" # Заголовок Регистрация
    account_button = By.XPATH, ".//p[text()='Личный Кабинет']" # Кнопка Личный Кабинет
    login_button_registration_page = By.XPATH, ".//a[text()='Войти']" # Кнопка Войти на странице регистрация
    forgot_password_button = By.XPATH, ".//a[text()='Восстановить пароль']" # Кнопка Восстановить пароль на странице вход
    recovery_button = By.XPATH, ".//button[text()='Восстановить']" # Кнопка Восстановить на странице восстановления пароля
    constructor_button = By.XPATH, ".//p[text()='Конструктор']" # Кнопка Конструктор
    logo = By.XPATH, ".//a[@href='/']" # Логотип
    assemble_burger = By.XPATH, ".//h1[text()='Соберите бургер']" # Соберите бургер
    buns_span = By.XPATH, ".//span[text()='Булки']" # Раздел булки
    sauces_span = By.XPATH, ".//span[text()='Соусы']"  # Раздел соусы
    fillings_span = By.XPATH, ".//span[text()='Начинки']"  # Раздел начинки
    header_incorrect_password = By.XPATH, ".//p[text() = 'Некорректный пароль']"  # Сообщение об ошибке Некорректный пароль
    header_exist_user = By.XPATH, ".//p[text() = 'Такой пользователь уже существует']"  # Сообщение об ошибке Такой пользователь уже существует
    order_button = By.XPATH, ".//button[text() = 'Оформить заказ']"  # Кнопка Оформить заказ
    header_profile = By.XPATH, ".//a[text() = 'Профиль']"  # Заголовок Профиль в личном кабинете
    logout_button = By.XPATH, ".//button[text() = 'Выход']"  # Кнопка Выход в личном кабинете
    login_button_recovery_page = By.XPATH, ".//a[text()='Войти']"  # Кнопка Войти на странице восстановления пароля
    active_div_buns_in_constructor = By.XPATH, ".//div[contains(@class, 'current')]/span[text()='Булки']"  # Активный раздел Булки в конструкторе
    active_div_sauces_in_constructor = By.XPATH, ".//div[contains(@class, 'current')]/span[text()='Соусы']"  # Активный раздел Соусы в конструкторе
    active_div_fillings_in_constructor = By.XPATH, ".//div[contains(@class, 'current')]/span[text()='Начинки']"  # Активный раздел Начинки в конструкторе
    fluorescent_buns_r2_d3 = By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']" # Флюоресцентная булка R2-D3
    sauce_spicy_x = By.XPATH, ".//p[text()='Соус Spicy-X']"  # Соус Spicy-X
    meat_of_immortal_shellfish_protostomia = By.XPATH, ".//p[text()='Мясо бессмертных моллюсков Protostomia']"  # Мясо бессмертных моллюсков Protostomia
