"""empty message

Revision ID: 316c3ea526d9
Revises: 30a0e82766b2
Create Date: 2024-02-19 19:44:47.681357

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '316c3ea526d9'
down_revision: Union[str, None] = '30a0e82766b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('login', sa.String(), nullable=False))
    op.create_unique_constraint("user_login_key", 'user', ['login'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("user_login_key", 'user', type_='unique')
    op.drop_column('user', 'login')
    # ### end Alembic commands ###
