from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON)
)

users = Table(
    "users",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("user_first_name", String, nullable=False),
    Column("user_second_name", String, nullable=False),
    Column("user_fathers_name", String, nullable=False),
    Column("user_role_id", Integer, ForeignKey("roles.id")),
    Column("user_password", String, nullable=False),
    Column("user_email", String, nullable=False),
    Column("user_birthday", String, nullable=False),
    Column("user_registered", TIMESTAMP, default=datetime.utcnow)
)
