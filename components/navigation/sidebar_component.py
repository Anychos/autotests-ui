import re
from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent
import allure


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page, 'logout')
        self.courses_list_item = SidebarListItemComponent(page, 'courses')
        self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')

    @allure.step("Проверка видимости сайдбара")
    def check_visible(self):
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    @allure.step("Клик по кнопке выхода из аккаунта")
    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    @allure.step("Клик по кнопке курсов")
    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    @allure.step("Клик по кнопке дашборда")
    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))