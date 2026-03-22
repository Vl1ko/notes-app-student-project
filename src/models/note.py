import uuid
from dataclasses import dataclass
from typing import Optional


@dataclass
class Note:
    """Модель заметки"""

    header: str = ""
    content: str = ""
    note_id: Optional[str] = None

    def __post_init__(self):
        """Генерация ID если не задан"""
        if self.note_id is None:
            self.note_id = str(uuid.uuid4())

    def to_dict(self) -> dict:
        """Конвертация в словарь для JSON"""
        return {"header": self.header, "content": self.content, "note_id": self.note_id}

    @classmethod
    def from_dict(cls, data: dict) -> "Note":
        """Создание объекта из словаря"""
        return cls(
            header=data.get("header", ""),
            content=data.get("content", ""),
            note_id=data.get("note_id"),
        )
