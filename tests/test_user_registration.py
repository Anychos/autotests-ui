from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.smoke
def test_user_registration_positive(start_chrome: Page):
    """
    Тест успешной регистрации пользователя
    """
    start_chrome.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration") # переход на сайт

    email_input = start_chrome.get_by_test_id("registration-form-email-input").locator("input") # поиск поля login
    email_input.fill("user.name@gmail.com") # заполнение поля email
    username_input = start_chrome.get_by_test_id("registration-form-username-input").locator("input")  # поиск поля username
    username_input.fill("username")  # заполнение поля username
    password_input = start_chrome.get_by_test_id("registration-form-password-input").locator("input")  # поиск поля password
    password_input.fill("password")  # заполнение поля password

    registration_button = start_chrome.get_by_test_id("registration-page-registration-button") # поиск кнопки registration
    registration_button.click()  # нажатие на кнопку

    dashboard_title = start_chrome.get_by_test_id("dashboard-toolbar-title-text") # поиск заголовка dashboard
    expect(dashboard_title).to_be_visible() # ожидание появления элемента
