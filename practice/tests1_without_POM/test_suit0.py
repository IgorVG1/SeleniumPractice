from selenium.webdriver.common.by import By
import time


def test_1(driver):
    driver.get('https://parsinger.ru/selenium/1/1.html')
    driver.find_element(By.NAME, 'first_name').send_keys('first name')
    driver.find_element(By.NAME, 'last_name').send_keys('last name')
    driver.find_element(By.NAME, 'patronymic').send_keys('patronymic')
    driver.find_element(By.NAME, 'age').send_keys('age')
    driver.find_element(By.NAME, 'city').send_keys('city')
    driver.find_element(By.NAME, 'email').send_keys('email')
    driver.find_element(By.ID, 'btn').click()

    time.sleep(3)


def test_2(driver):
    url = 'https://parsinger.ru/selenium/2/2.html'
    driver.get(url)
    driver.find_element(By.XPATH, '//a[text()="16243162441624"]').click()

    key = driver.find_element(By.ID, 'result')
    assert key.is_displayed(), 'Должно быть поздравление с большим числом'
    print('\nSecret key:\n' + key.text)


def test_3(driver):
    url = 'https://parsinger.ru/selenium/3/3.html'

    driver.get(url)

    tables = driver.find_elements(By.CLASS_NAME, 'text')
    sum = 0

    for table in tables:
        numerics = table.find_elements(By.TAG_NAME, 'p')
        for numeric in numerics:
            sum = sum + int(numeric.text)

    print('\nSum of all numerics:\n' + str(sum))

    assert sum == 450384194300, 'Сумма должна ровняться числу 450 384 194 300'
