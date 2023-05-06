import random
import time

import allure
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DragablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators

    @allure.title("Get all items")
    def get_all_items(self, elem):
        item_list = self.elements_are_visible(elem)
        return [item.text for item in item_list]

    @allure.title("Change items")
    def change_items(self, item):
        value = self.element_is_visible(self.locators.ALL_LOCATORS[item][0]).get_attribute('aria-selected')
        if value == 'false':
            self.element_is_visible(self.locators.ALL_LOCATORS[item][0]).click()
        text_before = self.get_all_items(self.locators.ALL_LOCATORS[item][1])
        item_what, item_where = random.sample(self.elements_are_visible(self.locators.ALL_LOCATORS[item][1]), k=2)
        self.action_drag_and_drop_to_element(item_what, item_where)
        text_after = self.get_all_items(self.locators.ALL_LOCATORS[item][1])
        return text_before, text_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators

    @allure.title("Click random items")
    def click_random_items(self, elem):
        item_list = self.elements_are_visible(elem)
        random.sample(item_list, k=random.randint(1, 3))
        for i in range(random.randint(1, 3)):
            item_list[i].click()

    def get_active_items(self, item):
        value = self.element_is_visible(self.locators.ALL_LOCATORS[item][0]).get_attribute("aria-selected")
        if value == 'false':
            self.element_is_visible(self.locators.ALL_LOCATORS[item][0]).click()
        self.click_random_items(self.locators.ALL_LOCATORS[item][1])
        active_items = self.elements_are_visible(self.locators.ALL_LOCATORS[item][2])
        return active_items


class ResizablePage(BasePage):
    locators = ResizablePageLocators

    @allure.title("Get width and height")
    def get_width_and_height(self, elem):
        width = int(elem.split(';')[0].split()[1].replace('px', ''))
        height = int(elem.split(';')[1].split()[1].replace('px', ''))
        return [width, height]

    @allure.title("Change size resizable box")
    def change_size_resizable_box(self):
        elem = self.element_is_visible(self.locators.RESIZABLE_BOX).get_attribute('style')
        size_before = self.get_width_and_height(elem)
        handle = self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE)
        self.action_drag_and_drop_by_offset(handle, random.randint(0, 350), random.randint(0, 150))
        elem = self.element_is_visible(self.locators.RESIZABLE_BOX).get_attribute('style')
        size_after = self.get_width_and_height(elem)
        return size_before, size_after

    @allure.title("Change size resizable")
    def change_size_resizable(self):
        handle = self.element_is_present(self.locators.RESIZABLE_HANDLE)
        self.go_to_element(handle)
        elem = self.element_is_visible(self.locators.RESIZABLE).get_attribute('style')
        size_before = self.get_width_and_height(elem)
        self.action_drag_and_drop_by_offset(handle, random.randint(1, 500), random.randint(1, 500))
        time.sleep(4)
        elem = self.element_is_visible(self.locators.RESIZABLE).get_attribute('style')
        size_after = self.get_width_and_height(elem)
        return size_before, size_after


class DroppablePage(BasePage):
    locators = DroppablePageLocators

    @allure.title("Get simple droppable")
    def simple_droppable(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        what = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        text_before = self.element_is_visible(self.locators.DROP_HERE_SIMPLE).text
        where = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(what, where)
        text_after = self.element_is_visible(self.locators.DROP_HERE_SIMPLE).text
        return text_before, text_after

    @allure.title("Get accept droppable")
    def accept_droppable(self, item):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        what = self.element_is_visible(self.locators.ACCEPT_AND_NOT_ACCEPT[item])
        where = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(what, where)
        text = self.element_is_visible(self.locators.DROP_HERE_ACCEPT).text
        return text


class PreventPropogationPage(BasePage):
    locators = DroppablePageLocators

    @allure.title("Get not greedy text")
    def move_element_inside_field(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        what = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        where = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX)
        self.action_drag_and_drop_to_element(what, where)
        text_after_outer = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX_TEXT).text
        text_after_inner = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX).text
        return text_after_outer, text_after_inner

    @allure.title("Get greedy text")
    def move_element_inside_field_greedy(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        what = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        where = self.element_is_visible(self.locators.GREEDY_DROP_BOX)
        self.action_drag_and_drop_to_element(what, where)
        text_after_outer = self.element_is_visible(self.locators.GREEDY_INNER_BOX_TEXT).text
        text_after_inner = self.element_is_visible(self.locators.GREEDY_DROP_BOX).text
        return text_after_outer, text_after_inner


class ReverTablePage(BasePage):
    locators = DroppablePageLocators

    @allure.step('drop will reventable')
    def drop_will_revertable(self):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        drag_div = self.element_is_visible(self.locators.WILL_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        position_before = drag_div.get_attribute('style')
        time.sleep(1)
        position_after = drag_div.get_attribute('style')
        return position_before, position_after

    @allure.step('drop will not reventable')
    def drop_not_revertable(self):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        drag_div = self.element_is_visible(self.locators.NOT_REVERT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        position_before = drag_div.get_attribute('style')
        time.sleep(1)
        position_after = drag_div.get_attribute('style')
        print(position_before)
        print(position_after)
        return position_before, position_after


class DragablePage(BasePage):
    locators = DragablePageLocators

    @allure.step('get before and after positions')
    def simple_drag(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        what = self.element_is_visible(self.locators.SIMPLE_DRAG)
        position_before = what.get_attribute("style")
        self.action_drag_and_drop_by_offset(what, random.randint(-100, 300), random.randint(-100, 300))
        position_after = what.get_attribute("style")
        return position_before, position_after

    @allure.title("Get only 'x' position")
    def get_only_x_position(self):
        self.element_is_visible(self.locators.AXIS_TAB).click()
        what = self.element_is_visible(self.locators.ONLY_X)
        position_before = what.get_attribute("style")
        self.action_drag_and_drop_by_offset(what, random.randint(-200, 500), 0)
        position_after = what.get_attribute("style")
        return position_before, position_after

    @allure.title("Get only 'y' position")
    def get_only_y_position(self):
        self.element_is_visible(self.locators.AXIS_TAB).click()
        what = self.element_is_visible(self.locators.ONLY_Y)
        position_before = what.get_attribute("style")
        self.action_drag_and_drop_by_offset(what, 0, random.randint(-200, 500))
        position_after = what.get_attribute("style")
        return position_before, position_after
