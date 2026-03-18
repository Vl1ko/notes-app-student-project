import flet as ft
from develop.object.Notes import Notes
import json

from flet.controls import page


#Добавление заметки в базу
def upload(notes_object_dict : dict):
    with open('zametki.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    data["Notes"].append(notes_object_dict)
    with open('zametki.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))

#Список словарей
def load():
    with open('zametki.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    data_list = data["Notes"]
    return data_list


#Список обьектов как обьектов из джейсон файлика
def wiev_object_list(data_list: list):
    list_object = []
    for block in data_list:
        notesss = Notes(**block)
        list_object.append(notesss)
    return list_object


#НЕ ИСПОЛЬЗУЕТСЯ ПОКА ЧТО
def append_notes():
    note_zametka = Notes()
    note_dict = {
        "conten_of_zametka" : note_zametka.conten_of_zametka,
        "headder" : note_zametka.headder,
    }
    upload(note_dict)


def list_of_notes_object_wiev(link : list):
    wiew_list = []
    for block in link:
        notesss = Notes(**block)
        wiew_list.append(notesss.object_note)
    return wiew_list


