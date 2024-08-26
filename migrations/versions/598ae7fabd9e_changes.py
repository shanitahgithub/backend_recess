"""changes

Revision ID: 598ae7fabd9e
Revises: 09f07f3f3010
Create Date: 2024-06-29 17:28:15.682520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '598ae7fabd9e'
down_revision = '09f07f3f3010'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
