import time
from selenium.webdriver.common.by import By


# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_pos.py

# ТЕСТ №1
def test_auth_by_code(Webdriver):
    """Авторизация по коду """

    # Ввод email
    enter_Email = Webdriver.find_element(By.XPATH, '//*[@id="address"]')
    enter_Email.send_keys('azveu@mailto.plus')
    time.sleep(10)

    auth = Webdriver.find_element(By.XPATH, '//*[@id="otp_get_code"]')
    auth.click()
    time.sleep(3)

    assert Webdriver.find_element(By.XPATH, '//*[@id="app"]/main[1]')


# ТЕСТ №2 ID
def test_auth_user_Email(driver):
    """Авторизация на сайте через почту """

    # Нажимаем на кнопку "Почту" для авторизации
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    time.sleep(5)

    # Ввеод email
    enter_email = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_email.send_keys('azveu@mailto.plus')
    time.sleep(4)

    # Ввод пароль
    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Qwerty')
    time.sleep(5)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')

# ТЕСТ №3
def test_auth_user_phone(driver):
    """Авторизация на сайте по номеру телефона """

    # Нажимаем на кнопку "Номер" для авторизации по номеру тел
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()
    time.sleep(5)

    # Ввеод номера тел
    enter_phone = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_phone.send_keys('+79828995463')
    time.sleep(4)

    # Ввод пароль
    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Qwerty')
    time.sleep(5)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')

# ТЕСТ №4
def test_auth_user_login(driver):
    """Авторизация на сайте через Логин """

    # Нажимаем на кнопку "Номер" для авторизации по номеру тел
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()
    time.sleep(5)

    # Ввеод email
    enter_login = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_login.send_keys('rtkid_1729077157900')
    time.sleep(4)

    # Ввести корректный пароль
    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Qwerty')
    time.sleep(5)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')


# ТЕСТ №5
def test_forgotten_password_Email(driver):
    """Востоновление пароля на странице авторизации через Email"""

    # Нажать кн."Забыл пароль"
    driver.find_element(By.XPATH, '//*[@id="forgot_password"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    time.sleep(3)

    # Ввод email
    enter_email = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_email.send_keys('azveu@mailto.plus')
    time.sleep(20)

    auth = driver.find_element(By.XPATH, '//*[@id="reset"]')
    auth.click()
    time.sleep(5)

    # Проверяем, что мы оказались на главной странице Подтверждение кода
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]')


# ТЕСТ №6
def test_forgotten_password_nomber(driver):
    """Востоновление пароля на странице авторизации по номеру тел"""

    # Нажать кн."Забыл пароль"
    driver.find_element(By.XPATH, '//*[@id="forgot_password"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()
    time.sleep(3)

    # Ввод номера тел
    enter_nomber = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_nomber.send_keys('+79828995463')
    time.sleep(20)

    auth = driver.find_element(By.XPATH, '//*[@id="reset"]')
    auth.click()
    time.sleep(5)

    # Проверяем, что мы оказались на главной странице Подтверждение кода
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]')



