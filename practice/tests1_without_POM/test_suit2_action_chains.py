import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC

def test_0_scroll_by_execute_script(driver):
    url = 'https://parsinger.ru/selenium/7/7.1/index.html'
    driver.get(url)

    height = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    wait(driver,5).until(EC.text_to_be_present_in_element((By.ID,'secret-container'),'Пароль: E7XX-QILL-PWJ1-SE0D'))
    #time.sleep(3)
    target = driver.find_element(By.ID,'secret-container').text
    print(target)
    assert target is not None

def test_1_scroll_by_send_keys(driver):
    url = 'https://parsinger.ru/selenium/7/7.2/index.html'
    driver.get(url)

    for i in range(100):
        inputs = driver.find_elements(By.CLASS_NAME,'interactive')
        inputs[i].send_keys('abc')
        inputs[i].send_keys(Keys.ENTER)
        inputs[i].send_keys(Keys.ARROW_DOWN)

    wait(driver,5).until(EC.text_to_be_present_in_element((By.ID,'hidden-password'),'Пароль: Wasteland-Survivor-2077'))
    pwd = driver.find_element(By.ID,'hidden-password').text
    print(f'\n{pwd}')

    assert pwd is not None

def test_2_drag_and_drop(driver):
    actions = AC(driver)

    url = 'https://parsinger.ru/selenium/7/7.3.1/index.html'
    driver.get(url)

    source = driver.find_element(By.ID,'draggable')
    target = driver.find_element(By.ID,'target')
    actions.drag_and_drop(source, target).perform()

    pwd = driver.find_element(By.ID,'password').text
    print(f'\nYour password:\n{pwd}')
    assert pwd is not None, 'In screen must present password'

def test_3_double_click(driver):
    actions = AC(driver)

    url = 'https://parsinger.ru/selenium/7/7.3.2/index.html'
    driver.get(url)

    element = driver.find_element(By.ID,'dblclick-area')
    actions.double_click(element).perform()

    pwd = driver.find_element(By.ID,'password').text
    print(f'\nYour password:\n{pwd}')
    assert pwd is not None, 'In screen must present password'

def test_4_combo_keys(driver):
    actions = AC(driver)

    url = 'https://parsinger.ru/selenium/7/7.3.3/index.html'
    driver.get(url)

    actions\
        .key_down(Keys.CONTROL)\
        .key_down(Keys.ALT)\
        .key_down(Keys.SHIFT)\
        .send_keys('T')\
        .key_up(Keys.CONTROL)\
        .key_up(Keys.ALT)\
        .key_up(Keys.SHIFT)\
        .perform()

    key = driver.find_element(By.CSS_SELECTOR,'span[key="access_code"]').text
    print(f'\nYour password:\n{key}')
    assert key is not None, 'In screen must present password'

def test_5_context_click(driver):
    actions = AC(driver)

    url = 'https://parsinger.ru/selenium/7/7.3.4/index.html'
    driver.get(url)

    element = driver.find_element(By.ID,'context-area')
    actions.context_click(element).perform()

    driver.find_element(By.CSS_SELECTOR,'div[data-action="get_password"]').click()

    key = driver.find_element(By.CSS_SELECTOR,'span[key="access_code"]').text
    print(f'\nYour password:\n{key}')
    assert key is not None, 'In screen must present password'

def test_6_scroll_to_end(driver):
    actions = AC(driver)

    url = 'https://parsinger.ru/selenium/7/7.3.5/index.html'
    driver.get(url)

    lc = driver.find_element(By.ID,'scrollable-container-left')
    rc = driver.find_element(By.ID,'scrollable-container-right')
    actions\
        .click(lc).send_keys(Keys.END)\
        .click(rc).send_keys(Keys.END)\
        .perform()

    wait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'span[key="access_code"]')))
    key = driver.find_element(By.CSS_SELECTOR,'span[key="access_code"]').text
    print(f'\nYour password:\n{key}')
    assert key is not None, 'In screen must present password'

def test_7_scroll_by_amount(driver):
    url = 'https://parsinger.ru/selenium/7/7.4.1/index.html'
    driver.get(url)

    actions = AC(driver)
    actions.scroll_by_amount(0,750).perform()

    time.sleep(3.5)

    full_text = driver.find_element(By.CSS_SELECTOR,'div.countdown').text
    parts_text = full_text.split(' ')
    key = parts_text[-1]

    actions.scroll_by_amount(0, 1500).perform()
    input_key = driver.find_element(By.CSS_SELECTOR,'input[type="text"]')
    input_key.send_keys(key)

    driver.find_element(By.TAG_NAME,'button').click()

    password = driver.find_element(By.ID,'final-key').text
    print(f'\n{password}')