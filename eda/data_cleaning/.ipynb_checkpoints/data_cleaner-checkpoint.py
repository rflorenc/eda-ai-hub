import pandas as pd
import numpy as np
from ..pandas_support import Sanitizer


class DataCleaning:
    """
    DataCleaning class performs simple validations and
    inplace changes to pandas objects
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def fillna_col_with_default(self, col: str, fill_value):
        Sanitizer.check_col_exists(self.df, col)
        self.df[col].fillna(fill_value, inplace=True)

    def fillna_col_with_mode(self, col: str):
        Sanitizer.check_col_exists(self.df, col)
        mode = self.df[col].mode()[0]
        self.df[col].fillna(mode, inplace=True)

    def dropna_col(self, col: str):
        """
        if >= 75% of data from a particular column is missing then dropna
        it is considered an incomplete dataset for that particular col
        """
        Sanitizer.check_col_exists(self.df, col)
        Sanitizer.check_isna_values_col_percent(self.df, col, 75)
        self.df[col].dropna(inplace=True)

    @staticmethod
    def enforce_df_quality(self, rawdf: pd.DataFrame) -> pd.DataFrame:
        for k, v in rawdf.items():
            for idx, val in enumerate(v):
                if not pd.isna(val):
                    # careful because for instance lat and long values can be negative
                    if isinstance(val, float) or val < 0:
                        # modified in-place
                        rawdf.at[rawdf.index[idx], k] = np.nan
        return rawdf
