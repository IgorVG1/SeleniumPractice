from practice.pages_suit2.scroll_es import ScrollExecuteScript
from practice.pages_suit2.scroll_sk import ScrollSendKeys
from practice.pages_suit2.drag_and_drop import DragAndDrop
from practice.pages_suit2.double_click import DoubleClick
from practice.pages_suit2.combo_keys import ComboKeys
from practice.pages_suit2.context_click import ContextClick
from practice.pages_suit2.scroll_to_end import ScrollToEnd

def test_0_scroll_by_execute_script(driver):
    ses = ScrollExecuteScript(driver)
    ses.open()
    ses.scroll_to_tail_page_get_and_check_key()


def test_1_scroll_by_send_keys(driver):
    ssk = ScrollSendKeys(driver)
    ssk.open()
    ssk.input_all_form_get_and_check_key()


def test_2_drag_and_drop(driver):
    dad = DragAndDrop(driver)
    dad.open()
    dad.drag_and_drop_target()
    dad.get_and_check_key()


def test_3_double_click(driver):
    dc = DoubleClick(driver)
    dc.open()
    dc.double_click_on_target()
    dc.get_and_check_key()


def test_4_combo_keys(driver):
    ck = ComboKeys(driver)
    ck.open()
    ck.take_combo_needed_keys()
    ck.get_and_check_key()


def test_5_context_click(driver):
    cc = ContextClick(driver)
    cc.open()
    cc.context_click_on_target()
    cc.click_to_get_key()
    cc.get_and_check_key()


def test_6_scroll_to_end(driver):
    ste = ScrollToEnd(driver)
    ste.open()
    ste.scroll_to_end_left_and_right_container()
    ste.get_and_check_key()

