"""chang

Revision ID: 628cacc72a68
Revises: 677bceebff2b
Create Date: 2018-03-08 00:52:52.802169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '628cacc72a68'
down_revision = '677bceebff2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_role_id_fkey', 'users', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('users_role_id_fkey', 'users', 'roles', ['role_id'], ['id'])
    # ### end Alembic commands ###