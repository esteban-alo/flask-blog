"""create permissions table

Revision ID: 3369ccfe28e6
Revises: 12034b970cd7
Create Date: 2024-01-27 20:36:22.670901

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
revision: str = "3369ccfe28e6"
down_revision: Union[str, None] = "12034b970cd7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    permissions = op.create_table(
        "permissions",
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
        PrimaryKeyConstraint("id", name="permission_pk"),
        UniqueConstraint("name"),
        UniqueConstraint("public_id"),
        schema="blog",
    )

    op.bulk_insert(
        permissions,
        [
            {"id": 1, "name": "create"},
            {"id": 2, "name": "read"},
            {"id": 3, "name": "write"},
            {"id": 4, "name": "update"},
            {"id": 5, "name": "delete"},
            {"id": 6, "name": "enable"},
            {"id": 7, "name": "disable"},
        ],
    )


def downgrade() -> None:
    op.drop_table("permissions", schema="blog")
