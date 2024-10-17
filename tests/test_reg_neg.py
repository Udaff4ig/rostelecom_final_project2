import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_reg_neg.py


# ТЕСТ №1
def test_reg_empty_string_name(driver):
    '''Пустое поле ввода "Имя"'''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Пустое поле ввода "Имя"
    enter_first_name.send_keys('')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region_RK = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[1]')
    choose_region_RK.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('sdfgh@mailto.plus')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ №2
def test_reg_Latin_letters_name(driver):
    ''' Латинские буквы в строке ввода "Имя" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Латинские буквы в поле ввода "Имя"
    enter_first_name.send_keys('Aleks')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[7]')
    choose_region.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('wertyujhg@mailto.plus')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ №3
def test_reg_numbers_string_name(driver):
    ''' Цифры в строке ввода "Имя" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод цифр в поле ввода "Имя"
    enter_first_name.send_keys('12345')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[7]')
    choose_region.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('wertyhg@mailto.plus')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ №4
def test_reg_Latin_Cyrillic_name(driver):
    ''' Латинские буквы и кириллица в строке ввода "Имя" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Латинские буквы и кириллица в поле ввода "Имя"
    enter_first_name.send_keys('Алеks')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[7]')
    choose_region.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('jjhgf@mailto.plus')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ №5
def test_reg_one_character_name(driver):
    ''' Ввод одного символа в строке ввода "Имя" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод одной буквы в поле ввода "Имя"
    enter_first_name.send_keys('А')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[7]')
    choose_region.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('ertyjmhng@mailto.plus')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ №6
def test_reg_exceeding_number_characters_name(driver):
    ''' Ввод 31 символа в строку ввода "Имя" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод 31 символа в поле ввода "Имя"
    enter_first_name.send_keys('Агуращурадуадушгаруоиагупаурмау')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#   time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[7]')
    choose_region.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('rtyuiuyt@mailto.plus')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ №7
def test_reg_forbidden_spec_characterss_name(driver):
    ''' Ввод запрещенных спецсимволов в строку ввода "Имя" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод запрещенных спецсимволов в поле ввода "Имя"
    enter_first_name.send_keys('!#$%&*+-/=?^_`{|}~')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    # Ввод фамилии
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[11]')
    choose_region.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('ertyuytr@mailto.plus')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ №8
def test_reg_empty_string_Last_name(driver):
    ''' Пустое поле ввода "Фамилия" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввода "Имя"
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    # Пустое поле ввода "Фамилия"
    enter_last_name.send_keys('')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region_RK = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[1]')
    choose_region_RK.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('wertytr@mailto.plus')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ №9
def test_reg_numbers_string_last_name(driver):
    ''' Цифры в строке ввода "Фамилия" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод "Имя"
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    # Ввод цифр в поле ввода "Фамилия"
    enter_last_name.send_keys('123456')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region_RK = driver.find_element(By.XPATH,
                                               '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[1]')
    choose_region_RK.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('efgtyjjth@mail.ru')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ № 10
def test_reg_Latin_Cyrillic_last_name(driver):
    ''' Латинские буквы и кириллица в строке ввода "Фамилия" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод "Имя"
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    # Латинские буквы и кириллица в поле ввода "Фамилия"
    enter_last_name.send_keys('Alekсов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region_RK = driver.find_element(By.XPATH,
                                               '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[5]')
    choose_region_RK.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('efrjtjhr@mail.ru')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ № 11
def test_reg_one_character_last_name(driver):
    ''' Ввод одного символа в строке ввода "Фамилия" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод "Имя"
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    # Ввод одной буквы в поле ввода "Фамилия"
    enter_last_name.send_keys('А')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[11]')
    choose_region.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('fgrtjyjh@mail.ru')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ №12 ID
def test_reg_exceeding_number_characters_last_name(driver):
    ''' Ввод 31 символа в строку ввода "Фамилия" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод "Имя"
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    # Ввод 31 символа в поле ввода "фамилия"
    enter_last_name.send_keys('Агуращурадуадушгаруоиагупаурмау')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[8]')
    choose_region.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('wfnmjyhtg@mail.ru')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ № 13
def test_reg_forbidden_spec_characterss_last_name(driver):
    ''' Ввод запрещенных спецсимволов в строку ввода "Фамилия" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод в поле "Имя"
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    # Ввод запрещенных спецсимволов в поле ввода "Фамилия"
    enter_last_name.send_keys('!#$%&*+-/=?^_`{|}~')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[19]')
    choose_region.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')
    # Вводим email
    enter_email.send_keys('wertyuyt@mail.ru')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ № 14 ID
def test_unsuccessful_email_already_used(driver):
    ''' Регистрация с уже зарегистрированным email '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввод в поле "Имя"
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    # Ввод в поле "Фамилия"
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[11]')
    choose_region.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')

    # Вводим email, который был зарегистрирован ранее
    enter_email.send_keys('azveu@mailto.plus')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ № 15 ID
def test_reg_empty_string_Last_Email(driver):
    ''' Пустое поле ввода "Email" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввода "Имя"
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    # Ввода "Фамилия"
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region_RK = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[1]')
    choose_region_RK.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')

    # Пустая строка email
    enter_email.send_keys('')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ № 16
def test_reg_Latin_letters_Email(driver):
    ''' Ввод запрещенных спецсимволов в строку ввода "Email" (&, %,#,@@@@,+,=)'''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввода "Имя"
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    # Ввод "Фамилия"
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[4]')
    choose_region.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')

    # Вводим email
    enter_email.send_keys('"№;%:"@mailto.plus')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# ТЕСТ №17
def test_reg_empty_string_phone(driver):
    ''' Некорректный ввод номера тел(+7 --- -------) в строку "телефон" '''

    # Нажимаем на кнопку "Зарегистроваться"
    driver.find_element(By.ID, "kc-register").click()
#    time.sleep(5)
    enter_first_name = driver.find_element(By.XPATH,
                                           '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    # Ввода "Имя"
    enter_first_name.send_keys('Алекс')
#    time.sleep(5)

    enter_last_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')

    # Ввода "Фамилия"
    enter_last_name.send_keys('Алексов')
#    time.sleep(5)

    # Выбор региона
    wait = WDW(driver, 5)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input'))).click()
#    time.sleep(5)

    choose_region_RK = driver.find_element(By.XPATH,
                                           '//section[@id="page-right"]/div/div/div/form/div[2]/div[2]/div[2]/div/div[27]')
    choose_region_RK.click()
#    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '//*[@id="address"]')

    # Некорректный вводом номера телефона
    enter_email.send_keys('+7 --- -------')
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
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение телефона"
