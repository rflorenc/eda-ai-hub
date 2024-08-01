from .base_loader import DataLoader
from dataclasses import dataclass
import pandas as pd
import requests


@dataclass()
class APIDataLoader(DataLoader):
    def __init__(self, base_url: str, endpoint: str, api_key: str, headers: dict = None):
        self.base_url = base_url
        self.endpoint = endpoint
        self.api_key = api_key
        self.headers = headers or {}

    def load_data(self, site: str, **kwargs) -> pd.DataFrame:
        """
        returns a pandas DataFrame from UK MET site endpoint
        """

        # define 3hourly as default
        params = {'res': kwargs.get('res', '3hourly'), 'api_key': self.api_key}
        url = f"{self.base_url}/{site}"
        resp = requests.get(url, params=params, headers=self.headers)
        resp.raise_for_status()
        data = resp.json()
        return pd.DataFrame(data)

    def load_sitelist(self, params=None) -> pd.DataFrame:
        """
        returns a pandas DataFrame from UK MET sitelist endpoint
        """
        url = f"{self.base_url}/{self.endpoint}?key={self.api_key}"
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        return pd.DataFrame(data)



