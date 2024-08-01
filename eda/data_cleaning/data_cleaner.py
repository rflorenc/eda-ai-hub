import pandas as pd
import numpy as np
from ..pandas_support import Sanitizer

class DataCleaning:
    """
    DataCleaning class performs simple validations and
    inplace changes to pandas objects.

    Attributes:
        df (pd.DataFrame): DataFrame that requires cleaning.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initialize DataCleaning with a DataFrame.

        Parameters:
        - df (pd.DataFrame): The DataFrame to be cleaned.
        """
        self.df = df

    def fillna_col_with_default(self, col: str, fill_value):
        """
        Fill missing values in a column with a provided default value.

        Parameters:
        - col (str): The column name in which null values should be replaced.
        - fill_value: The value to use for filling null values.
        """
        Sanitizer.check_col_exists(self.df, col)
        self.df[col].fillna(fill_value, inplace=True)

    def fillna_col_with_mode(self, col: str):
        """
        Fill missing values in a column with its mode (most frequent value).

        Parameters:
        - col (str): The column name in which null values should be replaced.
        """
        Sanitizer.check_col_exists(self.df, col)
        mode = self.df[col].mode()[0]
        self.df[col].fillna(mode, inplace=True)

    def dropna_col(self, col: str):
        """
        Drop a column if >= 75% of its data is missing.
        A column with 75% or more missing data is generally considered safe to drop

        Parameters:
        - col (str): The column name to be checked and possibly dropped.
        """
        Sanitizer.check_col_exists(self.df, col)
        Sanitizer.check_if_can_dropna_col(self.df, col, 75)
        self.df[col].dropna(inplace=True)

    @staticmethod
    def enforce_df_quality(self, rawdf: pd.DataFrame) -> pd.DataFrame:
        """
        Enforce quality checks on the DataFrame.
        For any non-NaN values that are either floats or negative, replace them with NaN.

        Parameters:
        - rawdf (pd.DataFrame): The input DataFrame on which quality checks are enforced.

        Returns:
        - pd.DataFrame: DataFrame after the quality checks.
        """
        for k, v in rawdf.items():
            for idx, val in enumerate(v):
                if not pd.isna(val):
                    if isinstance(val, float) or val < 0:
                        rawdf.at[rawdf.index[idx], k] = np.nan
        return rawdf
