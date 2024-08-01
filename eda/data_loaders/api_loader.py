from .base_loader import DataLoader
from dataclasses import dataclass
import pandas as pd


@dataclass()
class APIDataLoader(DataLoader):
    def __init__(self, base_url: str, endpoint: str, api_key: str, headers: dict = None):
        self.base_url = base_url
        self.endpoint = endpoint
        self.api_key = api_key
        self.headers = headers or {}

    def load_data(self, site: str, **kwargs) -> pd.DataFrame:
        """
        returns a pandas DataFrame from a particular API endpoint
        """
        pass
