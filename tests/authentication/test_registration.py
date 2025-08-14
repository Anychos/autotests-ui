import pytest
from allure_commons.types import Severity
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import allure
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.parent_suites import AllureParentSuite
from tools.allure.stories import AllureStory
from tools.allure.sub_suites import AllureSubSuite
from tools.allure.suites import AllureSuite


@pytest.mark.regression
@pytest.mark.registration
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureParentSuite.LMS)
@allure.suite(AllureSuite.AUTHENTICATION)
@allure.sub_suite(AllureSubSuite.REGISTRATION)
class TestRegistration:
    @allure.title('Регистрация с валидными данными')
    @allure.severity(Severity.BLOCKER)
    def test_successful_registration(self, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill_registration_form(
            email="user.name@gmail.com",
            username="username",
            password="password")
        registration_page.registration_form.check_visible(email="user.name@gmail.com", username="username", password="password")
        registration_page.click_registration_button()
        dashboard_page.toolbar.check_visible()