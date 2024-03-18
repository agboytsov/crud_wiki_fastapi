"""test4

Revision ID: 7eb709456e38
Revises: 583a9e33c05e
Create Date: 2024-03-18 23:16:34.629192

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7eb709456e38'
down_revision: Union[str, None] = '583a9e33c05e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
