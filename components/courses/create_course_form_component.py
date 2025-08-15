from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.input import Input
from elements.text_area import TextArea
import allure


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title_input = Input(page, 'create-course-form-title-input', 'Title')
        self.create_course_estimated_time_input = (
            Input(page, 'create-course-form-estimated-time-input', 'Estimated time')
        )
        self.create_course_description_textarea = (
            TextArea(page, 'create-course-form-description-input', 'Description')
        )
        self.create_course_max_score_input = Input(page, 'create-course-form-max-score-input', 'Max score')
        self.create_course_min_score_input = Input(page, 'create-course-form-min-score-input', 'Min score')

    @allure.step('Заполнение формы создания курса')
    def fill_create_course_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.create_course_title_input.fill(title)
        self.create_course_title_input.check_value(title)

        self.create_course_estimated_time_input.fill(estimated_time)
        self.create_course_estimated_time_input.check_value(estimated_time)

        self.create_course_description_textarea.fill(description)
        self.create_course_description_textarea.check_value(description)

        self.create_course_max_score_input.fill(max_score)
        self.create_course_max_score_input.check_value(max_score)

        self.create_course_min_score_input.fill(min_score)
        self.create_course_min_score_input.check_value(min_score)

    @allure.step('Проверка видимости формы создания курса')
    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.create_course_title_input.check_visible()
        self.create_course_title_input.check_value(title)

        self.create_course_estimated_time_input.check_visible()
        self.create_course_estimated_time_input.check_value(estimated_time)

        self.create_course_description_textarea.check_visible()
        self.create_course_description_textarea.check_value(description)

        self.create_course_max_score_input.check_visible()
        self.create_course_max_score_input.check_value(max_score)

        self.create_course_min_score_input.check_visible()
        self.create_course_min_score_input.check_value(min_score)