import os
import random
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from draft.draft import return_correct_form
from locators.form_page_locators import FormPageLocators
from generator.generator import get_person, generated_subject, generated_file, generated_city
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators

    @allure.title("Fill main fields in the form")
    def fill_main_fields(self):
        info = next(get_person())
        first_name = info.first_name
        last_name = info.last_name
        email = info.email
        mobile = info.mobile[:10]
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.PHOHE_NUMBER).send_keys(mobile)
        gender_click = self.element_is_visible(self.locators.GENDER)
        gender = gender_click.text
        gender_click.click()
        return first_name, last_name, email, gender, mobile

    @allure.title("Fill date n the form")
    def fill_date_form(self):
        calender = self.element_is_visible(self.locators.BIRTH_DAY)
        calender.click()
        with allure.step("Select year"):
            self.element_is_visible(self.locators.YEARS_CHANGE).click()
            year_change = self.element_is_visible(self.locators.YEARS)
            year = year_change.text
            year_change.click()
        with allure.step("Select month"):
            self.element_is_visible(self.locators.MONTHS_CHANGE).click()
            month_change = self.element_is_visible(self.locators.MONTHS)
            month = month_change.text
            month_change.click()
        with allure.step("Select day"):
            week = self.driver.find_elements(By.CSS_SELECTOR, ".react-datepicker__day")
            random_day = random.choice(week)
            day = random_day.text
            random_day.click()
        return day, month, year

    @allure.title("Fill hobbies, subject and upload file")
    def fill_other_field(self):
        subject_list = generated_subject()
        for item in subject_list:
            self.element_is_visible(self.locators.SUBJECT).send_keys(item)
            self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        hobby = self.element_is_visible(self.locators.HOBBIES)
        hobby.click()
        file_name, path = generated_file()
        self.element_is_visible(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        return subject_list, hobby.text, file_name.split('\\')[-1]

    @allure.title("Fill address")
    def fill_address(self):
        info = next(get_person())
        current_address = info.current_address
        state, city = generated_city()
        new_city = city[random.randint(0, len(city)-1)]
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(state)
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(new_city)
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).send_keys(Keys.RETURN)
        return current_address, state, new_city

    @allure.step('get form result')
    def form_result(self):
        result_list = self.elements_are_visible(self.locators.ALL_TABLE)
        data = ""
        for item in result_list:
            self.go_to_element(item)
            data += item.text
        print(data)
        correct_result = return_correct_form(data)
        return correct_result
