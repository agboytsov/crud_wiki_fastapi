"""test5

Revision ID: ca7532c2241f
Revises: 79acf1559d7a
Create Date: 2024-03-18 23:18:29.765526

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca7532c2241f'
down_revision: Union[str, None] = '79acf1559d7a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=2000), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article_content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('block_model', sa.String(), nullable=False),
    sa.Column('block_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article_content')
    op.drop_table('articles')
    # ### end Alembic commands ###
