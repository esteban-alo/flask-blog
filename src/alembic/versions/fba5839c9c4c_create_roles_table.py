"""create roles table

Revision ID: fba5839c9c4c
Revises: 3369ccfe28e6
Create Date: 2024-01-27 20:36:33.670577

"""

from typing import Sequence, Union

from sqlalchemy import (
    TIMESTAMP,
    UUID,
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    UniqueConstraint,
    text,
)
from sqlalchemy.sql.functions import now

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "fba5839c9c4c"
down_revision: Union[str, None] = "3369ccfe28e6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    roles = op.create_table(
        "roles",
        Column("id", Integer, autoincrement=True),
        Column("name", String(50)),
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
        PrimaryKeyConstraint("id", name="role_pk"),
        UniqueConstraint("name"),
        UniqueConstraint("public_id"),
        schema="blog",
    )

    op.bulk_insert(
        roles,
        [
            {"id": 1, "name": "admin"},
            {"id": 2, "name": "editor"},
            {"id": 3, "name": "user"},
        ],
    )


def downgrade() -> None:
    op.drop_table("roles", schema="blog")
