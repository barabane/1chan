"""rename post author_id

Revision ID: bf553549be8a
Revises: 37ba7bf427e6
Create Date: 2024-12-01 11:54:58.363396

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'bf553549be8a'
down_revision: Union[str, None] = '37ba7bf427e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('user_id', sa.UUID(), nullable=False))
    op.drop_constraint('post_author_id_fkey', 'post', type_='foreignkey')
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    op.drop_column('post', 'author_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'post',
        sa.Column(
            'author_id', sa.VARCHAR(length=50), autoincrement=False, nullable=False
        ),
    )
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.create_foreign_key(
        'post_author_id_fkey', 'post', 'user', ['author_id'], ['ip_address']
    )
    op.drop_column('post', 'user_id')
    # ### end Alembic commands ###