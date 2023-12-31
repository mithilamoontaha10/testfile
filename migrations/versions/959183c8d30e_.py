"""empty message

Revision ID: 959183c8d30e
Revises: 66fca7d908e7
Create Date: 2023-08-10 21:50:20.716255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '959183c8d30e'
down_revision = '66fca7d908e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('rating_count', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.drop_column('rating_count')
        batch_op.drop_column('rating')

    # ### end Alembic commands ###
