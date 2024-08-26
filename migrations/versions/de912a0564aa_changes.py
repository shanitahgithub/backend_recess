"""changes

Revision ID: de912a0564aa
Revises: 5ab1d49c5560
Create Date: 2024-07-03 23:14:43.672232

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'de912a0564aa'
down_revision = '5ab1d49c5560'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
        batch_op.drop_constraint('reviews_ibfk_1', type_='foreignkey')
        batch_op.drop_constraint('reviews_ibfk_2', type_='foreignkey')
        batch_op.drop_column('order_id')
        batch_op.drop_column('tick')
        batch_op.drop_column('restaurant_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('restaurant_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('tick', mysql.VARCHAR(length=100), nullable=True))
        batch_op.add_column(sa.Column('order_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('reviews_ibfk_2', 'restaurant', ['restaurant_id'], ['id'])
        batch_op.create_foreign_key('reviews_ibfk_1', 'orders', ['order_id'], ['id'])
        batch_op.alter_column('user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)

    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
