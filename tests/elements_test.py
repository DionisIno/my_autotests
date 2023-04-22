import time
import pytest

from pages.elements_page import *


@allure.suite("Main test")
class TestElements:
    @allure.feature("Testing Text Box")
    class TestTextBox:
        @allure.title("Get text box values")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_field()
            out_name, out_email, out_current_address, out_permanent_address = text_box_page.check_filled_field()
            assert full_name == out_name
            assert email == out_email
            assert current_address == out_current_address
            assert permanent_address == out_permanent_address

        @allure.title("Get placeholder value")
        def test_get_value_placeholder(self, driver):
            text_placeholder = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_placeholder.open()
            full_name = text_placeholder.get_placeholder()
            for item in full_name:
                assert len(item) != 0, "Can not find placeholder value"

    @allure.feature("Test Check Box")
    class TestCheckBox:
        @allure.title("Test check box")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random()
            input_checkbox = check_box_page.get_checked_box()
            output_checkbox = check_box_page.get_output_result()
            assert input_checkbox == output_checkbox

    @allure.feature("Test Radio Button")
    class TestRadioButton:
        radio_buttons_list = ['yes', 'impressive', 'no']
        random.shuffle(radio_buttons_list)

        @pytest.mark.parametrize('item', radio_buttons_list)
        @allure.title("Check radio button")
        def test_radio_button(self, driver, item):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            with allure.step("check click on the buttons"):
                radio_button_page.click_on_the_radio_button(item)
                output_field = radio_button_page.get_output_result()
                assert output_field == item.title(), f"{item.title()} radiobutton is not clickable"

    @allure.feature("Check webtable")
    class TestWebTable:
        @allure.title("add new person in table")
        def test_add_person_in_the_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            for i in range(random.randint(1, 10)):
                new_person = web_table_page.add_new_person()
                result = web_table_page.check_new_added_person()
                assert new_person in result, "A new person is not in the table"

        @allure.title("check people in the table")
        def test_check_people_in_the_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_people(key_word)
            table_result = web_table_page.check_people()
            assert key_word in table_result, "The person was not found in the table"

        @allure.title("Checking to update the person info in the table")
        def test_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_people(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_people()
            assert age in row, "The person card has not been changed"

        @allure.title("Delete person from table")
        def test_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_people(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found", "The person card has not been deleted"

        @allure.title("Check the change in the number of rows in the table")
        def test_change_rows(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = web_table_page.select_up_to_rows()
            print(count)
            # assert count == [5, 10, 20, 25, 50, 100], 'The number of rows in the table has not been changed or has changed incorrectly'

    @allure.feature("Buttons Page")
    class TestButtonsPage:
        button = ["double", "right", "click"]

        @pytest.mark.parametrize("item", button)
        @allure.title('Checking clicks of different types')
        def test_different_click_on_the_button(self, driver, item):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            button = button_page.click_on_different_button(item)
            assert button in ["You have done a double click", "You have done a right click",
                              "You have done a dynamic click"], f"The button was not pressed"

        @allure.title('Checking clicks of different types version 2')
        def test_different_click_on_the_button_v2(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            double = button_page.click_on_different_button("double")
            right = button_page.click_on_different_button("right")
            click = button_page.click_on_different_button("click")
            assert double == "You have done a double click", "The double click button was not pressed"
            assert right == "You have done a right click", "The right click button was not pressed"
            assert click == "You have done a dynamic click", "The dynamic click button was not pressed"

    @allure.feature("Links Page")
    class TestLinksPage:
        @allure.title("Check simple link")
        def test_check_simple_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.click_on_simple_link()
            assert href_link == current_url, "The link is broken or url is incorrect"

        @allure.title("Check simple link")
        def test_check_simple_link_v2(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.click_on_simple_link_v2()
            assert href_link == current_url, "The link is broken or url is incorrect"
