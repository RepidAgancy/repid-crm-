"""Creating user changed in model

Revision ID: 8224ba0aed52
Revises: f54f61b05643
Create Date: 2025-02-11 16:16:12.194725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8224ba0aed52'
down_revision: Union[str, None] = 'f54f61b05643'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employees', 'first_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('employees', 'last_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('employees', 'phone_number',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employees', 'phone_number',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('employees', 'last_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('employees', 'first_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    # ### end Alembic commands ###
