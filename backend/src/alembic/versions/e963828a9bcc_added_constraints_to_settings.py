"""Added constraints to settings

Revision ID: e963828a9bcc
Revises: 30ad273115e7
Create Date: 2024-01-08 16:27:12.056702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e963828a9bcc'
down_revision: Union[str, None] = '30ad273115e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('telegram_settings', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index(op.f('ix_telegram_settings_user_id'), 'telegram_settings', ['user_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_telegram_settings_user_id'), table_name='telegram_settings')
    op.alter_column('telegram_settings', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
