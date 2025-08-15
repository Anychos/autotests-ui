from playwright.sync_api import Page
import allure
from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.Icon import Icon
from elements.Image import Image
from elements.button import Button
from elements.file_input import FileInput
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.preview_image = Image(page, f'{identifier}-image-upload-widget-preview-image', 'Preview image')

        self.image_upload_info_icon = Icon(page, f'{identifier}-image-upload-widget-info-icon', 'Image upload info icon')
        self.image_upload_info_title = Text(page, f'{identifier}-image-upload-widget-info-title-text', 'Image upload info title')
        self.image_upload_info_description = Text(page,
            f'{identifier}-image-upload-widget-info-description-text',
            'Image upload info description'
        )

        self.upload_button = Button(page, f'{identifier}-image-upload-widget-upload-button', 'Upload button')
        self.remove_button = Button(page, f'{identifier}-image-upload-widget-remove-button', 'Remove button')
        self.upload_input = FileInput(page, f'{identifier}-image-upload-widget-input', 'File input')

    @allure.step('Проверка видимости виджета загрузки изображения')
    def check_visible(self, is_image_uploaded: bool = False):
        self.image_upload_info_icon.check_visible()
        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_text(
            'Tap on "Upload image" button to select file'
        )

        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_text('Recommended file size 540X300')

        self.upload_button.check_visible()

        if is_image_uploaded:
            self.remove_button.check_visible()
            self.preview_image.check_visible()

        if not is_image_uploaded:
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self):
        self.remove_button.click()

    @allure.step('Загрузка изображения')
    def upload_preview_image(self, file: str):
        self.upload_input.set_file(file)