from practice.pages_suit3_part_2.lots_of_checkboxes import LotsOfCheckboxes
from practice.pages_suit3_part_2.infinity_scroll import InfinityScroll
from practice.pages_suit3_part_2.infinity_scroll2 import InfinityScroll2
from practice.pages_suit3_part_2.many_scroll_containers import ManyScrollContainers

def test_1_lots_of_checkboxes(driver):
    loc = LotsOfCheckboxes(driver)
    loc.open()
    loc.sum_all_numbers_from_each_checkbox()


def test_2_infinity_scroll(driver):
    ic = InfinityScroll(driver)
    ic.open()
    ic.scroll_to_tail_list_of_checkboxes_sum_all_numbers_of_each_checkbox_and_check_password()

def test_3_infinity_scroll2(driver):
    is2 = InfinityScroll2(driver)
    is2.open()
    is2.scroll_to_tail_and_sum_all_numbers()

def test_4_many_scroll_containers(driver):
    msc = ManyScrollContainers(driver)
    msc.open()
    msc.scroll_to_tail_all_containers_and_sum_all_numbers_of_each()