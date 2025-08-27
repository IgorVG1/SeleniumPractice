
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


def test_17(driver):
    url = 'https://parsinger.ru/methods/3/index.html'

    driver.get(url)

    cookies = driver.get_cookies()
    values_secret_cookies = []

    for cookie in cookies:
        if 'secret_cookie_' in cookie['name']:
            value_cookie = int(cookie['value'])
            values_secret_cookies.append(value_cookie)

    key = sum(values_secret_cookies)
    print(f'\nYour key:\n{key}')


def test_18(driver):
    url = 'https://parsinger.ru/selenium/5.6/1/index.html'

    driver.get(url)

    cookies = [{'name': 'KXIYO4xMrWh', 'value': 'ibyAZPfXAsPqptPaNyL'},
               {'name': '0OIJ4G4ZLzK', 'value': 'kJcPzQu5Jr8ELK'},
               {'name': 'O1C4sd3RK5udnZ6P', 'value': '4mYYxbfgnIvuip2ry58EQ'},
               {'name': 'AUZgaLJ4Y', 'value': 'FLSZvYrkf1E57YMUkdD'},
               {'name': '9PWJc0VXVtnXNcS5Tf', 'value': 'YQ2G4RayBoXSEqEgA3oXRN3FAvAMT'},
               {'name': 'pN2x6MDb', 'value': 'htbtD59XD3vCemHRCe9iUxV1smvXAIk5XOwuHnnmMB0'},
               {'name': 'AsqpQd', 'value': 'uNFFRiqeRrj25MwJajG4AxeKvCxKbHUSbbvzb3C'},
               {'name': '73PVEdwTk0txDp4L', 'value': 'DTniz3Fwj110H24dfZfd5JqqfEtN'},
               {'name': 'jZ1MwGy5z0L8ZW00U', 'value': 'sspfahNvfeo3zHWAIW0jdp2A9LyDbIm0'},
               {'name': 'aLRosjpBhYrZ0J69a', 'value': 'zcoXWv5L9Pz5kwGeyP5jlAQ'},
               {'name': '9LPCTyKTNmvBcnZ', 'value': 'GWBjw1Gosk4IKxuh5J2eu0ikgowOaZwP8FOm1ekKeQIxJDIXBy'},
               {'name': 'psH0h', 'value': 'wNAUmVlQwG6VK5TvDfryipzWeLXX46WDbXUd8yGrhrA3Hnc'},
               {'name': 'BULl3P', 'value': 'wefA0ljyA82kYpV1OoOixtAIp6xjmiQlS9SLeN'},
               {'name': '3bIJVJCylqgshRC9r1dH', 'value': '6Y6EZE5dttgx7rKzP881nAhRPE'},
               {'name': 'dBDhCzi6VO0', 'value': 'LKMcpZ6bEJy5IY352OMViznSP5OMqS9IgZB0YMv'},
               {'name': '6SGnnuoZ7v', 'value': '6asdYiIPBsMEdO0mQ9Jlq0mSMbJjfg'},
               {'name': '4dfAVZ1qZwijwYMUj', 'value': '3TOxOPelSdN6cK273'},
               {'name': 'RMOPZQILwFr3o637M', 'value': 'RZoaTFTdytqxB6sZhO4ebrhWlxjhMoQn8ZiObpdcGgH'},
               {'name': '08cQ7E3qHOOMk4uy1fLz', 'value': 'YfYkz9boRjDHLTahMuZcAJPzbjwTlRt1iNZzGl'},
               {'name': 'YT1NKf55egy', 'value': '3MSmfnklFY5TzvM8np4guMsJYtmdHmbyHiz3Vp6Rtk7r4GWhC'},
               {'name': 'cTKnm0a3H2euL46Ibi', 'value': 'HCZ0KYkidXfFowGinPuWG19cT79gEJC'},
               {'name': 'mvAz0P7Igjs2JY', 'value': '8O67zvSDHJx'},
               {'name': 'TzWXbWMvDBcKTo', 'value': 'dzwNYZCg4jpxKtpCeumwq0DO2KtGWLIHpQLOrzmGbXMC8G'},
               {'name': '1BMgyMHkzUemIEr', 'value': '08Sd1v8kQi6eB1FTs9qfjDkJ9UfKCLOFGtDgbOlu9v9iiuu'},
               {'name': 'Jig5voy', 'value': 'Pi4OA6hY21TeHlHyPMaMFHgY0BZRcQ9V0nXg'},
               {'name': '10wa7lhCoJXIzEYW5kQ', 'value': 'BFp4YeKWKVKXHTOesJLleaAelwYwPz51C95IYzd'},
               {'name': 'BqXt5D', 'value': 'n99ZSFFhseCs7aVjU31pYSJxqMgFYGfreFZl9ixb2NNHRBp'},
               {'name': 'GJunU5e1BEvfd', 'value': 'y5YFJ3hF9hG45G86MD9W9nRk61JMsh8rsmbFFrDoeJVUfyBvZ'},
               {'name': 'itFJBn79wksvZ15lc2', 'value': 'nXpdqpt0Po84uOuSU'},
               {'name': 'O5Q70eOB5ivJt5DZ', 'value': 'AZRr2ATREeF9HQR2opgF'},
               {'name': '6jBEUxI0a7x790m', 'value': 'comi8Mx5ig95NAiSO8'},
               {'name': 'KpVF7aIkav32LuqIDI', 'value': 'ik4furgLieyUawgJpttvHxWoXm2zO19'},
               {'name': 'OTRFyN', 'value': 'vlzV7Z97sWcJStZgDJiRjzIf'},
               {'name': 'hKLzMbgdIlUTAMYSEo', 'value': 'Tq2l0QJ3ekwxY3uaC8n2ln1nDMWhltFQm2TNaBefAAzk'},
               {'name': 'GJKNrAvRn', 'value': 'dByJXuSsAIz3Rnqa9BvU11okpnSydEZnkaqMQu9RoE'},
               {'name': 'AowB8Q3t74JHmXTGc1', 'value': '02JklRAtbsNNe'},
               {'name': 'xPpvKmo03bGBYrmqw', 'value': '7bf4FgaLKoj6YvGq4huLT5r9eCflo70QhI9gAPkMIuj4Bg'},
               {'name': '8UqFFBP3Dm0s6XM', 'value': 'kSZJPw6oTBwqG94q'},
               {'name': 'WeeXL7bKNWIZZkgX', 'value': 'ap3DPbBYqlfEOZ6'},
               {'name': 'fhdSevpxKUzledgGtbL4', 'value': 'v5I4A3PFOlN9zWPDkedlC2eLbMZ5cn3cf8'},
               {'name': '3H6lO', 'value': 'jxc9994fPQBKpnyr8aZBDZlMAolnxXh'},
               {'name': 'QVen8QnA1648g4Dm9p', 'value': 'RXNYpaUTJlD4xVIOm'},
               {'name': '3PxMnD9w', 'value': 'JC74xNLEc5ujZge7OmXj5EWk3hwdm4OH8FgF60D6pFl'},
               {'name': 'o8yY57CZSN', 'value': 'afO10rX663gaVttfSxeE70Gd22JKxwJAli7EhEdzkxxME'},
               {'name': 'UpAdf46rvxXW', 'value': 'Ft2FEQV71gLnG'},
               {'name': 'WRrpVIAkMKiZVxHt299', 'value': 'FC53hjqCGooNgV'},
               {'name': 'XHViH149aRl5', 'value': 'YbozZeoGCt3gO1kRMoLExcfCotBz'},
               {'name': 'yjNLzeR4k', 'value': 'Chd2mmuK7nxuVTi'},
               {'name': '5M4RGm', 'value': 'tj3HWN5mVpz9zgIie2ac2KHKIeABaou'},
               {'name': 'CcxIZZYgojDZpHnO9zJl', 'value': 'xLiql8yXUxULBG9w2snaMLI4FjSyX'},
               {'name': 'NScrEjcTmwo639PQqki', 'value': 'eOSFemtdjyphiPubTAzTICUhgw92By'},
               {'name': '9b5OpL5NrCpmtsE', 'value': 'VKdEIeX5ZNTghD6sq3qyjBHJaUuXfpQ7YnYb'},
               {'name': 'uyBoiSTHTtxV8Wszttb', 'value': 'SHEEfVcj1jNv3V1oqeT2wfEbWKZ0uJ2ljwv'},
               {'name': 'qR6AeEoEbQb1GYRj', 'value': 'mA66a177y8e6Nm7BlKBvpcUrM3fm6y4K'},
               {'name': 'l0Y9gn8MNtC', 'value': 'M1L2OUmAisn1c6DNB9mJfTHRM9V3HuXUAEGG8Zx'},
               {'name': 'L8m4GeWyECR', 'value': 'QuFfnWXebyrwwqXfVvAN2dbSisST8IgGyLggrVzTjaCeQ'},
               {'name': 'GxJSMQh9aZjFdhgjaAj', 'value': 'phOonlKiMt0xLDtvoB52TbATS1Ggm4Pv5lztk5vTNkXVqp'},
               {'name': 'GRE1eZ8D1bb', 'value': 'llpIP76V4S978YmQcfW'},
               {'name': 'dooT1cyS41bIWEB9c', 'value': 'ORu004k9aFl9FdS77Iz'},
               {'name': 'csjauyxnCpBySvkXTDzS', 'value': 'SJKqcIqWDbUJbxnHfD8jNJzYKb3Yp3TPIRDIpxCNB'},
               {'name': 'Y6CgAqWN8', 'value': 'qu0g6xEm0iJeTKM8NfOZUxP0XQaCtUfiTWHtQJ5soU5cpZ'},
               {'name': 'xxtL44KLbN60b5q', 'value': 'RSNFhhicL7pWpo3gvE3tJbHaIjU'},
               {'name': 'KcvqC30', 'value': '58IlGI646RMaGMYtL5XYqxFq8UaMwjPDNFNApAuDpUI9tMoM4t'},
               {'name': 'y761v6wZDo3V7O', 'value': '3i9iZjnZXdHlJxDz7ZrkPthYdI3PowS5yRomV0v8fR9WVco4'},
               {'name': 'Ixr7AetyC', 'value': 'lYRaNZAnoNHc9UZIoXI9E'},
               {'name': 'QIvvsr04T0JGVJE', 'value': 'tr6fE8moJI897w967QTmKojC730GdkKTUonevQbYsHQ71mi'},
               {'name': 'CBTq9zQjJx', 'value': 'z7BuIeFufYeZysVnrglrDJk8KW8UBWYt62'},
               {'name': '2ALhFQM7svECfgsSaiTa', 'value': 'VGMsulQVoobUe4m6w8dZGej8jFzSES3hzl9OG2csqpl'},
               {'name': '7VQixJTzu2H', 'value': 'jPnLpldHTFNgPCH1RUlmRQx7N58P7CQHajLYvGxho'},
               {'name': 'KdmUSh1SJH6M9', 'value': 'HPKIgmOBqq6Ln6QSPKedXuFpOoWhrOUzCxRMlcoJ2Gd0S7Hd'},
               {'name': 't6B9gl6QeGEDl1LW', 'value': 'kGs0hk4Pmeb83dBbuHTSzIVNcY0G4iucq73lkCMwt6Akv4w'},
               {'name': 'gcjmy3', 'value': 'QtB6duKOGc7eNc9MFwiOOaikXCYQg6dO4m66sJJxkRebKIKiR'},
               {'name': '2oBZU9j', 'value': '2U80qbFDpRElKTshedtaZ42OzYG48OQckEt2Zy9D7T'},
               {'name': 'g2tyy8erqS4E5pdSynCB', 'value': 'VN5zSYJpNHQC14FVl'},
               {'name': 'lLhLcbED3XAgAPaMp', 'value': 'tBUVWsfSNg0Iv4TLPAmBRm2m2nrWh'},
               {'name': 'iUfgKa7OX', 'value': 'GtyGoiA00RNiTgqvbXs78khbzQ7d0rh5xTk1aZK'},
               {'name': 'WQGGXKzZXvRXLC0', 'value': 'itGXA2mVtchzcqstP39BvfBvwh'},
               {'name': 'p37sYwX5mgtwXJl3yFBL', 'value': 'h20iY8XooVE'},
               {'name': 'tubsOLf', 'value': 'YGlaF0EEJrT1c5Z2HBAWnc1Q3an3Ob'},
               {'name': 'mg1Pr2NJJEnw2UkGFg', 'value': 'L48wovkYz32wa16iiswcgbA6JmyVoysUqjfm4i7'},
               {'name': 'V55E3ui8KHXybSDSSnoc', 'value': '7rhA8PSMZFy1aC8CQXbitOxY0qdUkDOUWijijIvlHhtB0q1'},
               {'name': 'AcWBQQy', 'value': 'zl1GXRHA3neBLCN8'},
               {'name': 'PtvgV4eJ21CrPE3xeH9', 'value': '1tU9KvLdq2uRNRKtA'},
               {'name': 'XjuSocgLwoMvFo8a', 'value': 'pvmx5A97Sad0U6d6i'},
               {'name': 'mMpdmPLcZEAZDzNyA8a2', 'value': 'WG6CrZ3zXfxN84hJXUKJq0ZroYditsADYplxwhkgXkUcZ'},
               {'name': 'tojhHp0ZlGrZ8Y3', 'value': 'fqpJvGkfQRT7ytNTU5KPum150MmcVR1nja0QIQRVEOPiNvT7Pg'},
               {'name': 'LDHgCR5PNoqYdffU5', 'value': '7a0tCBgGzylPTGUStOuNXORrRWwy03Upm2CvJX'},
               {'name': 'F4xcvPzuYYAvDrvDi', 'value': 'zQEpxlKpKprtwFbJyx0XYxFrlc8XP2RhRG'},
               {'name': 'fmnoi', 'value': 'yB9333KC4bP4SHUF90Kj7OC9QXz22WAZ3xtZxLi9'},
               {'name': 'TbGdmTkjcC52T7q', 'value': '2HCejTOfB98e30JMj3Pz9Ok9xLz5Y9lkaJaHoRF2vA5xq0i'},
               {'name': 'tg3vMrNIZHs', 'value': '2XRV99ShR8yc0bCe0QOuC9xd0A'},
               {'name': '8FaJo5TVO7TmoOI', 'value': 'bGYulAOS3ARzN3Rsyx9JJzu'},
               {'name': 'YLBwBAUCJ05p5fx2', 'value': 'Z8lGSb7AnZKVwlIqKgRIafpIfTVufj'},
               {'name': 'fpZCwfH', 'value': 'cqo4KOj8LSagd6VUhBrq6RJtUquwK7mJaDQsQb'},
               {'name': 'zjUiv081bH', 'value': 'LSJtgc56ylEJGMd1AhE9QcXudC8g'},
               {'name': 'yiWR1RtAnWH71I1', 'value': 'ruskXwdCQOfbfIgtKcetVb'},
               {'name': 'KMKvYURaBlIEmtyX', 'value': 'NFIzhI600J5QYN'},
               {'name': 'hbFS4sDwQh', 'value': 's4zWhushscPPDDFqT5tzPJqix0HMjjG'},
               {'name': 'b9wAAVSyw4V2LQ', 'value': 'SDkldbPnf6NjLZSxWZV7CpCW'},
               {'name': 'jFhFn0wPFRG', 'value': 'RYqOrD21ZN7aUeBXqISZ2afocnvvwd6hw3BXUj1wEm0mUO'}]

    win_age = 100
    win_skills = 0
    index_winner = 0

    for cookie in cookies:
        driver.add_cookie(cookie)
        driver.refresh()
        wait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'age')))

        age_input = driver.find_element(By.ID,'age').text
        age_input_parts = age_input.split(' ')
        age_string = age_input_parts[-1]
        age = int(age_string)

        skill_inputs = driver.find_elements(By.TAG_NAME,'li')
        skills = len(skill_inputs)

        if age < win_age:
            win_age = age
            win_skills = skills
            index_winner = cookies.index(cookie)

        elif age == win_age:
            if skills > win_skills:
                win_age = age
                win_skills = skills
                index_winner = cookies.index(cookie)

        driver.delete_all_cookies()

    print(f'\nAge winner:{win_age}\nAmount skills winner:{win_skills}')
    winner = cookies[index_winner]
    key = winner["value"]
    print(key)
