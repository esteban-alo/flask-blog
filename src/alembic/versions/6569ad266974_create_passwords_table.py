"""create passwords table

Revision ID: 6569ad266974
Revises: ec7b9219a02d
Create Date: 2024-01-27 20:37:25.090991

"""

from typing import Sequence, Union

from sqlalchemy import (
    TIMESTAMP,
    Column,
    ForeignKeyConstraint,
    Integer,
    PrimaryKeyConstraint,
    String,
)
from sqlalchemy.sql.functions import now

from alembic import op
from src.utils.helpers import generate_salt, hash_password

# revision identifiers, used by Alembic.
revision: str = "6569ad266974"
down_revision: Union[str, None] = "ec7b9219a02d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

SALT = generate_salt()
HASHED_PASSWORD = hash_password(password="admin", salt=SALT)


def upgrade() -> None:
    passwords = op.create_table(
        "passwords",
        Column("id", Integer, autoincrement=True),
        Column("password", String(140)),
        Column("salt", String(40)),
        Column("user_id", Integer),
        Column("created_at", TIMESTAMP, nullable=False, server_default=now()),
        Column(
            "updated_at",
            TIMESTAMP,
            nullable=False,
            onupdate=now(),
            server_default=now(),
        ),
        PrimaryKeyConstraint("id", name="password_pk"),
        ForeignKeyConstraint(
            [
                "user_id",
            ],
            [
                "blog.users.id",
            ],
            onupdate="CASCADE",
            ondelete="SET NULL",
        ),
        schema="blog",
    )

    op.bulk_insert(
        passwords,
        [
            {"password": HASHED_PASSWORD, "salt": SALT, "user_id": 1},
        ],
    )


def downgrade() -> None:
    op.drop_table("passwords", schema="blog")
