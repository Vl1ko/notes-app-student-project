import json
from pathlib import Path
from typing import List, Optional

from src.models.note import Note


class NoteRepository:
    """Репозиторий для работы с заметками"""

    DEFAULT_FILE_PATH = Path("data/zametki.json")

    def __init__(self, file_path: Optional[Path] = None):
        self.file_path = file_path or self.DEFAULT_FILE_PATH
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        """Создание файла, если не существует"""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self._write_data({"Notes": []})

    def _read_data(self) -> dict:
        """Чтение данных из JSON с обработкой ошибок"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()

                if not content:
                    return {"Notes": []}
                data = json.loads(content)

                if data is None:
                    return {"Notes": []}
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return {"Notes": []}

    def _write_data(self, data: dict) -> None:
        """Запись данных в JSON"""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_all_notes(self) -> List[Note]:
        """Получение всех заметок"""
        data = self._read_data()
        return [Note.from_dict(note_data) for note_data in data.get("Notes", [])]

    def add_note(self, note: Note) -> None:
        """Добавление заметки"""
        data = self._read_data()
        data["Notes"].append(note.to_dict())
        self._write_data(data)

    def delete_note(self, note_id: str) -> bool:
        """Удаление заметки по ID"""
        data = self._read_data()
        original_length = len(data["Notes"])
        data["Notes"] = [n for n in data["Notes"] if n.get("note_id") != note_id]

        if len(data["Notes"]) < original_length:
            self._write_data(data)
            return True
        return False

    def update_note(self, note: Note) -> bool:
        """Обновление существующей заметки"""
        data = self._read_data()
        for i, item in enumerate(data["Notes"]):
            if item.get("note_id") == note.note_id:
                data["Notes"][i] = note.to_dict()
                self._write_data(data)
                return True
        return False

    def search_notes(self, query: str) -> List[Note]:
        """Поиск заметок по заголовку"""
        all_notes = self.get_all_notes()
        return [note for note in all_notes if query.lower() in note.header.lower()]
