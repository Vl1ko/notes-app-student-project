import flet as ft

from src.database.note_repository import NoteRepository
from src.models import Note


def main(page: ft.Page):
    page.title = "ToDoList"
    page.padding = 20
    page.window_width = 800
    page.window_height = 600

    # Инициализация репозитория
    repo = NoteRepository()

    # Контейнер для заметок
    notes_container = ft.Row(
        controls=[],
        alignment=ft.MainAxisAlignment.START,
        spacing=20,
        wrap=True,
        run_spacing=20,
    )

    # Поле поиска
    search_field = ft.TextField(
        label="Поиск по названию заметки",
        width=600,
        on_submit=lambda e: search_notes(e.control.value),
    )

    def create_note_card(note: Note, on_delete, on_save, page: ft.Page) -> ft.Container:
        def delete_handler(e):
            if on_delete(note.note_id):
                refresh_notes()

        return note.create_ui_component(on_delete=delete_handler, on_save=on_save)

    def search_notes(query: str):
        """Обработчик поиска"""
        results = repo.search_notes(query)
        # Отобразить результаты (можно добавить отдельный компонент)
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Найдено: {len(results)} заметок")
        )
        page.snack_bar.open = True
        page.update()

    def add_new_note(e):
        """Добавление новой заметки"""
        new_note = Note(header="Новая заметка", content="")
        repo.add_note(new_note)
        refresh_notes()

    def save_handler(updated_note: Note):
        repo.update_note(updated_note)  # ← чистое сохранение

    def refresh_notes():
        """Обновление списка заметок"""
        notes_container.controls.clear()
        for note in repo.get_all_notes():
            notes_container.controls.append(
                create_note_card(
                    note,
                    repo.delete_note,
                    save_handler,
                    page,
                )
            )
        page.update()

    # Верхняя панель
    top_bar = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            search_field,
            ft.IconButton(
                icon=ft.Icons.SEARCH,
                on_click=lambda e: search_notes(search_field.value),
            ),
        ],
        spacing=10,
    )

    # Область заметок
    notes_area = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[notes_container],
    )

    # Нижняя панель
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor="#FFFFFF",
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.IconButton(icon=ft.Icons.HOME),
                ft.Container(
                    content=ft.IconButton(
                        icon=ft.Icons.ADD,
                        on_click=add_new_note,
                        icon_size=30,
                    ),
                    width=60,
                    height=60,
                    border=ft.Border.all(2, "#000000"),
                    border_radius=30,
                    bgcolor="#4CAF50",
                ),
                ft.IconButton(icon=ft.Icons.SETTINGS),
            ],
        ),
    )

    page.add(top_bar, notes_area)
    refresh_notes()


if __name__ == "__main__":
    ft.app(target=main)
