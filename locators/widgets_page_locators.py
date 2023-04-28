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
    MULTI_COLOR = (By.CSS_SELECTOR, "div[id='autoCompleteMultipleContainer']")
    ONE_COLOR= (By.CSS_SELECTOR, "div[id='autoCompleteSingleContainer']")
