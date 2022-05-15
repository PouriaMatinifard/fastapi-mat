"""create posts table

Revision ID: b823fb7c50df
Revises: 
Create Date: 2022-04-26 15:03:45.516833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b823fb7c50df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_table('posts')

    pass
