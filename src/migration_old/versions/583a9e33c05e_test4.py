"""test4

Revision ID: 583a9e33c05e
Revises: be4793266efb
Create Date: 2024-03-18 23:15:00.667272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '583a9e33c05e'
down_revision: Union[str, None] = 'be4793266efb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
