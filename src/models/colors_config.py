import json
from pathlib import Path


class Colors_config:
    """Инициализаци данных заметки в обьект"""
    def __init__(self,bgcolor_page,bgcolor_appbar_back,bgcolor_add_note_button,bgcolor_alert_bar,bgcolor_note_headder,bgcolor_text_note):
        self.bgcolor_page = bgcolor_page
        self.bgcolor_appbar_back = bgcolor_appbar_back
        self.bgcolor_add_note_button = bgcolor_add_note_button
        self.bgcolor_alert_bar = bgcolor_alert_bar
        self.bgcolor_note_headder = bgcolor_note_headder
        self.bgcolor_text_note = bgcolor_text_note
