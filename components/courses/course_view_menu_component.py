from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.button import Button
import allure


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, 'course-view-menu-button', 'Course view menu button')
        self.edit_menu_item = Button(page, 'course-view-edit-menu-item', 'Course menu edit button')
        self.delete_menu_item = Button(page, 'course-view-delete-menu-item', 'Course menu delete button')

    @allure.step("Открытие меню курса и клик по кнопке редактирования")
    def click_edit(self, index: int):
        self.menu_button.click(index=index)

        self.edit_menu_item.check_visible(nth=index)
        self.edit_menu_item.click(nth=index)

    @allure.step("Открытие меню курса и клик по кнопке удаления")
    def click_delete(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_menu_item.check_visible(nth=index)
        self.delete_menu_item.click(nth=index)