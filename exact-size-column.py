# Exact size column extension for nautilus-python
# by D15C0DE 2024

import os, locale
from urllib.parse import unquote
from gi.repository import GObject, Nautilus
from typing import List

class ColumnExtension(GObject.GObject, Nautilus.ColumnProvider, Nautilus.InfoProvider):
    def get_columns(self) -> List[Nautilus.Column]:
        column = Nautilus.Column(
            name="NautilusPython::exact_size_column",
            attribute="exact_size",
            label="Exact Size",
        )

        return [
            column,
        ]

    def update_file_info(self, file: Nautilus.FileInfo) -> None:
        if file.get_uri_scheme() != "file":
            return

        if file.is_gone():
            return

        filename = unquote(file.get_uri()[7:])

        if file.is_directory():
            size = 0
            for path in os.scandir(filename):
                size += 1
            disp = "item"
        else:
            size = os.stat(filename).st_size
            disp = "byte"

        locale.setlocale(locale.LC_ALL, '') 
        file.add_string_attribute("exact_size", f"{size:n}" + " " + disp + ("" if size == 1 else "s"))
