from sqlalchemy import MetaData, Table, Column, Integer, String


meta = MetaData()

cell_data = Table(
    "cell_data", meta,
    Column("year", Integer),
    Column("month", Integer),
    Column("day", Integer),
    Column("cell_identity", String(64)),
    Column("frequency_band", Integer),
    Column("site_id", Integer),
    Column("type", String(64)),
)

sites = Table(
    "sites", meta,
    Column("year", Integer),
    Column("month", Integer),
    Column("day", Integer),
    Column("site_id", Integer),
)
