from practice.pages.input_form import InputForm
from practice.pages.link_secret import LinkSecret
from practice.pages.grand_sum import GrandSum
from practice.pages.little_sum import LittleSum
from practice.pages.many_checkboxes import ManyCheckboxes
from practice.pages.special_checkboxes import SpecialCheckboxes
from practice.pages.select_sum import SelectSum
from practice.pages.select_math import SelectMath

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


def test_6(driver):

    special_checkboxes = SpecialCheckboxes(driver)

    special_checkboxes.open()
    special_checkboxes.click_only_special_checkboxes()
    special_checkboxes.click_button()
    special_checkboxes.check_key_present()


def test_7(driver):

    select_sum = SelectSum(driver)

    select_sum.open()
    select_sum.sum_all_value_options_of_select_and_input_result()
    select_sum.click_button()
    select_sum.check_key_present()


def test_8(driver):

    select_math = SelectMath(driver)

    select_math.open()
    select_math.take_answer_in_math_hint()
    select_math.click_button()
    select_math.check_answer_and_get_key()
