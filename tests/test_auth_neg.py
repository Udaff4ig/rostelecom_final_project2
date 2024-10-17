import time
from selenium.webdriver.common.by import By

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_neg.py

# ТЕСТ №1
def test_auth_user_no_Email(driver):
    """Авторизация на сайте через почту, без заполнения строки ввода "Электронная почта" """

    # Нажимаем на кнопку "Почту" для авторизации
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
#    time.sleep(2)

    # Строка ввода "Электронная почта" оставляем пустой
    enter_email = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_email.send_keys('')
#    time.sleep(2)

    # Ввод пароль
    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('ffefer435')
    time.sleep(12)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
#    time.sleep(2)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')

# ТЕСТ №2
def test_auth_user_no_phone(driver):
    """Авторизация на сайте по номеру телефона, без заполнения строки ввода "Мабильный телефон" """

    # Нажимаем на кнопку "Номер" для авторизации по номеру тел
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()
#    time.sleep(2)

    # Строка ввода "Мабильный телефон" оставляем пустой
    enter_phone = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_phone.send_keys('')
#    time.sleep(2)

    # Ввод пароль
    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('DGFGwrewr654')
    time.sleep(12)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
#    time.sleep(2)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')

# ТЕСТ № 3
def test_auth_one_character_password(driver):
    ''' Ввод одного символа в строке ввода 'пароль' '''

    # Нажимаем на кнопку "Почту" для авторизации
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
#    time.sleep(2)

    # Строка ввода "Электронная почта" оставляем пустой
    enter_email = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_email.send_keys('wegarap900@rowplant.com')
#    time.sleep(2)

    # Ввод одной буквы в поле ввода пароля
    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('Q')
    time.sleep(12)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
#    time.sleep(2)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')


# ТЕСТ №4
def test_auth_exceeding_number_characters_password(driver):
    ''' Ввод 21 символа в строку ввода "пароль" '''

    # Нажимаем на кнопку "Почту" для авторизации
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
#    time.sleep(2)

    # Строка ввода "Электронная почта" оставляем пустой
    enter_email = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_email.send_keys('')
#    time.sleep(2)

    # # Ввод 21 символа в поле ввода пароль
    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('Bbaabbb1Bbbbbbb1Bbaab')
    time.sleep(12)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
#    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')


# ТЕСТ №5
def test_auth_no_password(driver):
    ''' Авторизация на сайте через Почту, без заполнения строки ввода пароль '''

    # Нажимаем на кнопку "Почту" для авторизации
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
#    time.sleep(2)

    # Строка ввода "Электронная почта" оставляем пустой
    enter_email = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_email.send_keys('wegarap900@rowplant.com')
#    time.sleep(2)

    # Строка ввода "Пароль" оставляем пустой
    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('')
    time.sleep(12)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
#    time.sleep(2)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')

# ТЕСТ №6
def test_auth_without_Latin_letters_password(driver):
    """ Авторизация на сайте через Почту, заполнение строки ввода "пароль" не используя латинские буквы """

    # Нажимаем на кнопку "Почту" для авторизации
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
#    time.sleep(2)

    # Строка ввода "Электронная почта" оставляем пустой
    enter_email = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_email.send_keys('wegarap900@rowplant.com')
#    time.sleep(2)

    # ввода "пароль" не используя латинские буквы
    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('Пврыга2')
    time.sleep(12)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
#    time.sleep(2)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')

# ТЕСТ№7
def test_auth_no_lowercase_letters_password(driver):
    """ Авторизация на сайте через Почту, заполнение строки ввода "пароль" не используя строчной буквы """

    # Нажимаем на кнопку "Почту" для авторизации
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
#    time.sleep(2)

    # Строка ввода "Электронная почта" оставляем пустой
    enter_email = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_email.send_keys('wegarap900@rowplant.com')
#    time.sleep(2)

    # Ввод "пароля" не используя строчной буквы
    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('FHEYFEFBJHBF1')
    time.sleep(12)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
#    time.sleep(2)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')


# ТЕСТ №8
def test_auth_by_code_no_Email(Webdriver):
    ''' """Авторизация по коду, с пустой строкой Email или мобильный телефон'''

    # Оставляем пустую строку ввода email или мобильный телефон
    enter_Email = Webdriver.find_element(By.XPATH, '//*[@id="address"]')
    enter_Email.send_keys('')
    time.sleep(12)

    auth = Webdriver.find_element(By.XPATH, '//*[@id="otp_get_code"]')
    auth.click()
#    time.sleep(2)

    assert Webdriver.find_element(By.XPATH, '//*[@id="app"]/main[1]')


# ТЕСТ №9
def test_auth_empty_string_phone(Webdriver):
    ''' Авторизация по коду,с некорректный ввод номера тел(+7 --- -------) в строкой Email или мобильный телефон '''


    # Оставляем пустую строку ввода email или мобильный телефон
    enter_Email = Webdriver.find_element(By.XPATH, '//*[@id="address"]')
    enter_Email.send_keys('+7 --- -------')
    time.sleep(12)

    auth = Webdriver.find_element(By.XPATH, '//*[@id="otp_get_code"]')
    auth.click()
#    time.sleep(2)

    assert Webdriver.find_element(By.XPATH, '//*[@id="app"]/main[1]')

# ТЕСТ №10 ID
def test_non_existent_email(driver):
    ''' Авторизация c несуществующим (незарегистрированным пользователем) в системе Email '''

    # Нажимаем на кнопку "Почту" для авторизации
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
#    time.sleep(2)

    # Строка ввода "Электронная почта" оставляем пустой
    enter_email = driver.find_element(By.XPATH, '//*[@id="username"]')
    enter_email.send_keys('kejf@mail.ru')
#    time.sleep(2)

    # Ввод пароль
    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Qwerty')
    time.sleep(15)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
#    time.sleep(2)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')