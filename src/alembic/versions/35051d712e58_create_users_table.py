"""create users table

Revision ID: 35051d712e58
Revises: 688e5a9672f2
Create Date: 2024-01-27 20:37:08.071461

"""

from typing import Sequence, Union

from sqlalchemy import (
    TIMESTAMP,
    UUID,
    Boolean,
    Column,
    ForeignKeyConstraint,
    Integer,
    PrimaryKeyConstraint,
    String,
    UniqueConstraint,
    text,
)
from sqlalchemy.sql.functions import now

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "35051d712e58"
down_revision: Union[str, None] = "688e5a9672f2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    users = op.create_table(
        "users",
        Column("id", Integer, autoincrement=True),
        Column("first_name", String(50)),
        Column("last_name", String(50)),
        Column("email", String(254)),
        Column("profile_picture", String(250)),
        Column("username", String(15)),
        Column("is_active", Boolean, nullable=False, server_default="t"),
        Column("role_id", Integer),
        Column(
            "public_id", UUID, nullable=False, server_default=text("gen_random_uuid()")
        ),
        Column("created_at", TIMESTAMP, nullable=False, server_default=now()),
        Column(
            "updated_at",
            TIMESTAMP,
            nullable=False,
            onupdate=now(),
            server_default=now(),
        ),
        PrimaryKeyConstraint("id", name="user_pk"),
        ForeignKeyConstraint(
            [
                "role_id",
            ],
            [
                "blog.roles.id",
            ],
        ),
        UniqueConstraint("email", "username"),
        UniqueConstraint("public_id"),
        schema="blog",
    )

    op.bulk_insert(
        users,
        [
            {"username": "admin", "role_id": 1},
        ],
    )


def downgrade() -> None:
    op.drop_table("users", schema="blog")
