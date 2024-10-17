import uuid
import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    # Установка неявного ожидания
    driver.implicitly_wait(5)
    # Переход на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state'
               '=0bed2c04-ae5f-49f4-9e7e-d6b5a80ebcb0&theme&auth_type')
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture()
def Webdriver():
    Webdriver = webdriver.Chrome(executable_path='chromedriver.exe')
    # Установка неявного ожидания
    Webdriver.implicitly_wait(7)
    # Переход на страницу авторизации
    Webdriver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?response_type=code&scope=openid&client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk-api.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Flk.rt.ru%252F&state=%7B%22uuid%22%3A%22AD1E1A00-ADC6-41E4-9493-CE8A5D78690E%22%7D')
    Webdriver.maximize_window()

    yield Webdriver

    Webdriver.quit()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Эта функция помогает обнаружить, что какой-либо тест не прошел успешно
    # и передать эту информацию в teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def web_browser(request, driver):

    yield driver

    # Этот код выполнится после отрабатывания теста:
    if request.node.rep_call.failed:
        # Сделать скриншот, если тест провалится:
        try:
            driver.execute_script("document.body.bgColor = 'white';")

            # Создаем папку screenshots и кладем туда скриншот с генерированным именем:
            driver.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # Для дебагинга, печатаем информацию в консоль
            print('URL: ', driver.current_url)
            print('Browser logs:')
            for log in driver.get_log('browser'):
                print(log)

        except:
            pass