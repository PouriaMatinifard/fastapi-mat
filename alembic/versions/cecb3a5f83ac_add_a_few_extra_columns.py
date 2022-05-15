"""add a few extra columns

Revision ID: cecb3a5f83ac
Revises: 211255223607
Create Date: 2022-04-27 13:30:42.582555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cecb3a5f83ac'
down_revision = '211255223607'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published',
                                     sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at',
                                     sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')

    pass
