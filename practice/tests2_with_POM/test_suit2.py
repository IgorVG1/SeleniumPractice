import pytest

from practice.pages.qa_practice_input_field import EmailField, PasswordField


# Генератор пар тестовых данных (PairWiseTesting)

emails = ['email1@email.com','email2@email.com','email3@email.com']
passwords = ['Password1!','Password2!','Password3!']

def generate_pairs():
    pairs = []
    for email in emails:
        for password in passwords:
            pairs.append(pytest.param((email, password),id = f'Email: {email} Password: {password}'))
    return pairs


@pytest.mark.parametrize(
    'data',
    generate_pairs()
)

def test_1(driver,data):

    login, passw = data

    ef = EmailField(driver)
    pf = PasswordField(driver)

    ef.open_page_email_field()
    ef.input_email(login)
    ef.check_login_correct()

    ef.open_page_password_field()

    pf.input_password(passw)
    pf.check_password_correct()