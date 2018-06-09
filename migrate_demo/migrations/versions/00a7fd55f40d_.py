"""empty message

Revision ID: 00a7fd55f40d
Revises: a6b24ccd6122
Create Date: 2018-06-07 18:34:20.367705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00a7fd55f40d'
down_revision = 'a6b24ccd6122'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('tags', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'tags')
    # ### end Alembic commands ###