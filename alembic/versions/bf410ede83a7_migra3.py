"""migra3

Revision ID: bf410ede83a7
Revises: 32ebf19d2c04
Create Date: 2022-02-03 15:30:25.076087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf410ede83a7'
down_revision = '32ebf19d2c04'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('profile', sa.Enum("hospital","patient", name="profile"), nullable=True))


def downgrade():
    pass
