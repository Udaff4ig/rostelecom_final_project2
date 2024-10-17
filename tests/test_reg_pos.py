import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_reg_pos.py


# ТЕСТ №1
def test_reg_positive_Email(driver):
    ''' Регистрация через Email с валидными данными '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод корректного имя
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/div[2]'))).click()
#    time.sleep(5)

    choose_region_RB = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[2]')
    choose_region_RB.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('yahseb@mailto.plus')
#    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    # Вводим пароль
    enter_password.send_keys('123456789Qwerty')
#    time.sleep(5)
    # Подтверждение пароля
    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Qwerty')

#    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()

    # Проверяем, что мы оказались на главной странице Подтверждение кода
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"


# ТЕСТ №2
def test_reg_positive_Number(driver):
    ''' Регистрация через номер телефона с валидными данными. Номер в данном тесте виртуальный.
        Можно подставить свой '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод корректного имя
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/div[2]'))).click()
#    time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[16]')
    choose_region.click()
#    time.sleep(3)

    enter_number = driver.find_element(By.XPATH, '//*[@id="address"]')

    # Вводим номера телефона
    enter_number.send_keys('+79828995463')
 #   time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    # Вводим пароль
    enter_password.send_keys('123456789Qwerty')
  #  time.sleep(6)
    # Подтверждение пароля
    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Qwerty')

   # time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()

    # Проверяем, что мы оказались на главной странице Подтверждение кода
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение телефона"


# ТЕСТ №3
def test_reg_positive_min_characters_name(driver):
    '''Проверка  поле "Имя" на ввод 2 символов состоящих из букв кириллицы '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')

    # Ввод в поле "имя" мин кол-во символов ( 2 )
    enter_first_name.send_keys('Ал')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/div[2]'))).click()
#    time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[5]')
    choose_region.click()
#    time.sleep(3)

    enter_number = driver.find_element(By.XPATH, '//*[@id="address"]')

    # Вводим Email
    enter_number.send_keys('dlfhkdlkj@mailto.plus')
#    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    # Вводим пароль
    enter_password.send_keys('123456789Qwerty')
#    time.sleep(6)
    # Подтверждение пароля
    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Qwerty')

#    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()

    # Проверяем, что мы оказались на главной странице Подтверждение кода
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"


# ТЕСТ №4
def test_reg_positive_max_characters_name(driver):
    '''Проверка  поле "Имя" на ввод 30 символов состоящих из букв кириллицы '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')

    # Ввод в поле "имя" max кал-во символов( 30 )
    enter_first_name.send_keys('Агуращурадуадушгаруоигупаурмау')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/div[2]'))).click()
#    time.sleep(5)

    choose_region_RB = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[2]')
    choose_region_RB.click()
#    time.sleep(3)

    enter_number = driver.find_element(By.XPATH, '//*[@id="address"]')

    # Ввод Email
    enter_number.send_keys('jjrfjkj@mailto.plus')
#    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    # Вводим пароль
    enter_password.send_keys('123456789Qwerty')
#    time.sleep(6)
    # Подтверждение пароля
    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Qwerty')

#    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()

    # Проверяем, что мы оказались на главной странице Подтверждение кода
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"

# ТЕСТ №5
def test_reg_positive_dash_name(driver):
    ''' Проверка  поле "Имя" на ввод сложно-составного имени( через -) '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')

    # Ввод в поле "имя" знак тире(-)
    enter_first_name.send_keys('Мамин-Сибиряк')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/div[2]'))).click()
#    time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[30]')
    choose_region.click()
#    time.sleep(3)

    enter_number = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Ввод Email
    enter_number.send_keys('rgrrtg@mailto.plus')
#    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    # Вводим пароль
    enter_password.send_keys('123456789Qwerty')
#    time.sleep(6)
    # Подтверждение пароля
    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Qwerty')

#    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()

    # Проверяем, что мы оказались на главной странице Подтверждение кода
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"


# ТЕСТ №6
def test_reg_positive_min_characters_last_name(driver):
    '''Проверка  поле "Фамилия" на ввод 2 символов состоящих из букв кириллицы '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод корректного имя
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    # Ввод мин каличество символов в поле "фамилия"
    enter_last_name.send_keys('Ал')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/div[2]'))).click()
 #   time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[36]')
    choose_region.click()
#    time.sleep(3)

    enter_number = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим Email
    enter_number.send_keys('hjgefheg@mailto.plus')
#    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    # Вводим пароль
    enter_password.send_keys('123456789Qwerty')
#    time.sleep(5)
    # Подтверждение пароля
    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Qwerty')

#    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()

    # Проверяем, что мы оказались на главной странице Подтверждение кода
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"



# ТЕСТ №7
def test_reg_positive_max_characters_last_name(driver):
    '''Проверка  поле "Фамилия" на ввод 30 символов состоящих из букв кириллицы '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
 #   time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод корректного имя
    enter_first_name.send_keys('Алекс')
 #   time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    # Ввод в поле фамилия 30 символов
    enter_last_name.send_keys('Агуращурадуадушгауоиагупаурмау')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/div[2]'))).click()
#    time.sleep(5)

    choose_region_RB = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[2]')
    choose_region_RB.click()
#    time.sleep(3)

    enter_number = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим Email
    enter_number.send_keys('kjrfhekl@mailto.plus')
#    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    # Вводим пароль
    enter_password.send_keys('123456789Qwerty')
#    time.sleep(5)
    # Подтверждение пароля
    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Qwerty')

#    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()

    # Проверяем, что мы оказались на главной странице Подтверждение кода
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"


# ТЕСТ №8
def test_reg_positive_dash_last_name(driver):
    '''Проверка  поле "Фамилия" на ввод сложно составной фамилии (через -)'''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод корректного имя
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    # Ввод фамилии со знаком тире(-)
    enter_last_name.send_keys('Алексов-Сибиряк')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/div[2]'))).click()
#    time.sleep(5)

    choose_region_RB = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[2]')
    choose_region_RB.click()
#    time.sleep(3)

    enter_number = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим Email
    enter_number.send_keys('puytrdfbj@mailto.plus')
#    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    # Вводим пароль
    enter_password.send_keys('123456789Qwerty')
#    time.sleep(5)
    # Подтверждение пароля
    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Qwerty')

#    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()

    # Проверяем, что мы оказались на главной странице Подтверждение кода
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"



# ТЕСТ №9
def test_reg_positive_min_characters_password(driver):
    '''Проверка  поле "пароль" на ввод символов (хотя бы одна Заглавная буква и одна цифра или спецсимвол) '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод корректного имя
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/div[2]'))).click()
#    time.sleep(5)

    choose_region_RB = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[2]')
    choose_region_RB.click()
 #   time.sleep(3)

    enter_number = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим Email
    enter_number.send_keys('yuijjmu@mailto.plus')
#    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')

    # Вводим пароль, который содержит 8 символов
    enter_password.send_keys('123456789Qwerty')
#    time.sleep(5)
    # Подтверждение пароля
    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('RThdjve7')

#    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()

    # Проверяем, что мы оказались на главной странице Подтверждение кода
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"



# ТЕСТ №10
def test_reg_positive_special_characters_email(driver):
    '''Проверка  поле "Email" на ввод разрешенных спецсимволов в именной части (aaa@email.ru)'''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод корректного имя
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/div[2]'))).click()
#    time.sleep(5)

    choose_region_RB = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[2]')
    choose_region_RB.click()
#    time.sleep(3)

    enter_number = driver.find_element(By.XPATH, '//*[@id="address"]')

    # Вводим в Email рзрешенных символов aaa@email.ru
    enter_number.send_keys('hfgefjkj@mailto.plus')
#    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')

    # Вводим пароль
    enter_password.send_keys('123456789Qwerty')
#    time.sleep(5)
    # Подтверждение пароля
    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Qwerty')

#    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()

    # Проверяем, что мы оказались на главной странице Подтверждение кода
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"


# ТЕСТ №11
def test_reg_positive_numbers_email(driver):
    '''Проверка  поле "Email" на ввод цифр'''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод имя
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/div[2]'))).click()
#    time.sleep(5)

    choose_region_RB = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[2]')
    choose_region_RB.click()
#    time.sleep(3)

    enter_number = driver.find_element(By.XPATH, '//*[@id="address"]')

    # Вводим в Email цифр
    enter_number.send_keys('2345678@mailto.plus')
#    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')

    # Вводим пароль
    enter_password.send_keys('123456789Qwerty')
#    time.sleep(6)
    # Подтверждение пароля
    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Qwerty')

#    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()

    # Проверяем, что мы оказались на главной странице Подтверждение кода
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"

