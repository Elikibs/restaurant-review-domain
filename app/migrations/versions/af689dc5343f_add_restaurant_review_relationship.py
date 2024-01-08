"""Add Restaurant-Review relationship

Revision ID: af689dc5343f
Revises: 724f6a544602
Create Date: 2024-01-08 17:01:10.339884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af689dc5343f'
down_revision = '724f6a544602'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('restaurant_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_restaurant_id_restaurants'), 'reviews', 'restaurants', ['restaurant_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_restaurant_id_restaurants'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'restaurant_id')
    # ### end Alembic commands ###