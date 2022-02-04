"""hospital and patient

Revision ID: d4122930bf09
Revises: 8a110c0e4c5f
Create Date: 2022-02-04 02:48:32.894634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4122930bf09'
down_revision = '8a110c0e4c5f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'hospital_users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('address', sa.String),
        sa.Column('medical_services', sa.String),
        sa.Column('user_id', sa.String, sa.ForeignKey("users.id")),
    )
    op.create_table(
        'patients',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('address', sa.String),
        sa.Column('date_of_birth', sa.Date),
        sa.Column('user_id', sa.String, sa.ForeignKey("users.id")),
    )



def downgrade():
    op.drop_table('profile')
