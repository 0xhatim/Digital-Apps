"""empty message

Revision ID: 7e234c60d55b
Revises: 2f0b99542cdc
Create Date: 2022-08-19 02:00:30.899779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e234c60d55b'
down_revision = '2f0b99542cdc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offers_owner2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_name', sa.String(length=120), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('owner_username', sa.String(length=80), nullable=True),
    sa.Column('price', sa.String(length=80), nullable=True),
    sa.Column('ip_active', sa.Integer(), nullable=True),
    sa.Column('app_desribe', sa.String(length=400), nullable=False),
    sa.Column('month', sa.Boolean(), nullable=True),
    sa.Column('image_file', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('offers_owner')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offers_owner',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('app_name', sa.VARCHAR(length=120), nullable=True),
    sa.Column('username', sa.VARCHAR(length=80), nullable=True),
    sa.Column('owner_username', sa.VARCHAR(length=80), nullable=True),
    sa.Column('price', sa.VARCHAR(length=80), nullable=True),
    sa.Column('ip_active', sa.INTEGER(), nullable=True),
    sa.Column('app_desribe', sa.VARCHAR(length=400), nullable=False),
    sa.Column('month', sa.BOOLEAN(), nullable=True),
    sa.CheckConstraint('month IN (0, 1)'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('offers_owner2')
    # ### end Alembic commands ###
