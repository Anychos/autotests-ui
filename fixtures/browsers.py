import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture(scope="session")
def start_chrome(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page

@pytest.fixture(scope="session", autouse=False)
def initialize_browser_state(start_chrome: Page) -> None:
    start_chrome.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")  # переход на сайт

    email_input = start_chrome.get_by_test_id("registration-form-email-input").locator("input")  # поиск поля login
    email_input.fill("user.name@gmail.com")  # заполнение поля email
    username_input = start_chrome.get_by_test_id("registration-form-username-input").locator(
        "input")  # поиск поля username
    username_input.fill("username")  # заполнение поля username
    password_input = start_chrome.get_by_test_id("registration-form-password-input").locator(
        "input")  # поиск поля password
    password_input.fill("password")  # заполнение поля password

    registration_button = start_chrome.get_by_test_id(
        "registration-page-registration-button")  # поиск кнопки registration
    registration_button.click()  # нажатие на кнопку

    context = start_chrome.context
    context.storage_state(path="browser-state.json")

@pytest.fixture()
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page