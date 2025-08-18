import pytest
from allure_commons.types import Severity
from config import settings
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
import allure
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.parent_suites import AllureParentSuite
from tools.allure.stories import AllureStory
from tools.allure.sub_suites import AllureSubSuite
from tools.allure.suites import AllureSuite
from tools.routes import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureParentSuite.LMS)
@allure.suite(AllureSuite.COURSES)
@allure.sub_suite(AllureSubSuite.COURSES)
class TestCourses:
    @allure.title('Создание курса')
    @allure.severity(Severity.BLOCKER)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(AppRoute.CREATE_COURSE)
        create_course_page.create_course_toolbar.check_visible()
        create_course_page.empty_view_image.check_visible(title='No image selected', description='Preview of selected image will be displayed here')
        create_course_page.upload_image_preview.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0")
        create_course_page.upload_image_preview.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.upload_image_preview.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill_create_course_form(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10")
        create_course_page.create_course_form.check_visible(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10")
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=False)
        create_course_page.create_exercise_toolbar.check_visible()
        create_course_page.empty_view_exercises.check_visible(title='There is no exercises', description='Click on "Create exercise" button to create new exercise')
        create_course_page.create_exercise_toolbar.click_create_exercise_button()
        create_course_page.exercises_form.check_visible(index=0, title="Exercise title", description="Exercise description")
        create_course_page.exercises_form.fill(index=0, title="Playwright", description="Playwright")
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.course_card_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )

    @allure.title('Проверка пустого списка курсов')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)
        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar.check_visible()
        courses_list_page.empty_view.check_visible(title='There is no results', description='Results from the load test pipeline will be displayed here')

    @allure.title('Создание и редактирование курса')
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(AppRoute.CREATE_COURSE)
        create_course_page.create_course_toolbar.check_visible()
        create_course_page.empty_view_image.check_visible(title='No image selected',
                                                          description='Preview of selected image will be displayed here')
        create_course_page.upload_image_preview.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0")
        create_course_page.upload_image_preview.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.upload_image_preview.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill_create_course_form(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10")
        create_course_page.create_course_form.check_visible(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10")
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=False)
        create_course_page.create_exercise_toolbar.check_visible()
        create_course_page.empty_view_exercises.check_visible(title='There is no exercises',
                                                              description='Click on "Create exercise" button to create new exercise')
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.course_card_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )
        courses_list_page.course_card_menu.click_edit(index=0)
        create_course_page.create_course_form.fill_create_course_form(
            title="Test",
            estimated_time="2 days",
            description="Test",
            max_score="1000",
            min_score="100")
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.course_card_view.check_visible(
            index=0, title="Test", max_score="1000", min_score="100", estimated_time="2 days"
        )