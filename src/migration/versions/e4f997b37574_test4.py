"""test4

Revision ID: e4f997b37574
Revises: f36b51fd424a
Create Date: 2024-03-18 23:13:53.136406

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4f997b37574'
down_revision: Union[str, None] = 'f36b51fd424a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
