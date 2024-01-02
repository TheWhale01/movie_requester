"""empty message

Revision ID: 282f8ded7d66
Revises: a5fed46443dd
Create Date: 2024-01-02 06:50:47.586616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '282f8ded7d66'
down_revision: Union[str, None] = 'a5fed46443dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
