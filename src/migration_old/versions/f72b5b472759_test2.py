"""test2

Revision ID: f72b5b472759
Revises: 4c43bab7e597
Create Date: 2024-03-18 22:40:21.290752

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f72b5b472759'
down_revision: Union[str, None] = '4c43bab7e597'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
