import flet as ft

from src.database.colors_set import ColorsSet
from src.database.note_repository import NoteRepository
from src.models import Note
from src.models.colors_config import ColorsConfig
from src.ui.components import create_note_card


def main(page: ft.Page):
    page.title = "ToDoList"
    page.padding = 20
    page.window_width = 800
    page.window_height = 600

    repo = NoteRepository()

    colr_s = ColorsSet(ColorsSet.read_tupe_tems())
    colr_conf = ColorsConfig(**colr_s.read_config_color())

    notes_container = ft.Row(
        controls=[],
        alignment=ft.MainAxisAlignment.START,
        spacing=20,
        wrap=True,
        run_spacing=20,
    )

    search_field = ft.TextField(
        label="Поиск по названию заметки",
        width=600,
        on_submit=lambda e: search_notes(e.control.value),
    )

    #Поиск и отображение соответсвующих заметок.
    def search_notes(query: str):
        results = repo.search_notes(query)
        notes_container.controls.clear()
        for note in results:

            def delete_handler(e, note_id=note.note_id):
                if repo.delete_note(note_id):
                    refresh_notes()

            notes_container.controls.append(
                create_note_card(
                    note=note,
                    on_delete=delete_handler,
                    on_save=save_handler,
                )
            )
        page.update()


    def add_new_note(e):
        new_note = Note(header="", content="")
        repo.add_note(new_note)
        refresh_notes()

    def save_handler(updated_note: Note):
        repo.update_note(updated_note)

    def refresh_notes():
        notes_container.controls.clear()
        for note in repo.get_all_notes():

            def delete_handler(e, note_id=note.note_id):
                if repo.delete_note(note_id):
                    refresh_notes()

            notes_container.controls.append(
                create_note_card(
                    note=note,
                    on_delete=delete_handler,
                    on_save=save_handler,
                )
            )
        page.update()

    def edit_color_in_white():
        """Изменение цветовой гаммы на белый"""
        ColorsSet.change_tupe_in("White_tems")
        refresh_colors()

    def edit_color_in_black():
        """Изменение цветовой гаммы на чёрный"""
        ColorsSet.change_tupe_in("Black_tems")
        refresh_colors()

    def refresh_colors():
        """Обновление цветовой гаммы"""
        colr_s = ColorsSet(ColorsSet.read_tupe_tems())
        colr_conf = ColorsConfig(**colr_s.read_config_color())
        page.bgcolor = colr_conf.bgcolor_page
        apbr.bgcolor = colr_conf.bgcolor_appbar_back
        settings_bar.bgcolor = colr_conf.bgcolor_alert_bar
        add_button.bgcolor = colr_conf.bgcolor_add_note_button
        page.update()

    # Верхняя панель
    top_bar = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            search_field,
            ft.IconButton(
                icon=ft.Icons.SEARCH,
                on_click=lambda e: search_notes(search_field.value),   # <-- добавлен вызов функции поиска
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

    # Алерт бар
    settings_bar = ft.AlertDialog(
        bgcolor=colr_conf.bgcolor_alert_bar,
        title=ft.Text("Выберете тему."),
        content=ft.Text("Выбранная вами тема будет сохранена и пременена сразу."),
        actions=[
            ft.Container(
                content=ft.TextButton(
                    content="Белая тема", on_click=lambda _: edit_color_in_white()
                ),
            ),
            ft.Container(
                content=ft.TextButton(
                    content="Тёмная тема", on_click=lambda _: edit_color_in_black()
                ),
            ),
        ],
        title_padding=ft.Padding.all(25),
    )

    # Кнопка добаввления
    add_button = ft.Container(
        content=ft.IconButton(
            icon=ft.Icons.ADD,
            on_click=add_new_note,
            icon_size=30,
        ),
        width=60,
        height=60,
        border=ft.Border.all(2, "#000000"),
        border_radius=30,
        bgcolor=colr_conf.bgcolor_add_note_button,
    )

    # Нижняя панель
    apbr = ft.BottomAppBar(
        bgcolor=colr_conf.bgcolor_appbar_back,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.IconButton(icon=ft.Icons.HOME),
                add_button,
                ft.IconButton(
                    icon=ft.Icons.SETTINGS,
                    on_click=lambda e: page.show_dialog(settings_bar),
                ),
            ],
        ),
    )

    # Добавление нижней панели
    page.bottom_appbar = apbr

    # Добавление элементов
    page.add(top_bar, notes_area)

    # Вызываем свежие заметки
    refresh_notes()

    # Меняем цвет задней страницы
    page.bgcolor = colr_conf.bgcolor_page


if __name__ == "__main__":
    ft.app(target=main)
