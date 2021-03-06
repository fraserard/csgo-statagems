"""empty message

Revision ID: 478f870e38e0
Revises: 314d3b180f3a
Create Date: 2021-09-01 21:58:00.878445

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '478f870e38e0'
down_revision = '314d3b180f3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('group_player', 'group_clearance',
               existing_type=mysql.INTEGER(),
               nullable=False,
               default=5)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('group_player', 'group_clearance',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
