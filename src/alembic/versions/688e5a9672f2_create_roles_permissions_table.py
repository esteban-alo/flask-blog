"""create roles permissions table

Revision ID: 688e5a9672f2
Revises: fba5839c9c4c
Create Date: 2024-01-27 20:36:58.393779

"""

from typing import Sequence, Union

from sqlalchemy import (
    TIMESTAMP,
    Column,
    ForeignKeyConstraint,
    Integer,
    PrimaryKeyConstraint,
    UniqueConstraint,
)
from sqlalchemy.sql.functions import now

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "688e5a9672f2"
down_revision: Union[str, None] = "fba5839c9c4c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    roles_permissions = op.create_table(
        "roles_permissions",
        Column("id", Integer, autoincrement=True),
        Column("role_id", Integer),
        Column("permission_id", Integer),
        Column("created_at", TIMESTAMP, nullable=False, server_default=now()),
        Column(
            "updated_at",
            TIMESTAMP,
            nullable=False,
            onupdate=now(),
            server_default=now(),
        ),
        PrimaryKeyConstraint("id", name="role_permission_pk"),
        ForeignKeyConstraint(
            [
                "role_id",
            ],
            [
                "blog.roles.id",
            ],
            onupdate="CASCADE",
            ondelete="SET NULL",
        ),
        ForeignKeyConstraint(
            [
                "permission_id",
            ],
            [
                "blog.permissions.id",
            ],
            onupdate="CASCADE",
            ondelete="SET NULL",
        ),
        UniqueConstraint("role_id", "permission_id"),
        schema="blog",
    )

    op.bulk_insert(
        roles_permissions,
        [
            {"role_id": 1, "permission_id": 1},
            {"role_id": 1, "permission_id": 2},
            {"role_id": 1, "permission_id": 3},
            {"role_id": 1, "permission_id": 4},
            {"role_id": 1, "permission_id": 5},
            {"role_id": 1, "permission_id": 6},
            {"role_id": 1, "permission_id": 7},
        ],
    )


def downgrade() -> None:
    op.drop_table("roles_permissions", schema="blog")
