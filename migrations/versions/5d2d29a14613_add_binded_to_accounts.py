"""add binded to accounts

Revision ID: 5d2d29a14613
Revises: 24fad7bbfc10
Create Date: 2017-11-01 06:00:59.782456

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5d2d29a14613'
down_revision = '24fad7bbfc10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('binded', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_accounts_binded'), 'accounts', ['binded'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_accounts_binded'), table_name='accounts')
    op.drop_column('accounts', 'binded')
    # ### end Alembic commands ###
