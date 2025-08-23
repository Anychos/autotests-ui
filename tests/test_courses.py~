import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.create_course_toolbar.check_visible()
    create_course_page.empty_view_image.check_visible(title='No image selected', description='Preview of selected image will be displayed here')
    create_course_page.upload_image_preview.check_visible(is_image_uploaded=False)
    create_course_page.create_course_form.check_visible(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0")
    create_course_page.upload_image_preview.upload_preview_image("./test_data/files/image.jpg")
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

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()
    courses_list_page.toolbar.check_visible()
    courses_list_page.empty_view.check_visible(title='There is no results', description='Results from the load test pipeline will be displayed here')