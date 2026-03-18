

import flet as ft



def main(page: ft.Page):
    headder = ft.Container(
        content=ft.TextField(
            hint_text="Заголовок",
            multiline = True,
            width=400,
            height=50,
            text_align=ft.TextAlign.LEFT,
            border="none",
        ),
        width = 400,
        height = 50,
    )
    dividers_of_block = ft.Divider(
        color="#000000",
        height=1,
        thickness=2,

    )
    text_of_zametka = ft.Container(
        content=ft.TextField(
            hint_text = "Содержимое заметки",
            multiline=True,
            text_align=ft.TextAlign.LEFT,
            border="none",
            width=400,
        ),
        width = 400,
        height = 270,
    )
    line_of_options_of_zametka = ft.Row(
        controls = [
            ft.Container(
                content = ft.IconButton(
                    icon = ft.Icons.DELETE,

                ),
                bgcolor = "#DC143C",
                border = ft.border.all(2,"#000000"),
                width=45,  # добавлена фиксированная ширина
                height=40,
                margin=ft.margin.only(0,0,3,0
                ),
                alignment=ft.Alignment.CENTER

            ),
        ],
        alignment=ft.MainAxisAlignment.END,
        width = 400,
        height=40,
    )



    pool_in_notes = ft.Column(
        controls=[
            headder,
            dividers_of_block,
            text_of_zametka,
            dividers_of_block,
            line_of_options_of_zametka
        ],
        run_spacing = 0
    )

    zametka = ft.Container(
        content = pool_in_notes,
    width = 400,
    height = 420,
    bgcolor = "#FFFF00",
    border = ft.Border.all(4, "#000000"),
    border_radius = 10,
    )
    page.add(zametka)

ft.run(main)

print()


def create_note():
    return ft.Container(
        content=ft.Column(
            controls=[
                 ft.Container(
                    content=ft.TextField(
                        hint_text="Заголовок",
                        value = "",
                        multiline=True,
                        width=400,
                        height=50,
                        text_align=ft.TextAlign.LEFT,
                        border="none",
                    ),
                    width=400,
                    height=50,
                ),
                 ft.Divider(
                    color="#000000",
                    height=1,
                    thickness=2,

                ),
                ft.Container(
                    content=ft.TextField(
                        hint_text="Содержимое заметки",
                        value="",
                        multiline=True,
                        text_align=ft.TextAlign.LEFT,
                        border="none",
                        width=400,
                    ),
                    width=400,
                    height=270,
                ),
                ft.Divider(
                    color="#000000",
                    height=1,
                    thickness=2,

                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.IconButton(
                                icon=ft.Icons.DELETE,
                            ),
                        bgcolor="#DC143C",
                        border=ft.border.all(2, "#000000"),
                        width=45,  # добавлена фиксированная ширина
                        height=40,
                        margin=ft.margin.only(0, 0, 3, 0),
                alignment=ft.Alignment.CENTER
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    width=400,
                    height=40,
                )
            ],
            run_spacing = 0
        ),
        width=400,
        height=420,
        bgcolor="#FFFF00",
        border=ft.Border.all(4, "#000000"),
        border_radius=10,
    )
baze_note = create_note