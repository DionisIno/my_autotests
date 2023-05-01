import time

from selenium.common import ElementClickInterceptedException

from draft.draft import *
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
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
            input_multi.send_keys(Keys.ENTER)
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


class DataPickerPage(BasePage):
    locators = DatePickerPageLocators

    @allure.title("Get month number by name")
    def get_month_number_by_name(self, item):
        months_dict = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        return months_dict[item]

    @allure.title("Get select date")
    def get_select_date(self):
        info = next(generator_date())
        year = info.year
        month = info.month
        day = info.day
        input_date = self.element_is_visible(self.locators.SELECT_DATE)
        input_date.click()
        self.set_date_by_value(self.locators.SELECT_DATE_YEAR, year)
        self.set_date_by_value(self.locators.SELECT_DATE_MONTH, month)
        self.set_date_from_list(self.locators.SELECT_DATE_DAYS, day)
        selected_date = f"{str(self.get_month_number_by_name(month)).zfill(2)}/{day}/{year}"
        date_after = input_date.get_attribute('value')
        return selected_date, date_after

    @allure.title("Set year and month")
    def set_date_by_value(self, item, value):
        select = Select(self.element_is_clicable(item))
        select.select_by_visible_text(value)

    @allure.title("Set day from list")
    def set_date_from_list(self, item, value):
        select = self.elements_are_present(item)
        for i in select:
            if i.text == value:
                time.sleep(1)
                i.click()
                break

    @allure.title("Set date with go to element")
    def set_date_with_go_to_element(self, item, value):
        select = self.elements_are_present(item)
        for i in select:
            if i.text == value:
                time.sleep(1)
                self.go_to_element(i)
                time.sleep(1)
                i.click()
                break

    @allure.title("Get year")
    def get_year(self):
        self.element_is_clicable(self.locators.DATE_AND_TIME_YEAR).click()
        time.sleep(1)
        lst = random.choice(self.elements_are_present(self.locators.DATE_AND_TIME_YEAR_LIST)[1:-1])
        self.go_to_element(lst)
        year = lst.text
        lst.click()
        return year

    @allure.title("Get month")
    def get_month(self):
        self.element_is_clicable(self.locators.DATE_AND_TIME_MONTH).click()
        time.sleep(1)
        lst = random.choice(self.elements_are_present(self.locators.DATE_AND_TIME_MONTH_LIST))
        self.go_to_element(lst)
        month = lst.text
        lst.click()
        return month

    @allure.title("Get time")
    def get_time(self):
        info = next(generator_date())
        time_info = info.time
        self.set_date_with_go_to_element(self.locators.DATE_AND_TIME_TIME_LIST, time_info)
        return time_info

    @allure.title("Get date and time")
    def get_date_and_time(self):
        info = next(generator_date())
        day = info.day
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        input_date.click()
        year = self.get_year()
        month = self.get_month()
        self.set_date_from_list(self.locators.SELECT_DATE_DAYS, day)
        time_date = self.get_time()
        time.sleep(1)
        input_date = f"{month} {day}, {year} {convert_to_12h_format(time_date)}"
        return input_date

    @allure.title("Get date after changes")
    def get_date_after_changes(self):
        self.go_to_element(self.element_is_present(self.locators.DATE_AND_TIME_INPUT))
        time.sleep(1)
        date_after = self.element_is_present(self.locators.DATE_AND_TIME_INPUT).get_attribute('value')
        return date_after


class SliderPage(BasePage):
    locators = SliderPageLocators

    @allure.title("Get slider value")
    def slider(self):
        value_before = self.element_is_visible(self.locators.SLIDER_INPUT).get_attribute('value')
        slider = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_by_offset(slider, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_INPUT).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators

    @allure.title("Get progress bar value")
    def progress_bar(self):
        value_before = self.element_is_present(self.locators.VALUE_PROGRESS_BAR).get_attribute('aria-valuenow')
        button = self.element_is_visible(self.locators.BUTTON_PROGRESS_BAR)
        button.click()
        time.sleep(random.randint(3, 10))
        button.click()
        value_after = self.element_is_present(self.locators.VALUE_PROGRESS_BAR).get_attribute('aria-valuenow')
        print(value_after)
        print(value_before)
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators

    def tabs_page(self, value):
        tabs = {'What':
                    {'title': self.locators.TABS_WHAT,
                     'content': self.locators.TABS_WHAT_CONTENT},
                'Origin':
                    {'title': self.locators.TABS_ORIGIN,
                     'content': self.locators.TABS_ORIGIN_CONTENT},
                'Use':
                    {'title': self.locators.TABS_USE,
                     'content': self.locators.TABS_USE_CONTENT},
                'More':
                    {'title': self.locators.TABS_MORE,
                     'content': self.locators.TABS_MORE_CONTENT}
                }
        button = self.element_is_visible(tabs[value]['title'])
        try:
            button.click()
            content = self.element_is_visible(tabs[value]['content'])
        except ElementClickInterceptedException:
            return f"Button {button.text} is not pressed", "Content is not exist",
        return button.text, content.text


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators

    @allure.title("Get info after hover on the element")
    def get_info_after_hover(self, value):
        elem = self.element_is_present(self.locators.ALL_LOCATORS[value])
        self.action_move_to_element(elem)
        time.sleep(1)
        text = self.element_is_present(self.locators.AFTER_HOVER_TEXT)
        return text.text
