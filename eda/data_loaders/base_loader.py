from abc import ABC, abstractmethod
import pandas as pd


class DataLoader(ABC):
    @abstractmethod
    def load_data(self, *args, **kwargs) -> pd.DataFrame:
        """ Loads data and returns a pandas DataFrame. """
        pass
