"""test2

Revision ID: 2a13fff87e0f
Revises: f5b5189d4f3c
Create Date: 2024-03-18 23:05:44.966920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a13fff87e0f'
down_revision: Union[str, None] = 'f5b5189d4f3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
