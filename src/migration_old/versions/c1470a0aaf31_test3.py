"""test3

Revision ID: c1470a0aaf31
Revises: af64ad9be125
Create Date: 2024-03-18 23:10:56.567861

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1470a0aaf31'
down_revision: Union[str, None] = 'af64ad9be125'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
