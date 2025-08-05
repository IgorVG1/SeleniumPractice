import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Генератор пар тестовых данных (PairWiseTesting)

emails = ['email1@email.com','email2@email.com','email3@email.com']
passwords = ['Password1!','Password2!','Password3!']

def generate_pairs():
    pairs = []
    for email in emails:
        for password in passwords:
            pairs.append(pytest.param((email, password),id = f'Email: {email} Password: {password}'))
    return pairs

# Альтернативный путь: в ручную создать все комбинации данных

# @pytest.mark.parametrize(
#    'data',
#    [
#        pytest.param(('email1@email.com','Password1!'), id = 'Email: email1@email.com Password: Password1!'),
#        pytest.param(('email2@email.com','Password2!'), id = 'Email: email2@email.com Password: Password2!'),
#        pytest.param(('email3@email.com','Password3!'), id = 'Email: email3@email.com Password: Password3!')
#    ]
#)

@pytest.mark.parametrize(
    'data',
    generate_pairs()
)

def test_1(driver,data):

    login, passw = data

    driver.get('https://www.qa-practice.com/elements/input/email')

    input_email = driver.find_element(By.ID,'id_email')
    input_email.send_keys(login)
    input_email.send_keys(Keys.ENTER)

    text_message_after_login = driver.find_element(By.ID,'result')
    assert text_message_after_login.is_displayed()
    print('\nLogin correct')

    driver.find_element(By.XPATH,'//a[text()="Password field"]').click()

    input_password = driver.find_element(By.NAME,'password')
    input_password.send_keys(passw)
    input_password.send_keys(Keys.ENTER)

    text_message_after_passw = driver.find_element(By.NAME,'result')
    assert text_message_after_passw.is_displayed()
    print('\nPassword correct')