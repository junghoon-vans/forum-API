"""Modify Article model

Revision ID: f833287f558d
Revises: c8bcbcd45709
Create Date: 2020-03-19 19:34:09.216277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f833287f558d'
down_revision = 'c8bcbcd45709'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('article_board_fkey', 'article', type_='foreignkey')
    op.drop_column('article', 'board')
    op.add_column('board', sa.Column('articles', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'board', 'article', ['articles'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'board', type_='foreignkey')
    op.drop_column('board', 'articles')
    op.add_column('article', sa.Column('board', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_foreign_key('article_board_fkey', 'article', 'board', ['board'], ['name'])
    # ### end Alembic commands ###