import pandas as pd
import matplotlib.pyplot as plt
from ..pandas_support import Sanitizer


class DataAnalysis:
    """
    DataAnalysis class provides methods to perform basic
    inspections and analysis on pandas DataFrame objects.

    Attributes:
        df (pd.DataFrame): DataFrame that requires analysis.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def initial(self):
        """
        Display a comprehensive initial analysis of the DataFrame including:
        - Top rows of the DataFrame
        - DataFrame info
        - Descriptive statistics
        - Shape of the DataFrame
        - Count of missing values
        - Duplicates and value counts in the DataFrame
        - Duplicates and value counts for each column in the DataFrame
        """

        print("self.df.head(10)")
        print(self.df.head(10))

        print("\nself.df.info()")
        self.df.info()

        print("\nself.df.describe()")
        print(self.df.describe())

        print("\nself.df.shape")
        print(self.df.shape)

        print("\nself.check_na_values()")
        self.check_na_values()

    def plot_distributions(self, column=None):
        """
        Plots the distribution histogram for each column in the DataFrame
        or for a specified column.

        Parameters:
        - column (str, optional): The name of the column to plot.
          If None, all columns are plotted. Default is None.
        """

        if column:
            self.df[column].hist(bins=30, figsize=(8, 6), color='g')
        else:
            self.df.hist(bins=30, figsize=(14, 10), color='g')

        plt.show()

    def check_na_values(self):
        """
        Display the count of missing values for each column in the DataFrame.
        """

        print(self.df.isna().sum())

    def check_na_values_percent_col(self, col: str):
        """
        Display the total count, missing values count, and percentage of missing values
        for a specific column. Also, it checks if the column can be safely dropped based
        on missing values.

        Parameters:
        - col (str): The column name to check for missing values.
        """

        print(f"Total {col} values via df[{col}].shape[0]: {self.df[col].shape[0]}")
        print(f"NaN {col} values via df[{col}].isna().sum(): {self.df[col].isna().sum()}")
        print(f"Percentage of NaN/None {col} values: {(self.df[col].isna().sum() / self.df[col].shape[0]) * 100}")
        Sanitizer.check_if_can_dropna_col(self.df, col)

    def check_dups_and_value_counts(self):
        """
        Display the count of duplicated rows in the DataFrame and the value counts
        for the whole DataFrame.
        """

        print(f"Duplicates for dataframe:")
        print(self.df.duplicated().sum())

        print(f"\nValue Counts for dataframe:")
        print(self.df.value_counts())

    def check_dups_and_value_counts_col(self, col: str):
        """
        Display the count of duplicated values and the value counts for a specific
        column in the DataFrame.

        Parameters:
        - col (str): The column name to check for duplicates and value counts.
        """

        Sanitizer.check_col_exists(self.df, col)

        print(f"Duplicates for column '{col}':")
        print(self.df[col].duplicated().sum())

        print(f"\nValue Counts for column '{col}':")
        print(self.df[col].value_counts())