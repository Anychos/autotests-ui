from elements.base_element import BaseElement


class FileInput(BaseElement):
    def set_file(self, file_path: str, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.set_input_files(file_path)