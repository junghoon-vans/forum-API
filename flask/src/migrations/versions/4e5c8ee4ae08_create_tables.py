"""create tables

Revision ID: 4e5c8ee4ae08
Revises: 3c7620131de9
Create Date: 2020-03-27 03:37:56.540768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e5c8ee4ae08'
down_revision = '3c7620131de9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('master', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['master'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('board', sa.Integer(), nullable=True),
    sa.Column('writer', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('pub_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['board'], ['board.id'], ),
    sa.ForeignKeyConstraint(['writer'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('user_fullname_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_fullname_key', 'user', ['fullname'])
    op.drop_table('article')
    op.drop_table('board')
    # ### end Alembic commands ###