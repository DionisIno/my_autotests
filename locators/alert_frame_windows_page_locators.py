from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, "button[id='messageWindowButton']")
    SAMPLE_PAGE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    NEW_WINDOW_PAGE = (By.TAG_NAME, "body")


class AlertsPageLocators:
    BUTTON_ALERT = (By.CSS_SELECTOR, "button[id='alertButton']")
    BUTTON_ALERT_AFTER_5_SECOND = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BOX = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_BOX_TEXT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMPT_TEXT = (By.CSS_SELECTOR, "span[id='promptResult']")


class FramePageLocators:
    BIG_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SMALL_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    FRAME_PAGE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFramePageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    FIRST_FRAME_TEXT = (By.CSS_SELECTOR, "body")
    SECOND_FRAME = (By.XPATH, "//iframe[contains(@srcdoc, 'Child Iframe')]")
    SECOND_FRAME_TEXT = (By.CSS_SELECTOR, "p")


class ModalPageLocators:
    SMALL_MODAL = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    MODAL_HEADER = (By.CSS_SELECTOR, "div[class='modal-title h4']")
    MODAL_TITLE = (By.CSS_SELECTOR, "div[class='modal-body']")
    MODAL_CLOSE = (By.CSS_SELECTOR, "button[class='close']")
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")

    BIG_MODAL = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
