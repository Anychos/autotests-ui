from elements.base_element import BaseElement
import allure
from tools.logger import get_logger

logger = get_logger('FILE_INPUT')


class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return 'file input'

    def set_file(self, file_path: str, nth: int = 0, **kwargs):
        step = f'Загрузка файла "{file_path}" в поле "{self.type_of} {self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth,**kwargs)
            logger.info(step)
            locator.set_input_files(file_path)