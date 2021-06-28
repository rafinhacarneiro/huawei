import pandas as pd
from typing import Any
from os import path, getcwd
from time import time
from SpreadsheetBuilder.Exceptions import SaveDirError

class Builder:
    """
    Builder

        Builds spreadsheets based on given data
    """

    default_save_directory = path.abspath(getcwd()) + "\\Spreadsheets"

    def save_as_xlsx(
        self,
        data: Any,
        filename = None,
        save_dir = None
    ) -> str:
        """
        Saves the data as .xlsx spreadsheet.

        Args
            - data (Any) : Any type of data
            - filename (str) : Desired name for the spreadsheet. Defaults to the current time in UNIX timestamp format
            - save_dir (str) : Path to save the file. Defaults to the working directory

        Returns
            str : The full path to the spreadsheet

        Raises
            SaveDirError: The selected path doesn't exists

        """

        df = pd.DataFrame(data)

        if not save_dir:
            save_dir = self.default_save_directory

        if not filename:
            filename = self.now

        print(f"{save_dir}\\{filename}.xlsx")

        if not path.exists(save_dir):
            raise(SaveDirError(save_dir))

        df.to_excel(f"{save_dir}\\{filename}.xlsx")


    @property
    def now(self):
        return str( int( time() ) )
