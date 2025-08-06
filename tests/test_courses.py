import pytest
from playwright.sync_api import expect
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    """
    Тест пустого списка курсов
    """
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")  # переход на сайт

    courses_page_title = chromium_page_with_state.locator(
        '//h6[@data-testid="courses-list-toolbar-title-text"]')  # поиск заголовка страницы
    expect(courses_page_title).to_have_text("Courses")
    print("Заголовок страницы 'Courses' найден")

    courses_page_no_results = chromium_page_with_state.locator(
        '//h6[@data-testid="courses-list-empty-view-title-text"]')  # поиск заголовка страницы
    expect(courses_page_no_results).to_have_text("There is no results")
    print("Заголовок пустого блока 'There is no results' найден")

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
    create_course_page.upload_preview_image("C:\\Users\\anton\PycharmProjects\\autotests-ui\\testdata\\files\\image.jpg")
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form("Playwright", "2 weeks", "Playwright", "100", "10")
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(0, "Playwright", "100", "10", "2 weeks")