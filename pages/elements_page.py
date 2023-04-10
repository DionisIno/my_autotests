from my_autotests.pages.base_page import BasePage
from my_autotests.locators.elements_page_locators import *


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()
    def fill_all_field(self):
        full_name = "Denis Denisov"
        email = "qwert@wr.ry"
        current_address ="Moscow"
        permanent_address = "Moscow"
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