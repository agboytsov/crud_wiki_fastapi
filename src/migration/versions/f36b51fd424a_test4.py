"""test4

Revision ID: f36b51fd424a
Revises: c1470a0aaf31
Create Date: 2024-03-18 23:12:00.256898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f36b51fd424a'
down_revision: Union[str, None] = 'c1470a0aaf31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
