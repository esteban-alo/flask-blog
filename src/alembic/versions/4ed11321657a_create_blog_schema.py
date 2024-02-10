"""create blog schema

Revision ID: 4ed11321657a
Revises: 
Create Date: 2024-01-27 19:53:58.506211

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4ed11321657a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA blog")


def downgrade() -> None:
    op.execute("DROP SCHEMA blog")
