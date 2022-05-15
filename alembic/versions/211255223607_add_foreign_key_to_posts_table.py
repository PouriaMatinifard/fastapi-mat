"""add foreign-key to posts table

Revision ID: 211255223607
Revises: f8bfb282b7d1
Create Date: 2022-04-26 15:35:28.506017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '211255223607'
down_revision = 'f8bfb282b7d1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='Users',
                          local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', "owner_id")
    pass
