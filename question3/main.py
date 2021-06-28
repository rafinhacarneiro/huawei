import pandas as pd
from pathlib import Path
from datetime import datetime as dt

def files_dataframe(folder: str) -> pd.DataFrame:

    files = list( Path(folder).rglob("*.*") )

    for i, file in enumerate(files):
        stats = file.stat()

        files[i] = {
            "name": file.stem,
            "extension": file.suffix,
            "location": file.parent,
            "size": stats.st_size,
            "last_modified": dt.utcfromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        }

    return pd.DataFrame(files)


this_folder = str(Path(__file__).parent.absolute()) + "\\files"
df = files_dataframe(this_folder)

print(this_folder)
print(df)