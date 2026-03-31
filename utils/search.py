import json
from typing import List, Optional
from pathlib import Path


class SearchService:
    """Сервис поиска по заметкам"""

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def search_in_file(self, query: str, field: str = "header") -> List[dict]:
        """
        Поиск записей в JSON файле

        Args:
            query: Строка поиска
            field: Поле для поиска (header, content)

        Returns:
            Список найденных записей
        """
        if not query.strip():
            return []

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

        results = []
        for note in data.get("Notes", []):
            if query.lower() in str(note.get(field, "")).lower():
                results.append(note)

        return results