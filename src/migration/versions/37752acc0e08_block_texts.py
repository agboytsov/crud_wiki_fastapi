"""block_texts

Revision ID: 37752acc0e08
Revises: 3b0ddd38b71b
Create Date: 2024-03-19 15:55:39.956071

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37752acc0e08'
down_revision: Union[str, None] = '3b0ddd38b71b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('block_texts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('block_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=256), nullable=True),
    sa.Column('class_name', sa.String(length=300), nullable=True),
    sa.ForeignKeyConstraint(['block_id'], ['article_content.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('block_texts')
    # ### end Alembic commands ###
