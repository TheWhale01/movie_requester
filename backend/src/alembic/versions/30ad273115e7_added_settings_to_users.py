"""Added settings to users

Revision ID: 30ad273115e7
Revises: a3f9a4219eb0
Create Date: 2024-01-08 16:24:32.353779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30ad273115e7'
down_revision: Union[str, None] = 'a3f9a4219eb0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('requests_tmdb_id_key', 'requests', type_='unique')
    op.create_index(op.f('ix_requests_tmdb_id'), 'requests', ['tmdb_id'], unique=True)
    op.add_column('telegram_settings', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'telegram_settings', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'telegram_settings', type_='foreignkey')
    op.drop_column('telegram_settings', 'user_id')
    op.drop_index(op.f('ix_requests_tmdb_id'), table_name='requests')
    op.create_unique_constraint('requests_tmdb_id_key', 'requests', ['tmdb_id'])
    # ### end Alembic commands ###
