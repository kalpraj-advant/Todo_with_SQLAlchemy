"""add_user_id_to_todos

Revision ID: 3fd411193971
Revises: 34fccb83eee3
Create Date: 2025-05-28 15:11:44.242218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fd411193971'
down_revision: Union[str, None] = '34fccb83eee3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = [col['name'] for col in inspector.get_columns('todos')]
    if 'user_id' not in columns:
        with op.batch_alter_table('todos', schema=None) as batch_op:
            batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
            batch_op.create_foreign_key('fk_todos_user_id_users', 'users', ['user_id'], ['id'])


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.drop_constraint('fk_todos_user_id_users', type_='foreignkey')
        batch_op.drop_column('user_id')
