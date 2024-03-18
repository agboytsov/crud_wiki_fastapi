"""test3

Revision ID: 8e89ff3e8b53
Revises: 2a13fff87e0f
Create Date: 2024-03-18 23:08:46.655446

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e89ff3e8b53'
down_revision: Union[str, None] = '2a13fff87e0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
