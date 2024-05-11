from constants import *
from src.db import DatabaseManager

if __name__ == "__main__":
    # Set-up logging:

    # Set up DB:
    db = DatabaseManager(db_url=DB_URL)
    db.build_schema()
