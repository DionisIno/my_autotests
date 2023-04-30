import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
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
    def fill_input_multi(self):
        colors = random.sample(next(generator_color()).color_name, k=random.randint(3, 5))
        for color in colors:
            input_multi = self.element_is_clicable(self.locators.MULTI_COLOR)
            time.sleep(1)
            input_multi.send_keys(color)
            time.sleep(1)
            input_multi.send_keys(Keys.ENTER)
            time.sleep(1)
            input_multi.send_keys(Keys.ENTER)
            time.sleep(1)
        return colors

    @allure.title("Check count of colors")
    def check_colors_in_field(self):
        colors = self.elements_are_present(self.locators.MULTI_COLOR_VALUE)
        lst = []
        for color in colors:
            lst.append(color.text)
        return lst

    @allure.title("Remove all colors")
    def remove_all_colors(self):
        self.element_is_visible(self.locators.REMOVE_ALL_COLORS).click()
        output = self.element_is_visible(self.locators.MULTI_COLOR).text
        return output

    @allure.title("Remove some colors")
    def remove_some_colors(self):
        all_colors = self.fill_input_multi()
        random.shuffle(all_colors)
        random_color = all_colors[0:random.randint(1, 2)]
        remove_color_name = []
        for i in self.elements_are_present(self.locators.GET_COLOR_NAME):
            if i.text in random_color:
                remove_color_name.append(i.text)
                time.sleep(1)
                self.element_is_present(self.locators.REMOVE_ONE_COLOR).click()
        return remove_color_name, all_colors

    @allure.title("Fill single color")
    def fill_single_color_field(self):
        colors = random.sample(next(generator_color()).color_name, k=1)
        for color in colors:
            input_single = self.element_is_clicable(self.locators.SINGLE_COLOR_INPUT)
            input_single.send_keys(color)
            input_single.send_keys(Keys.ENTER)
        return colors[0]

    def check_single_color_field(self):
        color = self.element_is_visible(self.locators.SINGLE_COLOR_NAME)
        return color.text
