import json
from pathlib import Path


class Colors_Set:
    """Работа с данными цветов"""

    DEFAULT_FILE_PATH = Path("data/colors_data.json")

    def __init__(self, chapter_config, file_path=DEFAULT_FILE_PATH):
        self.file_path = file_path or self.DEFAULT_FILE_PATH
        self.chapter_config = chapter_config

    def read_config_color(self) -> dict:
        """Читает нужный пресет цветовых настроек"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if self.chapter_config not in data:
                print(
                    f"Ошибка: тема '{self.chapter_config}' не найдена в {self.file_path}"
                )
                return {}

            return data[self.chapter_config]

        except FileNotFoundError:
            print(f"Ошибка: файл с цветами не найден: {self.file_path}")
            return {}
        except json.JSONDecodeError as e:
            print(f"Ошибка: неверный JSON в файле {self.file_path}: {e}")
            return {}

    @staticmethod
    def read_tupe_tems() -> str:
        """Прочитать тип используемой темы"""
        try:
            with open(Path("data/colors_data.json"), "r", encoding="utf-8") as f:
                data = json.load(f)
            data_return = data["Tems_mode"]["chapter"]
            return data_return
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(print(f"Ошибка: файл с темами не найден: {e}"))
            return {}

    @staticmethod
    def change_tupe_in(tupe_of_change: str):
        """Изменение нынещней темы на другую"""
        try:
            with open(Path("data/colors_data.json"), "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(e)
        data["Tems_mode"]["chapter"] = tupe_of_change
        with open(Path("data/colors_data.json"), "w", encoding="utf-8") as fif:
            fif.write(json.dumps(data, ensure_ascii=False, indent=4))
