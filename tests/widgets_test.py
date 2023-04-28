import random
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
