"""test running migrations

Revision ID: 6b2d7be8deb7
Revises: dd9ea73d039b
Create Date: 2025-02-17 16:41:15.185359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b2d7be8deb7'
down_revision: Union[str, None] = 'dd9ea73d039b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
