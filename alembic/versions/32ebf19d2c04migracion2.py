"""migracion2

Revision ID: 32ebf19d2c04
Revises: 4a21d0334799
Create Date: 2022-02-03 15:04:25.871943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32ebf19d2c04'
down_revision = '4a21d0334799'
branch_labels = None
depends_on = None


def upgrade():
    (op.add_column('users', sa.Column('profile', sa.Enum("hospital","patient", name="profile_types"), nullable=True)))


def downgrade():
    pass
