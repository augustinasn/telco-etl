import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@db/{DB_NAME}"
DB_CONNECTION_TIMEOUT = 10

DATA_FP = os.path.join(".", "data")
GSM_FP = os.path.join(DATA_FP, "gsm.csv")
LTE_FP = os.path.join(DATA_FP, "lte.csv")
UMTS_FP = os.path.join(DATA_FP, "umts.csv")
SITES_FP = os.path.join(DATA_FP, "site.csv")

LOGS_FP = os.path.join(".", "logs", "debug.log")

CELLS_PER_FREQUENCY_FOR_SITES_SQL_FP = os.path.join(".", "src", "sql", "cells_per_frequency_for_sites.sql")
CELLS_PER_TECHNOLOGY_FOR_SITES_SQL_FP = os.path.join(".", "src", "sql", "cells_per_technology_for_sites.sql")