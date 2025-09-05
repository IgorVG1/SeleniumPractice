from practice.pages_suit3_part_2.lots_of_checkboxes import LotsOfCheckboxes
from practice.pages_suit3_part_2.infinity_scroll import InfinityScroll
from practice.pages_suit3_part_2.infinity_scroll2 import InfinityScroll2
from practice.pages_suit3_part_2.many_scroll_containers import ManyScrollContainers
from practice.pages_suit3_part_2.uran_collecting import UranCollecting
from practice.pages_suit3_part_2.interactive_buttons import InteractiveButtons
from practice.pages_suit3_part_2.infinity_checkboxes import InfinityCheckboxes
from practice.pages_suit3_part_2.gods_like import GodsLike

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

def test_5_uran_collecting(driver):
    uc = UranCollecting(driver)
    uc.open()
    uc.collect_all_uranium_and_check_key()

def test_6_interactive_buttons(driver):
    ib = InteractiveButtons(driver)
    ib.open()
    ib.click_all_button_and_check_key()

def test_7_infinity_checkboxes(driver):
    ic = InfinityCheckboxes(driver)
    ic.open()
    ic.select_all_odd_checkboxes_in_each_table()
    ic.click_button_and_check_key_from_alert()

def test_8_gods_like(driver):
    gl = GodsLike(driver)
    gl.open()
    gl.likes_all_cards_and_sum_their_values()