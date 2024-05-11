import pandas as pd
from sqlalchemy import create_engine
from src.db.models import meta
from src.transformation import read_file_as_txt

from constants import *

class DatabaseManager:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = None
        self.init_db_engine()

    def init_db_engine(self):
        self.engine = create_engine(self.db_url,
                                    echo=False)

    def build_schema(self):
        meta.create_all(self.engine)

    def write_df_to_db(self, df: pd.DataFrame, table: str):
        df.to_sql(name=table,
                  con=self.engine,
                  if_exists="append",
                  index=False)

    def execute_raw_query(self, query: str):
        with self.engine.connect() as con:
            con.execute(query)

    def create_view_from_sql_file(self, name, fp):
        query = read_file_as_txt(fp)
        query = f"CREATE OR REPLACE VIEW {name} AS {query};"
        self.execute_raw_query(query)
