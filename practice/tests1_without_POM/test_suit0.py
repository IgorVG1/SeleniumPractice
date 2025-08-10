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

def test_4(driver):
    url = 'https://parsinger.ru/selenium/3/3.html'

    driver.get(url)

    numerics = driver.find_elements(By.CSS_SELECTOR,'div.text p:nth-child(2)')
    sum = 0

    for numeric in numerics:
        sum = sum + int(numeric.text)

    print('\nSum of all numerics on second graph in each table:\n' + str(sum))

    assert sum == 149494128600, 'Сумма должна ровняться числу 149 494 128 600'

def test_5(driver):
    url = 'https://parsinger.ru/selenium/4/4.html'

    driver.get(url)

    checkboxes = driver.find_elements(By.CLASS_NAME,'check')
    for checkbox in checkboxes:
        checkbox.click()

    driver.find_element(By.CLASS_NAME,'btn').click()

    wait(driver,5).until(EC.visibility_of_element_located((By.ID,'result')))

    result_key = driver.find_element(By.ID,'result')
    print('\nКодовое число:\n' + result_key.text)
    assert result_key.is_displayed(), 'Должно появиться число'