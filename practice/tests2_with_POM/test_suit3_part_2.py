from practice.pages_suit3_part_2.lots_of_checkboxes import LotsOfCheckboxes
from practice.pages_suit3_part_2.infinity_scroll import InfinityScroll

def test_1_lots_of_checkboxes(driver):
    loc = LotsOfCheckboxes(driver)
    loc.open()
    loc.sum_all_numbers_from_each_checkbox()


def test_2_infinity_scroll(driver):
    ic = InfinityScroll(driver)
    ic.open()
    ic.scroll_to_tail_list_of_checkboxes_sum_all_numbers_of_each_checkbox_and_check_password()