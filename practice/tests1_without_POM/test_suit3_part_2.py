import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.action_chains import ScrollOrigin as SO
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

def test_1_lots_of_checkboxes(driver):
    url = 'https://parsinger.ru/scroll/2/index.html'
    driver.get(url)

    all_summand = []
    checkboxes = driver.find_elements(By.CSS_SELECTOR,'input.checkbox_class')
    spans = driver.find_elements(By.TAG_NAME,'span')

    for checkbox in checkboxes:
        joint_index = checkboxes.index(checkbox)

        checkbox.click()

        summand = spans[joint_index].text
        if summand.isdigit():
            all_summand.append(int(summand))

    sum_up = sum(all_summand)
    print(f'\nSum of all numbers in checkboxes:\n{sum_up}')

def test_2_infinity_scroll(driver):
    url = 'https://parsinger.ru/infiniti_scroll_1/'
    driver.get(url)

    actions = AC(driver)
    all_summand = []
    time.sleep(2)

    for i in range(100):
        checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
        spans = driver.find_elements(By.TAG_NAME,'span')

        wait(driver,5).until(EC.element_to_be_clickable(checkboxes[i]))

        checkboxes[i].click()
        actions.send_keys(Keys.ARROW_DOWN).perform()
        summand = int(spans[i].text)
        all_summand.append(summand)

    pswd = sum(all_summand)
    print(f'\nYour password:\n{pswd}')
    assert pswd == 86049950, '\nCorrect password:\n86049950'

def test_3_infinity_scroll2(driver):
    url = 'https://parsinger.ru/infiniti_scroll_2/'
    driver.get(url)
    time.sleep(1)

    actions = AC(driver)
    all_summand = []

    for i in range(100):
        tables = driver.find_elements(By.TAG_NAME, 'p')
        actions.move_to_element(tables[i]).send_keys(Keys.ARROW_DOWN).perform()

        summand = int(tables[i].text)
        all_summand.append(summand)

    summa = sum(all_summand)
    print(f'\nSum of all numbers:\n{summa}')

def test_4_many_scroll_containers(driver):
    url = 'https://parsinger.ru/infiniti_scroll_3/'
    driver.get(url)

    actions = AC(driver)
    scroll_containers = driver.find_elements(By.XPATH,'//div[@class="main"]/div')
    all_sum_of_container = []

    for container in scroll_containers:

        target = container.find_element(By.CSS_SELECTOR,'div div')
        all_summand = []

        for i in range(8):
            actions.click(target)\
                .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN)\
                .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN)\
                .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()

        spans = container.find_elements(By.TAG_NAME, 'span')

        for span in spans:
            summand = int(span.text)
            all_summand.append(summand)

        sum_of_container = sum(all_summand)
        print(f'\nSum of container #{scroll_containers.index(container)}:\n{sum_of_container}')
        all_sum_of_container.append(sum_of_container)

    pswd = sum(all_sum_of_container)
    print(f'\nYour password:\n{pswd}')

def test_5_uran_collecting(driver):
    url = 'https://parsinger.ru/selenium/5.7/1/index.html'
    driver.get(url)

    urans = driver.find_elements(By.CLASS_NAME,'button-container')
    for uran in urans:
        driver.execute_script("return arguments[0].scrollIntoView(true);",uran)
        uran.click()

    key = driver.switch_to.alert.text
    print(f'\nYour key:\n{key}')
    assert driver.switch_to.alert, 'Must be displayed alert with key'

def test_6_interactive_buttons(driver):
    url = 'https://parsinger.ru/selenium/5.7/5/index.html'
    driver.get(url)

    actions = AC(driver)

    buttons = driver.find_elements(By.CLASS_NAME,'timer_button')
    for button in buttons:
        while not button.get_attribute('style') == "background-color: green;":
            actions.click_and_hold(button).perform()

    actions.reset_actions()
    wait(driver,5).until(EC.alert_is_present())
    key = driver.switch_to.alert.text
    print(f'\nYour key:\n{key}')
    assert driver.switch_to.alert, 'Must be displayed alert with key'

def test_7_infinity_checkboxes(driver):
    url = 'https://parsinger.ru/selenium/5.7/4/index.html'
    driver.get(url)
    wait(driver,5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,'child_container')))

    target = driver.find_element(By.XPATH, '//div[@id="main_container"]')
    actions = AC(driver)

    for i in range(20):
        actions.click(target)\
            .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN)\
            .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN)\
            .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN)\
            .perform()

    tables = driver.find_elements(By.CLASS_NAME,'child_container')
    for table in tables:
        checkboxes = table.find_elements(By.TAG_NAME,'input')
        for checkbox in checkboxes:
            checkbox_value = int(checkbox.get_attribute('value'))
            if checkbox_value % 2 == 0:
                checkbox.click()

    driver.find_element(By.CLASS_NAME,'alert_button').click()

    alert = driver.switch_to.alert
    key = alert.text
    print(f'\nYour key:\n{key}')
    assert alert, 'Alert must be displayed with your key'

def test_8_gods_like(driver):
    url = 'https://parsinger.ru/selenium/7/7.5/index.html'
    driver.get(url)

    actions = AC(driver)
    all_summand = []
    wait(driver,5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'card')))

    for i in range(100):
        cards = driver.find_elements(By.CLASS_NAME,'card')
        cards[i].find_element(By.CLASS_NAME,'like-btn').click()
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(0.05)
        summand = int(cards[i].find_element(By.CLASS_NAME,'big-number').text)
        all_summand.append(summand)

    key = sum(all_summand)
    print(f'\nYour key:\n{key}')