
import pytest
from pages.widgets_page import *


@allure.suite("Test Widgets Pages")
class TestWidgets:
    @allure.feature("Test Accordian Page")
    class TestAccordian:
        title_text = ["what", "where", "why"]
        random.shuffle(title_text)

        @pytest.mark.parametrize('item', title_text)
        @allure.title("Check accordian title")
        def test_check_accordian_title(self, driver, item):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            text, check = accordian_page.check_text_in_cards(item)
            assert text == check, "Title is incorrect"

        @pytest.mark.parametrize('item', title_text)
        @allure.title("Check accordian content")
        def test_check_accordian_content(self, driver, item):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            text = accordian_page.check_content_from_card(item)
            assert len(text) > 0, "Content is empty"

    @allure.feature("Test Auto Complete Page")
    class TestAutoComplete:
        @allure.title("Check multi color names")
        def test_multi_colors(self, driver):
            color_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            color_page.open()
            input_colors = color_page.fill_input_multi()
            output_color = color_page.check_colors_in_field()
            assert input_colors == output_color, "Input data does not match output"

        @allure.title("Check remove all colors")
        def test_remove_all_color(self, driver):
            color_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            color_page.open()
            input_color = color_page.fill_input_multi()
            output_color = color_page.remove_all_colors()
            assert len(input_color) > len(output_color) == 0, "After deleting all elements, the field is not empty"

        @allure.title("Check remove some colors")
        def test_remove_some_colors(self, driver):
            color_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            color_page.open()
            deleted_colors, all_colors = color_page.remove_some_colors()
            assert set(deleted_colors).issubset(set(all_colors)) and len(deleted_colors) < len(all_colors), \
                """The removed colors aren't in the main list, or the length of the removed colors is greater than or 
                equal to the main list"""

        @allure.title("Fill single color name")
        def test_check_single_color(self, driver):
            color_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            color_page.open()
            input_color = color_page.fill_single_color_field()
            output_color = color_page.check_single_color_field()
            assert input_color == output_color, "Selected color is wrong"
