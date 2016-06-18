"""empty message

Revision ID: 0325b31025de
Revises: d2c62a51503a
Create Date: 2016-06-17 14:58:59.208185

"""

# revision identifiers, used by Alembic.
revision = '0325b31025de'
down_revision = 'd2c62a51503a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password_hash')
    ### end Alembic commands ###