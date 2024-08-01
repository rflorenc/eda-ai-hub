import pandas as pd
from ..pandas_support import Sanitizer


class DataAnalysis:
    """
    DataAnalysis class just outputs values without replacing or returning objects
    """
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def check_missing_values(self):
        print(self.df.isna().sum())

    def check_dups_and_value_counts(self):
        print(f"Duplicates for dataframe:")
        print(self.df.duplicated().sum())

        print(f"\nValue Counts for dataframe:")
        print(self.df.value_counts())

    def check_dups_and_value_counts_col(self, col: str):
        Sanitizer.check_col_exists(self.df, col)

        print(f"Duplicates for column '{col}':")
        print(self.df[col].duplicated().sum())

        print(f"\nValue Counts for column '{col}':")
        print(self.df[col].value_counts())
