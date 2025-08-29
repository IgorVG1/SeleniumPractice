from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/1/1.html'

class InputForm:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)

    def input_first_name(self):
        self.driver.find_element(By.NAME, 'first_name').send_keys('first name')

    def input_last_name(self):
        self.driver.find_element(By.NAME, 'last_name').send_keys('last name')

    def input_patronymic(self):
        self.driver.find_element(By.NAME, 'patronymic').send_keys('patronymic')

    def input_age(self):
        self.driver.find_element(By.NAME,'age').send_keys('age')

    def input_city(self):
        self.driver.find_element(By.NAME,'city').send_keys('city')

    def input_email(self):
        self.driver.find_element(By.NAME,'email').send_keys('email')

    def click_button(self):
        self.driver.find_element(By.ID,'btn').click()