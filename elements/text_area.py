from playwright.sync_api import Locator, expect
from elements.base_element import BaseElement
import allure
from tools.logger import get_logger

logger = get_logger('TEXT_AREA')


class TextArea(BaseElement):
    @property
    def type_of(self) -> str:
        return 'text area'

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f'Заполнение поля "{self.type_of} {self.name}" значением "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

    def check_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Проверка что значение поля "{self.type_of} {self.name}" соответствует ожидаемому "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)

    def clear(self, nth: int = 0, **kwargs):
        step = f'Очистка поля "{self.type_of} {self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.clear()