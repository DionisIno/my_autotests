from my_autotests.pages.base_page import BasePage
from my_autotests.locators.elements_page_locators import *
from my_autotests.generator.generator import *


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()
    def fill_all_field(self):
        info = next(get_person())
        full_name = info.full_name
        email = info.email
        current_address = info.current_address
        permanent_address = info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADRES).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADRES).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_field(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address

class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_BUTTON).click()

    def click_random(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 5
        while count !=0:
            item = item_list[random.randint(1, 16)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_box(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        lst = []
        for i in checked_list:
            item = i.find_element("xpath", self.locators.TITLE_ITEM)
            lst.append(item.text)
        return str(lst).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT)
        lst = []
        for i in result_list:
            lst.append(i.text)
        return str(lst).replace(' ', '').lower()
