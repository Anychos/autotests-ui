from playwright.sync_api import Page
import allure
from components.base_component import BaseComponent, expect
from elements.button import Button
from elements.input import Input
from elements.text import Text


class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.delete_button = Button(page, "create-course-exercise-{index}-box-toolbar-delete-exercise-button", "Delete exercise")
        self.subtitle = Text(page, "create-course-exercise-{index}-box-toolbar-subtitle-text", "Exercise subtitle")
        self.title_input = Input(page, "create-course-exercise-form-title-{index}-input", "Title")
        self.description_input = Input(page, "create-course-exercise-form-description-{index}-input", "Description")

    def click_delete_button(self, index: int):
        self.delete_button.click(index=index)

    @allure.step('Проверка видимости формы создания упражнения с индексом {index}')
    def check_visible(self, index: int, title: str, description: str):
        self.subtitle.check_visible(index=index)
        self.subtitle.check_text(f"#{index + 1} Exercise", index=index)

        self.title_input.check_visible(index=index)
        self.title_input.check_value(title, index=index)

        self.description_input.check_visible(index=index)
        self.description_input.check_value(description, index=index)

    @allure.step('Заполнение формы создания упражнения с индексом {index}')
    def fill(self, index: int, title: str, description: str):
        self.title_input.fill(title, index=index)
        self.title_input.check_value(title, index=index)

        self.description_input.fill(description, index=index)
        self.description_input.check_value(description, index=index)
