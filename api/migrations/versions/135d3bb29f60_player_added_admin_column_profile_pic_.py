"""player: added admin column, profile pic hash column, removed profile url column, fixed updated_at column

Revision ID: 135d3bb29f60
Revises: 0e9142485b6c
Create Date: 2021-07-29 12:52:42.079783

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '135d3bb29f60'
down_revision = '0e9142485b6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player', sa.Column('avatar_hash', sa.String(length=64), nullable=False))
    op.add_column('player', sa.Column('is_admin', sa.Boolean(), server_default=sa.text('False'), nullable=False))
    op.drop_column('player', 'profile_pic_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player', sa.Column('profile_pic_url', mysql.TEXT(), nullable=False))
    op.drop_column('player', 'is_admin')
    op.drop_column('player', 'avatar_hash')
    # ### end Alembic commands ###
