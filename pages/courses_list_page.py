from playwright.sync_api import Page, expect
from components.courses.course_view_component import CourseViewComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = CoursesListToolbarViewComponent(page)
        self.course_card_view = CourseViewComponent(page)
        self.course_card_menu = CourseViewMenuComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')