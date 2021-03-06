"""add_similar_components_table

Revision ID: 60b296cac700
Revises: e48c7b4235aa
Create Date: 2016-12-14 08:33:32.920904

"""

# revision identifiers, used by Alembic.
revision = '60b296cac700'
down_revision = 'e48c7b4235aa'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('similar_components',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fromcomponent', sa.Text(), nullable=False),
    sa.Column('tocomponent', sa.Text(), nullable=False),
    sa.Column('similarity_distance', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('fromcomponent', 'tocomponent', name='sim_comps')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('similar_components')
    # ### end Alembic commands ###
