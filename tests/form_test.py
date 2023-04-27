import time

import pytest
from pages.form_page import *


@allure.suite("Practice Form")
class TestAllForm:
    @allure.feature("Testing Form")
    class TestForm:
        @allure.title("Fill form field")
        def test_fill_form_field(self, driver):
            form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
            form_page.open()
            form_page.remove_footer()
            first_name, last_name, email, gender, mobile = form_page.fill_main_fields()
            day, month, year = form_page.fill_date_form()
            subject_list, hobby, file_name = form_page.fill_other_field()
            address, state, city = form_page.fill_address()
            input_data = [[first_name, last_name], [email], [gender], [mobile], [day.zfill(2), month, year],
                          subject_list, [hobby], [file_name], [address], [state, city]]
            output_data = form_page.form_result()
            result = (input_data == output_data)
            assert result == True, "Incorrect form filling or test error"
