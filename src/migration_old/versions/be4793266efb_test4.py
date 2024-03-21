"""test4

Revision ID: be4793266efb
Revises: e4f997b37574
Create Date: 2024-03-18 23:14:21.958769

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be4793266efb'
down_revision: Union[str, None] = 'e4f997b37574'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
