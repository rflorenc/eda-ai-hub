import pandas as pd
import numpy as np
from dataclasses import dataclass


@dataclass
class Sanitizer:
    @staticmethod
    def check_null_values_percent(rawdf: pd.DataFrame) -> pd.DataFrame:
        nulls_percent_df = pd.DataFrame({'Null Values': rawdf.isna().sum(),
                                         'Percentage Null Values': (rawdf.isna().sum()) / (len(rawdf)) * 100})
        return nulls_percent_df

    @staticmethod
    def check_isna_values_col_percent(rawdf: pd.DataFrame, col: str, percent=75) -> bool:
        if not (0 <= percent <= 100):
            raise ValueError("Percent must be between 0 and 100.")

        null_percent = (rawdf[col].isna().sum() / len(rawdf)) * 100
        if null_percent < percent:
            raise ValueError(f"Cannot dropna for column {col} as it has less than {percent}% missing values.")

        return null_percent >= percent

    @staticmethod
    def check_col_exists(rawdf: pd.DataFrame, col: str):
        if col == "":
            raise ValueError("Column name must not be an empty string.")
        elif col not in rawdf.columns:
            raise KeyError(f"Column '{col}' does not exist in DataFrame.")

    @staticmethod
    def check_null_values(rawdf: pd.DataFrame) -> pd.DataFrame:
        nulls_df = pd.DataFrame({'Null Values': rawdf.isna().sum()})
        return nulls_df


