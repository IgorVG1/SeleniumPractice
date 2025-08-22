
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import Select
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


def test_6(driver):
    url = 'https://parsinger.ru/selenium/5/5.html'

    numbers = [1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38,
               39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73,
               74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118,
               119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153,
               154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
               187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207,
               208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233,
               234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255,
               256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
               292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314,
               318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349,
               353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412,
               419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451,
               452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479,
               480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519]

    driver.get(url)
    checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input.check')
    for checkbox in checkboxes:
        value_checkbox = int(checkbox.get_attribute('value'))
        if value_checkbox in numbers:
            checkbox.click()

    driver.find_element(By.CSS_SELECTOR, 'input.btn').click()

    key = driver.find_element(By.ID, 'result')
    print('\nKey number:\n' + key.text)
    assert key.is_displayed()


def test_7(driver):
    url = 'https://parsinger.ru/selenium/7/7.html'
    sum = 0

    driver.get(url)

    selects = driver.find_elements(By.TAG_NAME, 'option')
    for select in selects:
        sum = sum + int(select.text)

    driver.find_element(By.ID, 'input_result').send_keys(sum)
    driver.find_element(By.ID, 'sendbutton').click()

    key = driver.find_element(By.ID, 'result')
    print('\nYour Key:\n' + key.text)
    wait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'result')))
    assert key.is_displayed()


def test_8(driver):
    url = 'https://parsinger.ru/selenium/6/6.html'

    driver.get(url)

    math_hint = driver.find_element(By.ID, 'text_box').text  # Парсим текст из элемента
    print('\nMath hint:\n' + math_hint)
    answer = str(eval(math_hint))  # Преобразуем полученный текст в код и выполняем его с помощью функции <eval()>
    print('\nYour answer"\n' + answer)

    select = driver.find_element(By.ID, 'selectId')
    Select(select).select_by_visible_text(answer)

    driver.find_element(By.ID, 'sendbutton').click()

    key = driver.find_element(By.ID, 'result')
    if key.is_displayed():
        print('\nChecking your answer...\nExactly!\nYour key:\n' + key.text)
    assert key.is_displayed(), 'You have taken mistake(('


def test_9(driver):
    url = 'https://parsinger.ru/selenium/5.5/1/1.html'

    driver.get(url)

    inputs = driver.find_elements(By.TAG_NAME, 'input')
    for input in inputs:
        input.clear()

    driver.find_element(By.TAG_NAME, 'button').click()

    wait(driver, 10).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    key_from_alert = alert.text
    print("\nYour Key :\n" + str(key_from_alert))
    assert key_from_alert is not None, "Alert must contain big number, it's key"


def test_10(driver):
    url = 'https://parsinger.ru/methods/3/index.html'

    driver.get(url)

    cookies = driver.get_cookies()
    filtered_cookies = []
    print('\nFiltered cookies:')
    for cookie in cookies:
        name = cookie['name']
        value = cookie['value']

        if '_' in name:
            parts = name.split('_')
            number_cookie = int(parts[-1])

            if number_cookie % 2 == 0:
                key_part = int(value)
                filtered_cookies.append(key_part)
                print(f'Name:{name}\nValue:{value}')

    key_sum = sum(filtered_cookies)
    print(f'\nYour Key:\n{key_sum}')

    assert key_sum is not None, 'Must be sum values of all filtered cookies'


def test_11(driver):
    url = 'https://parsinger.ru/selenium/5.5/2/1.html'

    driver.get(url)

    inputs = driver.find_elements(By.TAG_NAME, 'input')
    for input in inputs:
        if input.get_attribute('data-enabled') == 'true':
            input.clear()

    driver.find_element(By.TAG_NAME, 'button').click()

    alert = driver.switch_to.alert
    alert_key = alert.text
    print('\nYour key:\n' + alert_key)
    assert alert_key is not None, 'Alert must contain big number, it it key'


def test_12(driver):
    url = 'https://parsinger.ru/methods/5/index.html'

    driver.get(url)

    list_expire_cookie = []

    links = driver.find_elements(By.CSS_SELECTOR, 'div.urls')
    for link in links:
        link.click()

        cookies_link = driver.get_cookies()
        for cookie_link in cookies_link:
            expiry_cookie = int(cookie_link['expiry'])
            list_expire_cookie.append(expiry_cookie)

        driver.back()

    print('\nList of expire all cookie each link:')
    print(list_expire_cookie)

    longest_expire_cookie = max(list_expire_cookie)
    print('\nThe most longest expire of cookie:')
    print(longest_expire_cookie)
    index_extra_cookie = list_expire_cookie.index(longest_expire_cookie)

    links[index_extra_cookie].click()
    key = driver.find_element(By.ID, 'result').text
    print(f'\nYour Key:\n{key}')


def test_13(driver):
    url = 'https://parsinger.ru/scroll/4/index.html'

    driver.get(url)

    buttons = driver.find_elements(By.TAG_NAME, 'button')
    sum = 0

    for button in buttons:
        driver.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        number = int(driver.find_element(By.ID, 'result').text)
        sum += number

    print(f'\nYour key:\n{sum}')
    assert sum is not None, "Must be big number. It is your key"


def test_14(driver):
    url = 'https://parsinger.ru/selenium/5.5/3/1.html'

    driver.get(url)

    checkboxes = driver.find_elements(By.TAG_NAME,'input')
    inputs = driver.find_elements(By.TAG_NAME,'textarea')
    sum = 0

    for checkbox in checkboxes:
        index_checkbox = checkboxes.index(checkbox)
        if checkbox.is_selected():
            summand = int(inputs[index_checkbox].get_attribute('value'))
            sum += summand

    print(f'\nSum of all inputs with selected checkbox:\n{sum}')
    assert sum.is_integer(), 'Must be big number, it is your key'


def test_15(driver):
    url = 'https://parsinger.ru/selenium/5.5/4/1.html'

    driver.get(url)

    inputs_gray = driver.find_elements(By.CSS_SELECTOR,'textarea[color="gray"]')
    inputs_blue = driver.find_elements(By.CSS_SELECTOR,'textarea[color="blue"]')
    inputs_button = driver.find_elements(By.CSS_SELECTOR,'div.parent button')

    for input_g in inputs_gray:

        joint_index = inputs_gray.index(input_g)
        joint_text = input_g.text

        input_g.clear()
        inputs_blue[joint_index].send_keys(joint_text)
        inputs_button[joint_index].click()

    driver.find_element(By.ID,'checkAll').click()

    key = driver.find_element(By.ID,'congrats').text
    print(f'\nYour key:\n{key}')
    assert key is not None, 'Must be text with code same format as XXXX-XXXX-XXXX...'


def test_16(driver):
    url = 'https://parsinger.ru/selenium/5.5/5/1.html'

    driver.get(url)

    HEXes = driver.find_elements(By.TAG_NAME,'span')
    selects = driver.find_elements(By.TAG_NAME,'select')
    checkboxes = driver.find_elements(By.CSS_SELECTOR,'input[type="checkbox"]')
    inputs = driver.find_elements(By.CSS_SELECTOR,'input[type="text"]')
    button_check_result = driver.find_elements(By.XPATH,'//button[text()="Проверить"]')
    button_general = driver.find_element(By.XPATH,'//button[text()="Проверить все элементы"]')

    for HEX in HEXes:
        joint_index = HEXes.index(HEX)
        joint_HEX = HEX.text
        joint_select = selects[joint_index]
        color_blocks = driver.find_elements(By.CSS_SELECTOR,'button[data-hex="' + joint_HEX + '"]')
        joint_color_block = color_blocks[joint_index]
        joint_checkbox = checkboxes[joint_index]
        joint_input = inputs[joint_index]
        joint_button = button_check_result[joint_index]

        Select(joint_select).select_by_value(joint_HEX)
        joint_color_block.click()
        joint_checkbox.click()
        joint_input.send_keys(joint_HEX)
        joint_button.click()

    button_general.click()

    key = driver.switch_to.alert.text
    print(f'\nYour key:\n{key}')
    assert key.isdigit(), 'Must be alert with big number, it is your key'

