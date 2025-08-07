import pytest
from playwright.sync_api import Page
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def login_page(start_chrome: Page) -> LoginPage:
    return LoginPage(page=start_chrome)

@pytest.fixture
def registration_page(start_chrome: Page) -> RegistrationPage:
    return RegistrationPage(page=start_chrome)

@pytest.fixture
def dashboard_page(start_chrome: Page) -> DashboardPage:
    return DashboardPage(page=start_chrome)

@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page_with_state)

@pytest.fixture
def courses_list_page(start_chrome: Page) -> CoursesListPage:
    return CoursesListPage(page=start_chrome)

@pytest.fixture
def courses_list_page_with_state(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=chromium_page_with_state)

@pytest.fixture
def create_course_page_with_state(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page_with_state)

