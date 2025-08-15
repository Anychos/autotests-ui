from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.Image import Image
from elements.text import Text
import allure


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)
        self.title = Text(page, 'course-widget-title-text', 'Course title')
        self.image = Image(page, 'course-preview-image', 'Course image')
        self.max_score_text = Text(page, 'course-max-score-info-row-view-text', 'Max score')
        self.min_score_text = Text(page, 'course-min-score-info-row-view-text', 'Min score')
        self.estimated_time_text = Text(page, 'course-estimated-time-info-row-view-text', 'Estimated time')

    @allure.step('Проверка видимости данных созданного курса с индексом {index}')
    def check_visible(self, index: int, title: str, max_score: str, min_score: str, estimated_time: str):
        self.image.check_visible(nth=index)

        self.title.check_visible(nth=index)
        self.title.check_text(title, nth=index)

        self.max_score_text.check_visible(nth=index)
        self.max_score_text.check_text(f"Max score: {max_score}", nth=index)

        self.min_score_text.check_visible(nth=index)
        self.min_score_text.check_text(f"Min score: {min_score}", nth=index)

        self.estimated_time_text.check_visible(nth=index)
        self.estimated_time_text.check_text(
            f"Estimated time: {estimated_time}", nth=index)