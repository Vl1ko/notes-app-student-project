import flet as ft

class Notes:
    def __init__(self,conten_of_zametka = "",headder = ""):
        self.conten_of_zametka = conten_of_zametka
        self.headder = headder
        self.object_note =ft.Container(
        content=ft.Column(
            controls=[
                 ft.Container(
                    content=ft.TextField(
                        hint_text="Заголовок",
                        value = self.headder,
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
                        value=self.conten_of_zametka,
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


