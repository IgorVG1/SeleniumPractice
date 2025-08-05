from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

link_email_field = 'https://www.qa-practice.com/elements/input/email'
link_password_field = 'https://www.qa-practice.com/elements/input/passwd'

class EmailField:

    def __init__(self, driver):
        self.driver = driver

    def open_page_email_field(self):
        self.driver.get(link_email_field)

    def input_email(self, input_email_data):
        input_email = self.driver.find_element(By.ID, 'id_email')
        input_email.send_keys(input_email_data)
        input_email.send_keys(Keys.ENTER)

    def check_login_correct(self):
        text_message_after_login = self.driver.find_element(By.ID, 'result')
        assert text_message_after_login.is_displayed()
        print('\nLogin correct')

    def open_page_password_field(self):
        self.driver.find_element(By.XPATH, '//a[text()="Password field"]').click()

class PasswordField:

    def __init__(self, driver):
        self.driver = driver

    def input_password(self, input_password_data):
        input_password = self.driver.find_element(By.NAME, 'password')
        input_password.send_keys(input_password_data)
        input_password.send_keys(Keys.ENTER)

    def check_password_correct(self):
        text_message_after_passw = self.driver.find_element(By.NAME, 'result')
        assert text_message_after_passw.is_displayed()
        print('\nPassword correct')