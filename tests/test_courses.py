import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page_with_state: CoursesListPage):
    """
    Тест пустого списка курсов
    """
    courses_list_page_with_state.open_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page_with_state.check_visible_courses_title()
    courses_list_page_with_state.check_visible_create_course_button()
    courses_list_page_with_state.check_visible_empty_view()
    courses_list_page_with_state.navbar.check_visible("username")
    courses_list_page_with_state.sidebar.check_visible()

def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    """
    Тест создания курса
    """
    create_course_page.open_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form("", "", "", "0", "0")
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form("Playwright", "2 weeks", "Playwright", "100", "10")
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(0, "Playwright", "100", "10", "2 weeks")