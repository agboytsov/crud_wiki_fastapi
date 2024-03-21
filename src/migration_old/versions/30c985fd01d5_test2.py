"""test2

Revision ID: 30c985fd01d5
Revises: 06898c57d70c
Create Date: 2024-03-18 23:00:51.571141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30c985fd01d5'
down_revision: Union[str, None] = '06898c57d70c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
