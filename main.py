from develop.utils.find_line import Find_block
from develop.object.Notes import *
from develop.Note_work import *

find_obj = Find_block("text.json",None,"")


def main(page: ft.Page):
    page.title = "ToDoList"
    page.padding = 3
    # Добавить отображение всех заметок после запуска
    # Добавить фикс размер окна









    #Функция которая ищет те названия записок в которых имеется значение введёное пользоватлелем в названии
    def find_zapiska():
        find_obj.object_when_find_polzovatel = text_wwod.value
        f_list = find_obj.find_object()
        find_obj.object_when_find_polzovatel = ""
        block_wiwod.value = f_list
        page.update()

    def refresh_notes():
        new_notes_containers = list_of_notes_object_wiev(load())
        line_zametka.controls = new_notes_containers
        page.update()

    def add_new_note(e):  # Добавляем параметр e для event
        note_zametka = Notes()
        note_dict = {
            "conten_of_zametka": note_zametka.conten_of_zametka,
            "headder": note_zametka.headder,
        }
        upload(note_dict)
        refresh_notes()



        #Поле вовода
    text_wwod = ft.TextField(
        label = "Введите название вашей заметки:",
        width = 600,
        on_submit = find_zapiska,
    )
    #Кнопка поиск хпх
    find_knopka = ft.Container(
        content = ft.IconButton(
            icon = ft.Icons.SEARCH,
            on_click = find_zapiska,
        ),
        border=ft.Border.all(1, "#000000"),
        width = 50,
        height = 50,
        border_radius = 8,
    )

    #Первая строка выводимая
    first_line  = ft.Row(
        alignment = ft.MainAxisAlignment.CENTER,
        controls = [
            text_wwod,
            find_knopka,
        ],
        spacing = 2
    )

    #Заглушка для проверки заметок
    block_wiwod = ft.Text(
        value = "Вы не искали заметки."
    )

    #



    #линия заметок
    line_zametka = ft.Row(
        controls = [],
        alignment = ft.MainAxisAlignment.START,
        spacing = 20,
        wrap = True,
        run_spacing = 20,
    )


    #область для заметок , пока что
    place_for_zametki = ft.Column(
        expand = True,
        scroll  = ft.ScrollMode.AUTO,
        controls = [line_zametka],
    )



    #Cама ячейка











    page.add(first_line,block_wiwod,place_for_zametki)


    #Пока что просто бар меню потому что я так хочу мне пофиг
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor = "#FFFFFF",
        content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls = [
                ft.IconButton(
                    icon = ft.Icons.HOME,
                ),
                ft.Container(
                    content = ft.IconButton(
                        icon = ft.Icons.ADD,
                        on_click = add_new_note
                    ),
                    width = 100,
                    height = 100,
                    border=ft.Border.all(2, "#000000"),
                    border_radius = 50,
                )
                ,
                ft.IconButton(
                    icon = ft.Icons.SETTINGS,
                )
            ]
        )
    )


    refresh_notes()
ft.run(main)
