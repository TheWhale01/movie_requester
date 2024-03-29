"""Added notes to requests

Revision ID: 52dd5fafc70b
Revises: b1feb62ce336
Create Date: 2024-01-22 15:13:59.207307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52dd5fafc70b'
down_revision: Union[str, None] = 'b1feb62ce336'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('note', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('requests', 'note')
    # ### end Alembic commands ###
