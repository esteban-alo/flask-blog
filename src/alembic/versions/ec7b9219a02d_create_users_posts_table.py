"""create users posts table

Revision ID: ec7b9219a02d
Revises: 35051d712e58
Create Date: 2024-01-27 20:37:13.560552

"""

from typing import Sequence, Union

from sqlalchemy import (
    ARRAY,
    TIMESTAMP,
    UUID,
    Column,
    ForeignKeyConstraint,
    Integer,
    PrimaryKeyConstraint,
    UniqueConstraint,
)
from sqlalchemy.sql.functions import now

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ec7b9219a02d"
down_revision: Union[str, None] = "35051d712e58"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users_posts",
        Column("id", Integer, autoincrement=True),
        Column("user_id", Integer),
        Column("post_id", Integer),
        Column("likes", ARRAY(UUID)),
        Column("created_at", TIMESTAMP, nullable=False, server_default=now()),
        Column(
            "updated_at",
            TIMESTAMP,
            nullable=False,
            onupdate=now(),
            server_default=now(),
        ),
        PrimaryKeyConstraint("id", name="user_post_pk"),
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
        ForeignKeyConstraint(
            [
                "post_id",
            ],
            [
                "blog.posts.id",
            ],
            onupdate="CASCADE",
            ondelete="SET NULL",
        ),
        UniqueConstraint("user_id", "post_id"),
        schema="blog",
    )


def downgrade() -> None:
    op.drop_table("users_posts", schema="blog")
