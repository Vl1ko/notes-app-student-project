import uuid
from dataclasses import dataclass
from typing import Optional

import flet as ft


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

    def create_ui_component(self, on_delete=None, on_save=None) -> ft.Container:
        """Создание UI компонента заметки"""

        def on_header_change(e):
            """Обработчик изменения заголовка"""
            self.header = e.control.value
            if on_save:
                on_save(self)  # Сохраняем заметку

        def on_content_change(e):
            """Обработчик изменения содержимого"""
            self.content = e.control.value
            if on_save:
                on_save(self)  # Сохраняем заметку

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.TextField(
                        value=self.header,
                        hint_text="Заголовок",
                        multiline=False,
                        width=400,
                        height=50,
                        text_align=ft.TextAlign.LEFT,
                        border="none",
                        on_blur=on_header_change,  # ← Добавлено
                    ),
                    ft.Divider(color="#000000", height=1, thickness=2),
                    ft.TextField(
                        value=self.content,
                        hint_text="Содержимое заметки",
                        multiline=True,
                        width=400,
                        height=270,
                        text_align=ft.TextAlign.LEFT,
                        border="none",
                        on_blur=on_content_change,  # ← Добавлено
                    ),
                    ft.Divider(color="#000000", height=1, thickness=2),
                    ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                icon_color="#DC143C",
                                on_click=on_delete,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.END,
                        width=400,
                        height=40,
                    ),
                ],
                run_spacing=0,
            ),
            width=400,
            height=420,
            bgcolor="#FFFF00",
            border=ft.Border.all(4, "#000000"),
            border_radius=10,
            padding=10,
        )
