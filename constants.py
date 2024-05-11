import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@db/{DB_NAME}"

DATA_FP = os.path.join("data")
GSM_FP = os.path.join(DATA_FP, "gsm.csv")
LTE_FP = os.path.join(DATA_FP, "lte.csv")
UMNTS_FP = os.path.join(DATA_FP, "umnts.csv")
SITES_FP = os.path.join(DATA_FP, "site.csv")