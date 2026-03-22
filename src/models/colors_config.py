from dataclasses import dataclass


@dataclass
class ColorsConfig:
    bgcolor_page: str = "#FFFFFF"
    bgcolor_appbar_back: str = "#F0F0F0"
    bgcolor_add_note_button: str = "#DDDDDD"
    bgcolor_alert_bar: str = "#FFFFFF"
    bgcolor_note_headder: str = "#FFFFFF"
    bgcolor_text_note: str = "#FFFFFF"
