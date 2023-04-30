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


class DatePicker:
    SELECT_DATE = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
