"""test3

Revision ID: af64ad9be125
Revises: a33bcfb16a3d
Create Date: 2024-03-18 23:10:22.998834

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af64ad9be125'
down_revision: Union[str, None] = 'a33bcfb16a3d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
