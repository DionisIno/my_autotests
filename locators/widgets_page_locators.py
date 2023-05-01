from selenium.webdriver.common.by import By


class AccordianPageLocators:
    WHAT = (By.CSS_SELECTOR, "div[id='section1Heading']")
    WHAT_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content']")
    WHAT_CONTENT_CHECK = (By.CSS_SELECTOR, "div[id='section1Heading']~div")
    WHERE = (By.CSS_SELECTOR, "div[id='section2Heading']")
    WHERE_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content']")
    WHERE_CONTENT_CHECK = (By.CSS_SELECTOR, "div[id='section2Heading']~div")
    WHY = (By.CSS_SELECTOR, "div[id='section3Heading']")
    WHY_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content']")
    WHY_CONTENT_CHECK = (By.CSS_SELECTOR, "div[id='section3Heading']~div")


class AutoCompletePageLocators:
    MULTI_COLOR = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTI_COLOR_VALUE = (By.CSS_SELECTOR, "div[class$='auto-complete__multi-value']")
    REMOVE_ALL_COLORS = (By.XPATH, "//div[contains(@class, 'auto-complete__clear-indicator')]")
    GET_COLOR_NAME = (By.CSS_SELECTOR, "div[class$='auto-complete__multi-value__label']")
    REMOVE_ONE_COLOR = (By.CSS_SELECTOR, "div[class$='auto-complete__multi-value__remove']")

    # SINGLE_COLOR_NAME = (By.CSS_SELECTOR, "div[id='autoCompleteSingleContainer']")
    SINGLE_COLOR_NAME = (By.CSS_SELECTOR, "div[class^='auto-complete__single-value']")
    SINGLE_COLOR_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")


class DatePickerPageLocators:
    SELECT_DATE = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    SELECT_DATE_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    SELECT_DATE_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    SELECT_DATE_DAYS = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")


class SliderPageLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, "input[class^='range-slider']")
    SLIDER_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")


class ProgressBarPageLocators:
    BUTTON_PROGRESS_BAR = (By.CSS_SELECTOR, "button[id='startStopButton']")
    VALUE_PROGRESS_BAR = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")


class TabsPageLocators:
    TABS_WHAT = (By.CSS_SELECTOR, "a[id='demo-tab-what']")
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-what']")
    TABS_ORIGIN = (By.CSS_SELECTOR, "a[id='demo-tab-origin']")
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-origin']")
    TABS_USE = (By.CSS_SELECTOR, "a[id='demo-tab-use']")
    TABS_USE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-use']")
    TABS_MORE = (By.CSS_SELECTOR, "a[id='demo-tab-more']")
    TABS_MORE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-more']")


class ToolTipsPageLocators:
    ALL_LOCATORS = {"button": (By.CSS_SELECTOR, "button[id='toolTipButton']"),
                    "field": (By.CSS_SELECTOR, "input[id='toolTipTextField']"),
                    "text": (By.XPATH, "//div[@id='texToolTopContainer']/a[contains(text(), 'Contrary')]"),
                    "number": (By.XPATH, "//div[@id='texToolTopContainer']/a[contains(text(), '1.10.32')]")
                    }
    AFTER_HOVER_TEXT = (By.CSS_SELECTOR, "div[class='tooltip-inner']")
