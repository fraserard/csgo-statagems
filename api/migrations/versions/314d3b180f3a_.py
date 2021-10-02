"""empty message

Revision ID: 314d3b180f3a
Revises: 59ae2d8baf0a
Create Date: 2021-09-01 21:47:03.057142

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '314d3b180f3a'
down_revision = '59ae2d8baf0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('group_player', 'group_clearance',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('group_player', 'group_clearance',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
