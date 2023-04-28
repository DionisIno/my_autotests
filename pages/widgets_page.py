import random
import time

from selenium.webdriver import Keys

from generator.generator import *
from locators.widgets_page_locators import *
from pages.base_page import *


class AccordianPage(BasePage):
    locators = AccordianPageLocators

    @allure.title("check text in the cards")
    def check_text_in_cards(self, item):
        if item == "what":
            content = self.element_is_visible(self.locators.WHAT).text
            return content, "What is Lorem Ipsum?"
        elif item == "where":
            content = self.element_is_visible(self.locators.WHERE).text
            return content, "Where does it come from?"
        elif item == "why":
            content = self.element_is_visible(self.locators.WHY).text
            return content, "Why do we use it?"

    @allure.title("check text from the cards")
    def check_content_from_card(self, item):
        time.sleep(1)
        if item == "what":
            check_attribute = self.element_is_present(self.locators.WHAT_CONTENT_CHECK).get_attribute('class')
            if check_attribute == "collapse show":
                content = self.element_is_visible(self.locators.WHAT_CONTENT).text
                return content
            else:
                self.element_is_visible(self.locators.WHAT).click()
                time.sleep(1)
                content = self.element_is_visible(self.locators.WHAT_CONTENT).text
                return content
        elif item == "where":
            check_attribute = self.element_is_present(self.locators.WHERE_CONTENT_CHECK).get_attribute('class')
            if check_attribute == "collapse show":
                content = self.element_is_visible(self.locators.WHERE_CONTENT).text
                return content
            else:
                self.element_is_visible(self.locators.WHERE).click()
                time.sleep(1)
                content = self.element_is_present(self.locators.WHERE_CONTENT).text
                return content
        elif item == "why":
            check_attribute = self.element_is_present(self.locators.WHY_CONTENT_CHECK).get_attribute('class')
            if check_attribute == "collapse show":
                content = self.element_is_visible(self.locators.WHY_CONTENT).text
                return content
            else:
                self.element_is_visible(self.locators.WHY).click()
                time.sleep(1)
                content = self.element_is_present(self.locators.WHY_CONTENT).text
                return content


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators

    @allure.title("Fill multi color names")
    def fill_multi_color(self, item):
        colors = random.sample(next(generator_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_color = self.element_is_visible(self.locators.MULTI_COLOR)
            input_color.send_keys(color)
            input_color.send_keys(Keys.ENTER)


