"""test2

Revision ID: 5cf604fabe9a
Revises: 70cbf2ba14f9
Create Date: 2024-03-18 22:43:51.777873

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5cf604fabe9a'
down_revision: Union[str, None] = '70cbf2ba14f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
