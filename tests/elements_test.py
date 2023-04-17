import time
import allure
from my_autotests.pages.elements_page import *

@allure.suite("Main test")
class TestElements:
    @allure.feature("Test Text Box")
    class TestTextBox:
        @allure.title("Test text box")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_field()
            out_name, out_email, out_current_address, out_permanent_address = text_box_page.check_filled_field()
            time.sleep(5)
            assert full_name == out_name
            assert email == out_email
            assert current_address == out_current_address
            assert permanent_address == out_permanent_address

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
            time.sleep(5)
            print(input_checkbox)
            print(output_checkbox)
            assert input_checkbox == output_checkbox

    @allure.feature("Test Radio Button")
    class TestRadioButton:

        @allure.title("Check radio button")
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            with allure.step("check click on the buttons"):
                radio_buttons_list = ['yes', 'impressive', 'no']
                # random.shuffle(radio_buttons_list)
                # for i in radio_buttons_list:
                #     radio_button = radio_button_page.click_on_the_radio_button(i)
                #     output = radio_button_page.get_output_result()
                #     print(output)
                radio_button_page.click_on_the_radio_button('yes')
                output_yes = radio_button_page.get_output_result()
                radio_button_page.click_on_the_radio_button('impressive')
                output_impressive = radio_button_page.get_output_result()
                radio_button_page.click_on_the_radio_button('no')
                output_no = radio_button_page.get_output_result()
            assert output_yes == "Yes", "Yes radiobutton is not clickable"
            assert output_impressive == "Impressive", "Impressive radiobutton is not clickable"
            assert output_no == "No", "No radiobutton is not clickable"
    @allure.feature("Check webtable")
    class TestWebTable:
        @allure.title("add new person in table")
        def test_add_person_in_the_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            # count = random.randint(1, 100)
            new_person = web_table_page.add_new_person()
            result = web_table_page.check_new_added_person()
            assert new_person in result

        @allure.title("check people in the table")
        def test_check_people_in_the_table(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_people(key_word)
            table_result = web_table_page.check_people()
            time.sleep(15)
            assert key_word in table_result