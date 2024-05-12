import pandas as pd
from typing import List

from constants import *


def load_df_from_csv(fp: str) -> pd.DataFrame:
    """
    Loads a DataFrame from a CSV file.

    Args:
        fp (str): The file path to the CSV file.

    Returns:
        pd.DataFrame: The DataFrame loaded from the CSV file.
    """
    df = pd.read_csv(filepath_or_buffer=fp, sep=";")
    return df


def read_file_as_txt(fp: str) -> str:
    """
    Reads the contents of a text file.

    Args:
        fp (str): The file path to the text file.

    Returns:
        str: The contents of the text file.
    """
    with open(fp, "r") as fh:
        contents = fh.read()
    return contents


def load_source_data_as_dfs() -> List[pd.DataFrame]:
    """
    Loads source data from CSV files into DataFrames.

    Returns:
        List[pd.DataFrame]: A list of DataFrames containing source data.
    """
    gsm_df = load_df_from_csv(fp=GSM_FP)
    lte_df = load_df_from_csv(fp=LTE_FP)
    umts_df = load_df_from_csv(fp=UMTS_FP)
    sites_df = load_df_from_csv(fp=SITES_FP)
    return [gsm_df, lte_df, umts_df, sites_df]


def parse_cell_data(gsm_df: pd.DataFrame,
                    lte_df: pd.DataFrame,
                    umts_df: pd.DataFrame) -> pd.DataFrame:
    """
    Parses cell data from multiple DataFrames into a single DataFrame.

    Args:
        gsm_df (pd.DataFrame): DataFrame containing GSM cell data.
        lte_df (pd.DataFrame): DataFrame containing LTE cell data.
        umts_df (pd.DataFrame): DataFrame containing UMTS cell data.

    Returns:
        pd.DataFrame: A DataFrame containing parsed cell data from all input DataFrames.
    """
    gsm_df["type"] = "gsm"
    lte_df["type"] = "lte"
    umts_df["type"] = "umts"

    cell_data_df = pd.concat(objs=[gsm_df, lte_df, umts_df], axis=0)
    return cell_data_df
