import allure
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
            print(text)
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

    @allure.feature("Test Date picker Page")
    class TestDataPicker:
        @allure.title("Check select date")
        def test_check_select_date(self, driver):
            date_page = DataPickerPage(driver, "https://demoqa.com/date-picker")
            date_page.open()
            input_date, date_after = date_page.get_select_date()
            assert input_date == date_after, "Date has not changed"

        @allure.title("Check date and time page")
        def test_check_date_and_time(self, driver):
            date_page = DataPickerPage(driver, "https://demoqa.com/date-picker")
            date_page.open()
            date_changes = date_page.get_date_and_time()
            date_after = date_page.get_date_after_changes()
            print(date_changes)
            print(date_after)
            assert date_after == date_changes, "Date has not changed"

    @allure.feature("Test Slider page")
    class TestSlider:
        @allure.title("Check slider")
        def test_check_slider(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            value_before, value_after = slider_page.slider()
            assert value_before != value_after, "Slider works incorrect"

    @allure.feature("Test Progress Bar Page")
    class TestProgressBar:

        @allure.title("Check progress bar")
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar.open()
            value_before, value_after = progress_bar.progress_bar()
            assert value_before != value_after, "Progress Bar works incorrect"

    @allure.feature('Test Tabs Page')
    class TestTabsPage:
        lst = ["What", "Origin", "Use", "More"]

        @pytest.mark.parametrize('value', lst)
        @allure.title('Check switched tabs')
        def test_tabs_page(self, driver, value):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            button, content = tabs_page.tabs_page(value)
            assert value == button and len(content) != 0, f"The tab '{button}' was not pressed or text is missing"

    @allure.feature("Test Tool Tips Page")
    class TestToolTips:
        lst = [("button", 'You hovered over the Button'),
               ("field", 'You hovered over the text field'),
               ("text", 'You hovered over the Contrary'),
               ("number", 'You hovered over the 1.10.32')
               ]

        @pytest.mark.parametrize("item", lst)
        @allure.title("Check tool tips page")
        def test_tool_tips(self, driver, item):
            tool_tips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tool_tips_page.open()
            value, input_text = item
            text = tool_tips_page.get_info_after_hover(value)
            assert text == input_text, "'Hover missing or incorrect content'"
