"""nueva

Revision ID: 8a110c0e4c5f
Revises: bf410ede83a7
Create Date: 2022-02-03 15:54:54.939431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a110c0e4c5f'
down_revision = 'bf410ede83a7'
branch_labels = None
depends_on = None


def upgrade():
    (op.add_column('users', sa.Column('profile', sa.Enum("hospital","patient", name="profile_types"), nullable=True)))


def downgrade():
    pass
