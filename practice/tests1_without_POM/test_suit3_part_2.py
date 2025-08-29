import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC
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