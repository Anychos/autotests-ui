import pytest
from playwright.sync_api import sync_playwright, expect, Page


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

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list_2(chromium_page_with_state):
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