from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Open a browser')
    def open(self):
        self.driver.get(self.url)

    @allure.step('Find a visible element')
    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Find visible elements')
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Find a present element')
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Find present elements')
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Find a not visible element')
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Find clickable elements')
    def element_is_clicable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Go to specified element')
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Remove footer')
    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        # self.driver.execute_script("document.getElementsById('close-fixedban').remove();")
        # self.driver.execute_script("document.body.style.zoom = '0.5'")

    @allure.step('Remove footer v2')
    def remove_footer_v2(self):
        a = self.driver.find_element(By.TAG_NAME, 'footer')
        self.driver.execute_script("arguments[0].style.display = 'none'", a)

    @allure.step("Double click")
    def action_double_click(self, elem):
        action = ActionChains(self.driver)
        action.double_click(elem)
        action.perform()

    @allure.step("Right click")
    def action_right_click(self, elem):
        action = ActionChains(self.driver)
        action.context_click(elem)
        action.perform()
