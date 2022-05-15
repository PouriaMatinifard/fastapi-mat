"""create a users table

Revision ID: f8bfb282b7d1
Revises: 9d77598bd5fb
Create Date: 2022-04-26 15:30:09.211675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8bfb282b7d1'
down_revision = '9d77598bd5fb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Users',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('email', sa.String, nullable=False),
                    sa.Column('password', sa.String, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('Users')

    pass
