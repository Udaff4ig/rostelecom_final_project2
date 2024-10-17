import time
from selenium.webdriver.common.by import By

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_social.py


# ТЕСТ №1
def test_vk_auth(driver):
    """Авторизация через VK"""
    driver.find_element(By.XPATH, '//*[@id="oidc_vk"]').click()
#    time.sleep(3)

    # Проверяем переход по ссылке на быстрый вход в vk по  qr-коду
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]')


# ТЕСТ №2
def test_mail_auth(driver):
    """Авторизация через Mail"""
    driver.find_element(By.XPATH, '//*[@id="oidc_mail"]').click()
#    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="wrp"]')


# ТЕСТ №3
def test_Tinkoff_auth(driver):
    """Авторизация через Тиньков"""
    driver.find_element(By.XPATH, '//*[@id="oidc_tinkoff"]').click()
#    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="form-title"]')


# ТЕСТ №4
def test_OK_auth(driver):
    """Авторизация через Одноклассники"""
    driver.find_element(By.XPATH, '//*[@id="oidc_ok"]').click()
#    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="widget-el"]/div[2]')
