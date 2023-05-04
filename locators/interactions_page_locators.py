from selenium.webdriver.common.by import By


class SortablePageLocators:
    ALL_LOCATORS = {
        "list": [(By.CSS_SELECTOR, "a[id='demo-tab-list']"),
                 (By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class^='list-group-item']")],
        "grid": [(By.CSS_SELECTOR, "a[id='demo-tab-grid']"),
                 (By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] div[class^='list-group-item']")]
    }


class SelectablePageLocators:
    ALL_LOCATORS = {
        "list": [(By.CSS_SELECTOR, "a[id='demo-tab-list']"),
                 (By.CSS_SELECTOR, "li[class='mt-2 list-group-item list-group-item-action']"),
                 (By.CSS_SELECTOR, "li[class='mt-2 list-group-item active list-group-item-action']")],
        "grid": [(By.CSS_SELECTOR, "a[id='demo-tab-grid']"),
                 (By.CSS_SELECTOR, "li[class='list-group-item list-group-item-action']"),
                 (By.CSS_SELECTOR, "li[class='list-group-item active list-group-item-action']")]
    }


class ResizablePageLocators:
    RESIZABLE_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction'] span")
    RESIZABLE = (By.CSS_SELECTOR, "div[id='resizable']")
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, "div[id='resizable'] span")


class DroppablePageLocators:
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-simple']")
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, "div[id='draggable']")
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, "div[id='draggable']~#droppable")
    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-accept']")
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, "div[id='acceptDropContainer'] div[id='droppable']")
    ACCEPT_AND_NOT_ACCEPT = {"acceptable": (By.CSS_SELECTOR, "div[id='acceptable']"),
                             "not_acceptable": (By.CSS_SELECTOR, "div[id='notAcceptable']")
                             }
    # Prevent
    PREVENT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-preventPropogation']")
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, "div[id='dragBox']")
    NOT_GREEDY_DROP_BOX = (By.CSS_SELECTOR, "div[id='notGreedyDropBox'] div[id='notGreedyInnerDropBox']")
    NOT_GREEDY_INNER_BOX_TEXT = (By.CSS_SELECTOR, "div[id='notGreedyDropBox'] > p")
    GREEDY_DROP_BOX = (By.CSS_SELECTOR, "div[id='greedyDropBox'] div[id='greedyDropBoxInner']")
    GREEDY_INNER_BOX_TEXT = (By.CSS_SELECTOR, "div[id='greedyDropBox'] > p")
    # Revert
    REVERT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-revertable']")
    WILL_REVERT = (By.CSS_SELECTOR, "div[id='revertable']")
    NOT_REVERT = (By.CSS_SELECTOR, "div[id='notRevertable']")
    DROP_HERE_REVERT = (By.CSS_SELECTOR, "div[id='revertableDropContainer'] div[id='droppable']")


class DragablePageLocators:
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-simple']")
    SIMPLE_DRAG = (By.CSS_SELECTOR, "div[id='dragBox']")
    # Axis Restricted
    AXIS_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-axisRestriction']")
    ONLY_X = (By.CSS_SELECTOR, "div[id='restrictedX']")
    ONLY_Y = (By.CSS_SELECTOR, "div[id='restrictedY']")
