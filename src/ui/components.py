import flet as ft

from src.models.note import Note


def create_note_card(
    note: Note,
    on_delete=None,
    on_save=None,
) -> ft.Container:
    def on_header_change(e):
        note.header = e.control.value
        if on_save:
            on_save(note)

    def on_content_change(e):
        note.content = e.control.value
        if on_save:
            on_save(note)

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.TextField(
                    value=note.header,
                    hint_text="Заголовок",
                    multiline=False,
                    width=400,
                    height=50,
                    text_align=ft.TextAlign.LEFT,
                    border="none",
                    on_blur=on_header_change,
                ),
                ft.Divider(color="#000000", height=1, thickness=2),
                ft.TextField(
                    value=note.content,
                    hint_text="Содержимое заметки",
                    multiline=True,
                    width=400,
                    height=270,
                    text_align=ft.TextAlign.LEFT,
                    border="none",
                    on_blur=on_content_change,
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
        bgcolor="#a293ab",  # <-- Изменён цвет
        border=ft.Border.all(4, "#000000"),
        border_radius=10,
        padding=10,
    )
