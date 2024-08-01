import pandas as pd
from dataclasses import dataclass

@dataclass
class Sanitizer:
    """
    A utility class providing methods to sanitize and inspect DataFrames for null values.
    """

    @staticmethod
    def check_null_values_percent(rawdf: pd.DataFrame) -> pd.DataFrame:
        """
        Compute the percentage of null values for each column in the DataFrame.

        Parameters:
        - rawdf (pd.DataFrame): The input DataFrame.

        Returns:
        - pd.DataFrame: A DataFrame with columns showing the number of null values and their percentage for each column.
        """

        nulls_percent_df = pd.DataFrame({'Null Values': rawdf.isna().sum(),
                                         'Percentage Null Values': (rawdf.isna().sum()) / (len(rawdf)) * 100})
        return nulls_percent_df

    @staticmethod
    def check_if_can_dropna_col(rawdf: pd.DataFrame, col: str, percent=75) -> bool:
        """
        Check if a column can be safely dropped based on the percentage of null values.

        Parameters:
        - rawdf (pd.DataFrame): The input DataFrame.
        - col (str): The column name to check.
        - percent (int, default=75): The threshold percentage. If the percentage of null values in the column is
                                     greater than this value, the column can generally be dropped.

        Returns:
        - bool: True if the column can be dropped, False otherwise.

        """

        if not (0 <= percent <= 100):
            raise ValueError("Percent must be between 0 and 100.")

        null_percent = (rawdf[col].isna().sum() / len(rawdf[col])) * 100
        if null_percent < percent:
            print(f"Cannot dropna for column {col} as it has less than {percent}% missing values.")
        else:
            print(f"It is generally OK to dropna for column {col}.")
        return null_percent >= percent

    @staticmethod
    def check_col_exists(rawdf: pd.DataFrame, col: str):
        """
        Check if a column exists in the DataFrame.

        Parameters:
        - rawdf (pd.DataFrame): The input DataFrame.
        - col (str): The column name to check.

        """

        if col == "":
            raise ValueError("Column name must not be an empty string.")
        elif col not in rawdf.columns:
            raise KeyError(f"Column '{col}' does not exist in DataFrame.")

    @staticmethod
    def check_null_values(rawdf: pd.DataFrame) -> pd.DataFrame:
        """
        Compute the number of null values for each column in the DataFrame.

        Parameters:
        - rawdf (pd.DataFrame): The input DataFrame.

        Returns:
        - pd.DataFrame: A DataFrame showing the number of null values for each column.
        """

        nulls_df = pd.DataFrame({'Null Values': rawdf.isna().sum()})
        return nulls_df
