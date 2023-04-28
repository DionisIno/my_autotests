import random
import time
from selenium.webdriver import Keys
import requests

from locators.alert_frame_windows_page_locators import *
from pages.base_page import *


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators

    @allure.title("Get button text")
    def check_button_text(self):
        text = self.element_is_visible(self.locators.NEW_TAB)
        return text.text

    @allure.title("Get new tab text")
    def check_new_tab_text(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.element_is_visible(self.locators.SAMPLE_PAGE)
        return text.text

    @allure.title("Get link in the new tab")
    def check_link_in_the_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.driver.current_url
        return text

    @allure.title("Get status code")
    def check_status_code(self, link):
        response = requests.get(link)
        return response.status_code

    @allure.title("Get new window button text")
    def check_new_window_button_text(self):
        text = self.element_is_visible(self.locators.NEW_WINDOW)
        return text.text

    @allure.title("Get new window text")
    def check_new_window_text(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.element_is_visible(self.locators.SAMPLE_PAGE)
        return text.text

    @allure.title("Get link in the new window")
    def check_link_in_the_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.driver.current_url
        return text

    @allure.title("Get new window message button text")
    def check_new_window_message_button_text(self):
        text = self.element_is_visible(self.locators.NEW_WINDOW_MESSAGE)
        return text.text

    # @allure.title("Problem getting text from new tab")
    # def check_message_in_the_new_window(self):
    #     main_window_handle = self.driver.current_window_handle
    #     print(f"\nOriginal window: {main_window_handle}")
    #     print(f"Count of window before: {len(self.driver.window_handles)}")
    #     self.element_is_visible(self.locators.NEW_WINDOW_MESSAGE).click()
    #     print(f"Count od window after: {len(self.driver.window_handles)}")
    #     print(f"All count window handles: {self.driver.window_handles}")
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     print(f"Window handle after switch: {self.driver.current_window_handle}")
    #     print(f"Current url: {self.driver.current_url}")
    #     text = self.element_is_present(self.locators.NEW_WINDOW_PAGE)
    #     return text.text


class AlertPage(BasePage):
    locators = AlertsPageLocators

    @allure.title("Alert after click on the button")
    def simple_alert(self):
        self.element_is_visible(self.locators.BUTTON_ALERT).click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    @allure.title("Alert after click on the button after 5 second")
    def alert_after_five_second(self):
        self.element_is_visible(self.locators.BUTTON_ALERT_AFTER_5_SECOND).click()
        time.sleep(5)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    @allure.title("Get info from complex alert")
    def complex_alert(self, item):
        self.element_is_visible(self.locators.CONFIRM_BOX).click()
        alert = self.driver.switch_to.alert
        if item == "accept":
            alert.accept()
            text = "Ok"
        else:
            alert.dismiss()
            text = "Cancel"
        response = self.element_is_present(self.locators.CONFIRM_BOX_TEXT).text
        return text, response

    @allure.title("Get info from prompt")
    def prompt(self):
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.PROMPT).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()
        response = self.element_is_present(self.locators.PROMPT_TEXT).text
        return text, response


class FramePage(BasePage):
    locators = FramePageLocators

    @allure.title("Get info from frame pages")
    def get_frame_info(self, item):
        if item == "small":
            frame = self.element_is_present(self.locators.SMALL_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_PAGE).text
            self.driver.switch_to.default_content()
            return [width, height, text]
        if item == "big":
            frame = self.element_is_present(self.locators.BIG_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAME_PAGE).text
            self.driver.switch_to.default_content()
            return [width, height, text]


class NestedFramesPage(BasePage):
    locators = NestedFramePageLocators

    @allure.title("Check wondow with nested frames")
    def nested_frame_page(self):
        first_frame = self.element_is_present(self.locators.FIRST_FRAME)
        self.driver.switch_to.frame(first_frame)
        text_first_frame = self.element_is_present(self.locators.FIRST_FRAME_TEXT).text
        second_frame = self.element_is_present(self.locators.SECOND_FRAME)
        self.driver.switch_to.frame(second_frame)
        text_second_frame = self.element_is_present(self.locators.SECOND_FRAME_TEXT).text
        return text_first_frame, text_second_frame


class ModalPage(BasePage):
    locators = ModalPageLocators

    @allure.title('Get small button text')
    def get_modal_button_text(self, item):
        if item == "small":
            text = self.element_is_visible(self.locators.SMALL_MODAL).text
            return text, "Small modal"
        elif item == "big":
            text = self.element_is_visible(self.locators.BIG_MODAL).text
            return text, "Large modal"

    @allure.title('Get content from small modal')
    def get_content_from_small_modal(self):
        self.element_is_visible(self.locators.SMALL_MODAL).click()
        header_text = self.element_is_present(self.locators.MODAL_HEADER).text
        title_text = self.element_is_present(self.locators.MODAL_TITLE).text
        return header_text, title_text

    @allure.title('Check closing modal window')
    def check_close_modal_different_ways(self, item):
        modal = self.element_is_visible(self.locators.SMALL_MODAL)
        modal.click()
        if item == "esc":
            modal.send_keys(Keys.ESCAPE)
            return "Click on esc"
        elif item == "button":
            self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
            return "Click on button"
        elif item == "cross":
            self.element_is_visible(self.locators.MODAL_CLOSE).click()
            return "Click on cross"

    @allure.title('Get content from large modal')
    def get_content_from_large_modal(self):
        self.element_is_visible(self.locators.BIG_MODAL).click()
        header_text = self.element_is_present(self.locators.MODAL_HEADER).text
        title_text = self.element_is_present(self.locators.MODAL_TITLE).text
        return header_text, title_text

    @allure.title('Check closing large modal window')
    def check_close_large_modal_different_ways(self, item):
        modal = self.element_is_visible(self.locators.BIG_MODAL)
        modal.click()
        if item == "esc":
            modal.send_keys(Keys.ESCAPE)
            return "Click on esc"
        elif item == "button":
            self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
            return "Click on button"
        elif item == "cross":
            self.element_is_visible(self.locators.MODAL_CLOSE).click()
            return "Click on cross"
