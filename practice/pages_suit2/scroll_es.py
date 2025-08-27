from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

url = 'https://parsinger.ru/selenium/7/7.1/index.html'

class ScrollExecuteScript:
    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def scroll_to_tail_page_get_and_check_key(self):
        height = self.driver.execute_script('return document.body.scrollHeight')
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        wait(self.driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, 'secret-container'), 'Пароль: E7XX-QILL-PWJ1-SE0D'))
        # time.sleep(3)
        target = self.driver.find_element(By.ID, 'secret-container').text
        print(target)
        assert target is not None