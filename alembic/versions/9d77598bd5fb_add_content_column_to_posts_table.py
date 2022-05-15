"""add content column to posts table

Revision ID: 9d77598bd5fb
Revises: b823fb7c50df
Create Date: 2022-04-26 15:24:45.798047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d77598bd5fb'
down_revision = 'b823fb7c50df'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))

    pass


def downgrade():
    op.drop('posts', 'content')

    pass
