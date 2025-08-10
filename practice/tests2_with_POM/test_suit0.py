from practice.pages.input_form import InputForm
from practice.pages.link_secret import LinkSecret
from practice.pages.grand_sum import GrandSum
from practice.pages.little_sum import LittleSum
from practice.pages.many_checkboxes import ManyCheckboxes

import time

def test_1(driver):
    input_form = InputForm(driver)

    input_form.open()
    input_form.input_first_name()
    input_form.input_last_name()
    input_form.input_patronymic()
    input_form.input_age()
    input_form.input_city()
    input_form.input_email()
    input_form.click_button()

    time.sleep(3)


def test_2(driver):
    link_secret = LinkSecret(driver)

    link_secret.open()
    link_secret.find_and_open_secret_link()
    link_secret.check_extra_key()


def test_3(driver):
    grand_sum = GrandSum(driver)

    grand_sum.open()
    grand_sum.get_sum_all_numerics_from_all_tables_and_check()


def test_4(driver):
    little_sum = LittleSum(driver)

    little_sum.open()
    little_sum.get_sum_all_numerics_from_each_second_graph_in_table_and_check()


def test_5(driver):
    many_checkboxes = ManyCheckboxes(driver)

    many_checkboxes.open()
    many_checkboxes.click_all_checkboxes()
    many_checkboxes.click_button()
    many_checkboxes.check_and_copy_result_key()
