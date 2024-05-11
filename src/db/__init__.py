import pandas as pd
from sqlalchemy import create_engine
from src.db.models import meta


class DatabaseManager:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = None
        self.init_db_engine()

    def init_db_engine(self):
        self.engine = create_engine(self.db_url, echo=False)

    def build_schema(self):
        meta.create_all(self.engine)

    def clear_schema(self):
        for tn, tbl in meta.tables.items():
            meta.drop_all(self.engine, [tbl], checkfirst=True)

    def write_df_to_db(self, df: pd.DataFrame, table: str):
        df.to_sql(name=table,
                  con=self.engine,
                  if_exists="replace",
                  index=False)