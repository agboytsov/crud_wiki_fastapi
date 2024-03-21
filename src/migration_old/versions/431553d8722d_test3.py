"""test3

Revision ID: 431553d8722d
Revises: 8e89ff3e8b53
Create Date: 2024-03-18 23:09:29.604880

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '431553d8722d'
down_revision: Union[str, None] = '8e89ff3e8b53'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
