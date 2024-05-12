import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.schema import DDL

from src.db.models import meta
from src.transformation import read_file_as_txt

from constants import *

class DatabaseManager:
    """
    A class for managing interactions with a SQL database.
    """

    def __init__(self, db_url: str):
        """
        Initializes the DatabaseManager instance.

        Args:
            db_url (str): The URL to connect to the database.
        """
        self.db_url = db_url
        self.engine = None
        self.init_db_engine()

    def init_db_engine(self):
        """
        Initializes the database engine.
        """
        self.engine = create_engine(self.db_url, echo=False)

    def build_schema(self):
        """
        Builds the schema defined in the database metadata.
        """
        meta.create_all(self.engine)

    def write_df_to_db(self, df: pd.DataFrame, table: str):
        """
        Writes a DataFrame to the specified database table.

        Args:
            df (pd.DataFrame): The DataFrame to be written to the database.
            table (str): The name of the database table.

        Note:
            This method appends the DataFrame to the existing table if it already exists.
        """
        df.to_sql(name=table, con=self.engine, if_exists="append", index=False)

    def execute_raw_query(self, query: str):
        """
        Executes a raw SQL query.

        Args:
            query (str): The SQL query to be executed.
        """
        with self.engine.connect() as con:
            con.execute(query)
            con.commit()

    def create_view_from_sql_file(self, name: str, fp: str):
        """
        Creates a database view from an SQL file.

        Args:
            name (str): The name of the view to be created.
            fp (str): The file path to the SQL file containing the view definition.

        Note:
            The SQL file should contain only the SELECT statement defining the view.
        """
        query = read_file_as_txt(fp)
        query = f"CREATE OR REPLACE VIEW {name} AS {query}"
        ddl = DDL(query)
        self.execute_raw_query(ddl)
