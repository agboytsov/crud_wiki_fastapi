"""test2

Revision ID: 06898c57d70c
Revises: 5cf604fabe9a
Create Date: 2024-03-18 22:47:33.219740

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06898c57d70c'
down_revision: Union[str, None] = '5cf604fabe9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
