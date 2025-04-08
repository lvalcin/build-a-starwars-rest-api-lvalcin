"""empty message

Revision ID: 051e29a1b421
Revises: 65fd237db24b
Create Date: 2025-04-07 22:57:23.376729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '051e29a1b421'
down_revision = '65fd237db24b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###
