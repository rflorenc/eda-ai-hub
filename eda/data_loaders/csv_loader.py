from .base_loader import DataLoader
from dataclasses import dataclass
import pandas as pd
import os


@dataclass
class CSVDataLoader(DataLoader):
    def __init__(self, datasets_dir: str):
        self.datasets_dir = os.path.abspath(datasets_dir)
        if not os.path.exists(self.datasets_dir):
            raise FileNotFoundError(f"Please ensure the \"{datasets_dir}\" directory exists. Exit.")

    def load_data(self, dataset_file: str, **read_csv_kwargs) -> pd.DataFrame:
        """
        returns a pandas DataFrame from a dataset file
        """
        file_path = os.path.join(self.datasets_dir, dataset_file)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file \"{file_path}\" does not exist.")

        return pd.read_csv(file_path, **read_csv_kwargs)
