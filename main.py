from constants import *

from src.logger import set_up_logger
from src.db import DatabaseManager
from src.transformation import load_source_data_as_dfs, parse_cell_data


if __name__ == "__main__":
    # Set-up logging:
    logger = set_up_logger()

    # Set up DB:
    db = DatabaseManager(db_url=DB_URL)
    db.build_schema()
    logger.info("Database set-up successful.")

    # Transform data:
    gsm_df, lte_df, umts_df, sites_df = load_source_data_as_dfs()
    cell_data_df = parse_cell_data(gsm_df, lte_df, umts_df)

    logger.info(f"Data extraction & transformation successful.")
    logger.info(cell_data_df.head())

    # Load data:
    db.write_df_to_db(df=cell_data_df,
                      table="cell_data")
    db.write_df_to_db(df=sites_df,
                      table="sites")
    logger.info(f"Source data loaded to the database successfully.")

    # Create views:
    db.create_view_from_sql_file(name="cells_per_frequency_for_sites",
                                 fp=CELLS_PER_FREQUENCY_FOR_SITES_SQL_FP)
    db.create_view_from_sql_file(name="cells_per_technology_for_sites",
                                 fp=CELLS_PER_TECHNOLOGY_FOR_SITES_SQL_FP)
    logger.info(f"Analytical views created successfully.")
