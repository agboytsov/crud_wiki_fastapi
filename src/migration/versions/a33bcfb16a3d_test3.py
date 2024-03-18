"""test3

Revision ID: a33bcfb16a3d
Revises: 431553d8722d
Create Date: 2024-03-18 23:09:53.314411

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a33bcfb16a3d'
down_revision: Union[str, None] = '431553d8722d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
