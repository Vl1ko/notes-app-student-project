import json
import flet as ft


class Find_block:
    def __init__(self, file_name_when_data, list_with_data = None, object_when_find_polzovatel = ""):
        self.file_name_when_data = file_name_when_data
        self.list_with_data = list_with_data
        self.object_when_find_polzovatel = object_when_find_polzovatel
    def find_object(self):
        with open(self.file_name_when_data,mode= "r",encoding= "utf-8") as json_file:
            data = json.load(json_file)
        list_tru_oject = []
        otv_polzovatela = self.object_when_find_polzovatel
        for block in list(data):
            if str(otv_polzovatela) in block:
                list_tru_oject.append(block)
        return list_tru_oject
help(ft.Column)
