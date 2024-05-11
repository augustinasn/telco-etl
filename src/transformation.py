import pandas as pd
from typing import List

from constants import *


def load_df_from_csv(fp: str) -> pd.DataFrame:
    df = pd.read_csv(filepath_or_buffer=fp,
                     sep=";")
    return df


def read_file_as_txt(fp: str) -> str:
    with open(fp, "r") as fh:
        contents = fh.read()
    return contents


def load_source_data_as_dfs() -> List[pd.DataFrame]:
    gsm_df = load_df_from_csv(fp=GSM_FP)
    lte_df = load_df_from_csv(fp=LTE_FP)
    umts_df = load_df_from_csv(fp=UMTS_FP)
    sites_df = load_df_from_csv(fp=SITES_FP)
    return [gsm_df, lte_df, umts_df, sites_df]


def parse_cell_data(gsm_df: pd.DataFrame,
                    lte_df: pd.DataFrame,
                    umts_df: pd.DataFrame) -> pd.DataFrame:
    gsm_df["type"] = "gsm"
    lte_df["type"] = "lte"
    umts_df["type"] = "umts"

    cell_data_df = pd.concat(objs=[gsm_df, lte_df, umts_df], axis=0)
    return cell_data_df
