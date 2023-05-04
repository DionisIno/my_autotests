import random

import allure
import pytest

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, PreventPropogationPage, \
    ReverTablePage, DragablePage


@allure.suite("Test Interactions Page")
class TestInteractions:
    @allure.feature("Test Sortable Page")
    class TestSortablePage:
        lst = ["list", "grid"]

        @pytest.mark.parametrize("item", lst)
        @allure.title("Check sortable items")
        def test_sortable_page(self, driver, item):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            before, after = sortable_page.change_items(item)
            assert before != after, "Elements have not changed"

    @allure.feature("Test Selectable Page")
    class TestSelectablePage:
        lst = ["list", "grid"]

        @pytest.mark.parametrize("item", lst)
        @allure.title("Check sortable items")
        def test_selectable_page(self, driver, item):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            content = selectable_page.get_active_items(item)
            assert len(content) > 0, "Elements has not selected"

    @allure.feature("Test Resizable Page")
    class TestResizablePage:
        @allure.title("Check size resizable box")
        def test_resizable_box_page(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            before, after = resizable_page.change_size_resizable_box()
            assert before != after, "Window size has not changed"

        @allure.title("Check size resizable")
        def test_resizable_page(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            before, after = resizable_page.change_size_resizable()
            assert before != after, "Window size has not changed"

    @allure.feature("Test Droppable Page")
    class TestDroppablePage:
        accept_list = [("acceptable", "Dropped!"),
                       ("not_acceptable", "Drop here")]

        @allure.title("Check simple droppable")
        def test_simple_droppable(self, driver):
            simple_droppable = DroppablePage(driver, "https://demoqa.com/droppable")
            simple_droppable.open()
            before, after = simple_droppable.simple_droppable()
            assert before != after, "The element has not been moved or the text has not changed"

        @pytest.mark.parametrize("item", accept_list)
        @allure.title("Check accept and not accept droppable")
        def test_accept_droppable(self, driver, item):
            accept_droppable = DroppablePage(driver, "https://demoqa.com/droppable")
            accept_droppable.open()
            text = accept_droppable.accept_droppable(item[0])
            assert item[1] == text, "Wrong text after moving element"

    class TestPreventPropogationPage:
        @allure.title("Check not greedy droppable")
        def test_prevent_page_not_greedy(self, driver):
            prevent_page = PreventPropogationPage(driver, "https://demoqa.com/droppable")
            prevent_page.open()
            text_after_outer, text_after_inner = prevent_page.move_element_inside_field()
            assert text_after_outer == text_after_inner, "Results should be the same"

        @allure.title("Check greedy droppable")
        def test_prevent_page_not_greedy(self, driver):
            prevent_page = PreventPropogationPage(driver, "https://demoqa.com/droppable")
            prevent_page.open()
            text_after_outer, text_after_inner = prevent_page.move_element_inside_field()
            assert text_after_outer != text_after_inner, "Results shouldn't be the same"

    @allure.feature("Test Rever Table")
    class TestReverTable:

        @allure.title('Check revert draggable droppable')
        def test_revert_droppable(self, driver):
            revert_droppable_page = ReverTablePage(driver, "https://demoqa.com/droppable")
            revert_droppable_page.open()
            before, after = revert_droppable_page.drop_will_revertable()
            assert before != after

        @allure.title('Check not_revert draggable droppable')
        def test_not_revert_droppable(self, driver):
            revert_droppable_page = ReverTablePage(driver, "https://demoqa.com/droppable")
            revert_droppable_page.open()
            before, after = revert_droppable_page.drop_not_revertable()
            assert before == after

    @allure.feature('Draggable Page')
    class TestDragable:
        @allure.title('Check simple draggable')
        def test_simple_dragable_page(self, driver):
            drag_able_page = DragablePage(driver, "https://demoqa.com/dragabble")
            drag_able_page.open()
            before, after = drag_able_page.simple_drag()
            assert before != after, "Element has not been moved"

        @allure.title('Check only "x" position')
        def test_simple_dragable_page(self, driver):
            drag_able_page = DragablePage(driver, "https://demoqa.com/dragabble")
            drag_able_page.open()
            before, after = drag_able_page.get_only_x_position()
            assert before != after, "Element has not been moved"

        @allure.title('Check only "y" position')
        def test_simple_dragable_page(self, driver):
            drag_able_page = DragablePage(driver, "https://demoqa.com/dragabble")
            drag_able_page.open()
            before, after = drag_able_page.get_only_y_position()
            assert before != after, "Element has not been moved"
