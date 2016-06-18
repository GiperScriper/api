"""empty message

Revision ID: 41fc015bc30c
Revises: 890f0f2ba1d1
Create Date: 2016-06-17 14:47:11.944599

"""

# revision identifiers, used by Alembic.
revision = '41fc015bc30c'
down_revision = '890f0f2ba1d1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('new_field', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'new_field')
    ### end Alembic commands ###