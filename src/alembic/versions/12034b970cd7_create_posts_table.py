"""create posts table

Revision ID: 12034b970cd7
Revises: 4ed11321657a
Create Date: 2024-01-27 20:36:16.175649

"""

from typing import Sequence, Union

from sqlalchemy import (
    ARRAY,
    TIMESTAMP,
    UUID,
    Boolean,
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
    Text,
    UniqueConstraint,
    text,
)
from sqlalchemy.sql.functions import now

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "12034b970cd7"
down_revision: Union[str, None] = "4ed11321657a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        Column("id", Integer, autoincrement=True),
        Column("title", String(256)),
        Column("text", Text),
        Column("tags", ARRAY(String(25))),
        Column("url_path", String(256)),
        Column("enabled", Boolean, default=False),
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
        PrimaryKeyConstraint("id", name="post_pk"),
        UniqueConstraint("title"),
        UniqueConstraint("public_id"),
        schema="blog",
    )


def downgrade() -> None:
    op.drop_table("posts", schema="blog")
