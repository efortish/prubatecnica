"""primera migracion

Revision ID: 4a21d0334799
Revises: 
Create Date: 2022-02-03 13:49:04.795893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a21d0334799'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('profile', sa.String))


def downgrade():
    pass
