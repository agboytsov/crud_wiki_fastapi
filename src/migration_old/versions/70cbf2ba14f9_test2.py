"""test2

Revision ID: 70cbf2ba14f9
Revises: f72b5b472759
Create Date: 2024-03-18 22:42:29.434089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70cbf2ba14f9'
down_revision: Union[str, None] = 'f72b5b472759'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
