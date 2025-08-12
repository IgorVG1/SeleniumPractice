from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

url = 'https://parsinger.ru/selenium/6/6.html'

class SelectMath:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def take_answer_in_math_hint(self):
        math_hint = self.driver.find_element(By.ID, 'text_box').text  # Парсим текст из элемента
        print('\nMath hint:\n' + math_hint)
        answer = str(eval(math_hint))  # Преобразуем полученный текст в код и выполняем его с помощью функции <eval()>
        print('\nYour answer"\n' + answer)

        select = self.driver.find_element(By.ID, 'selectId')
        Select(select).select_by_visible_text(answer)

    def click_button(self):
        self.driver.find_element(By.ID,'sendbutton').click()

    def check_answer_and_get_key(self):
        key = self.driver.find_element(By.ID, 'result')
        if key.is_displayed():
            print('\nChecking your answer...\nExactly!\nYour key:\n' + key.text)
        assert key.is_displayed(), 'You have taken mistake(('