"""test4

Revision ID: 79acf1559d7a
Revises: 7eb709456e38
Create Date: 2024-03-18 23:17:47.818178

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79acf1559d7a'
down_revision: Union[str, None] = '7eb709456e38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
