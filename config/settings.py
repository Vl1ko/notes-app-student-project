from dataclasses import dataclass
from pathlib import  Path


@dataclass
class Config():
    path_for_colors: str = Path("data/colors_data.json")
    path_for_zametki : str = Path("data/zametki.json")