from playwright.sync_api import Page, expect
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_toolbar = CreateCourseToolbarViewComponent(page)
        self.create_exercise_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.exercises_form = CreateCourseExerciseFormComponent(page)
        self.empty_view_image = EmptyViewComponent(page, 'create-course-preview')
        self.upload_image_preview = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.empty_view_exercises = EmptyViewComponent(page, 'create-course-exercises')