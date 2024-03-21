"""test2

Revision ID: f5b5189d4f3c
Revises: 30c985fd01d5
Create Date: 2024-03-18 23:03:44.803948

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5b5189d4f3c'
down_revision: Union[str, None] = '30c985fd01d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
