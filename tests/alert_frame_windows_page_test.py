import pytest

from pages.alert_frame_windows_page import *


@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindow:
    @allure.feature('Browser Windows')
    class TestBrowserWindow:
        @allure.title("Checking a text in the button")
        def test_check_button_text(self, driver):
            check_text = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            check_text.open()
            text = check_text.check_button_text()
            assert text == "New Tab", "The button text is not correct"

        @allure.title("Checking a text on the tab")
        def test_check_new_tab_text(self, driver):
            check_text = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            check_text.open()
            text = check_text.check_new_tab_text()
            assert text == "This is a sample page", "Incorrect button text"

        @allure.title("Checking link on the tab")
        def test_check_new_tab_link(self, driver):
            check_text = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            check_text.open()
            text = check_text.check_link_in_the_new_tab()
            assert text == "https://demoqa.com/sample", "Incorrect link"

        @allure.title("Checking a status code in the new tab")
        def test_check_status_code_in_the_new_tab(self, driver):
            check_text = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            check_text.open()
            link = check_text.check_link_in_the_new_tab()
            status_code = check_text.check_status_code(link)
            assert status_code == 200, f"Status code is {status_code}"

        @allure.title("Checking a text in the new window button")
        def test_check_new_window_button_text(self, driver):
            check_text = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            check_text.open()
            text = check_text.check_new_window_button_text()
            assert text == "New Window", "Incorrect button text"

        @allure.title("Checking a text on the new window")
        def test_check_new_window_text(self, driver):
            check_text = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            check_text.open()
            text = check_text.check_new_window_text()
            assert text == "This is a sample page", "The text in the bew tab is incorrect"

        @allure.title("Checking a link on the new window")
        def test_check_new_window_link(self, driver):
            check_text = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            check_text.open()
            text = check_text.check_link_in_the_new_window()
            assert text == "https://demoqa.com/sample", "Incorrect link"

        @allure.title("Checking a status code in the new window")
        def test_check_status_code_in_the_new_window(self, driver):
            check_text = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            check_text.open()
            link = check_text.check_link_in_the_new_window()
            status_code = check_text.check_status_code(link)
            assert status_code == 200, f"Status code is {status_code}"

        @allure.title("Checking new window message button text")
        def test_check_new_window_message_text(self, driver):
            check_text = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            check_text.open()
            text = check_text.check_new_window_message_button_text()
            assert text == "New Window Message", "Incorrect button text"

        # @allure.title("Problem getting text from new tab")
        # def test_check_text_new_message_window(self, driver):
        #     check_text = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
        #     check_text.open()
        #     text = check_text.check_message_in_the_new_window()
        #     print(text)

    @allure.feature("Alerts")
    class TestAlerts:
        lst = ["accept", "dismiss"]

        @allure.title("Check simple alert")
        def test_simple_alert(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text = alert_page.simple_alert()
            assert text == "You clicked a button", "You don't click a button"

        @allure.title("Check appear alert after 5 second")
        def test_alert_after_five_second(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text = alert_page.alert_after_five_second()
            assert text == "This alert appeared after 5 seconds", "Alert don't appear"

        @pytest.mark.parametrize('item', lst)
        @allure.title("Check complex alert(accept or dismiss)")
        def test_complex_alert(self, driver, item):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text, response = alert_page.complex_alert(item)
            assert text in response, "Wrong response"

        @allure.title("Check prompt")
        def test_prompt(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text, response = alert_page.prompt()
            assert text in response, "Wrong text"

    @allure.feature("Test frame")
    class TestFrame:
        size = ["small", "big"]

        @pytest.mark.parametrize("item", size)
        @allure.title("Check frame")
        def test_all_frame(self, driver, item):
            frame_page = FramePage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result = frame_page.get_frame_info(item)
            assert result == ['500px', '350px', 'This is a sample page'] or result == ['100px', '100px',
                                                                                       'This is a sample page'], "The frame does not exist"

    @allure.feature("Test nested frame")
    class TestNestedFrames:
        @allure.title("Check the page with nested frames")
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frame_page.open()
            text_first_frame, text_second_frame = nested_frame_page.nested_frame_page()
            assert text_first_frame == "Parent frame", "Parent frame doesn't exist"
            assert text_second_frame == "Child Iframe", "Child frame doesn't exist"

    @allure.feature("Test modal pages")
    class TestModalPages:
        close_modal = ["esc", "button", "cross"]
        size_button = ["small", "big"]

        @pytest.mark.parametrize('item', size_button)
        @allure.title("Check modal button text")
        def test_get_modal_button_text(self, driver, item):
            modal_page = ModalPage(driver, "https://demoqa.com/modal-dialogs")
            modal_page.open()
            text, check = modal_page.get_modal_button_text(item)
            assert text == check, "The button hasn't a text"

        @allure.title("Check if small modal have content")
        def test_get_content_small_modal(self, driver):
            modal_page = ModalPage(driver, "https://demoqa.com/modal-dialogs")
            modal_page.open()
            header, title = modal_page.get_content_from_small_modal()
            assert header == "Small Modal", "Modal hasn't header text"
            assert title == "This is a small modal. It has very less content", "Modal hasn't title text"

        @pytest.mark.parametrize('item', close_modal)
        @allure.title("Check close modal with different ways")
        def test_check_close_modal_different_ways(self, driver, item):
            modal_page = ModalPage(driver, "https://demoqa.com/modal-dialogs")
            modal_page.open()
            button = modal_page.check_close_modal_different_ways(item)
            assert item in button, f"Didn't click on the {item}"

        @allure.title("Check if big modal have content")
        def test_get_content_large_modal(self, driver):
            modal_page = ModalPage(driver, "https://demoqa.com/modal-dialogs")
            modal_page.open()
            header, title = modal_page.get_content_from_large_modal()
            assert header == "Large Modal", "Modal hasn't header text"
            assert len(title) > 0, "Modal hasn't title text"

        @pytest.mark.parametrize('item', close_modal)
        @allure.title("Check close modal with different ways")
        def test_check_close_large_modal_different_ways(self, driver, item):
            modal_page = ModalPage(driver, "https://demoqa.com/modal-dialogs")
            modal_page.open()
            button = modal_page.check_close_large_modal_different_ways(item)
            assert item in button, f"Didn't click on the {item}"
