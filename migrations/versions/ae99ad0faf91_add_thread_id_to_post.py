"""add thread_id to post

Revision ID: ae99ad0faf91
Revises: c35b9d99d81a
Create Date: 2024-11-30 23:23:44.721418

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'ae99ad0faf91'
down_revision: Union[str, None] = 'c35b9d99d81a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author_id', sa.VARCHAR(length=50), nullable=False))
    op.add_column('post', sa.Column('thread_id', sa.UUID(), nullable=False))
    op.drop_constraint('post_author_fkey', 'post', type_='foreignkey')
    op.create_foreign_key(None, 'post', 'user', ['author_id'], ['ip_address'])
    op.create_foreign_key(None, 'post', 'thread', ['thread_id'], ['id'])
    op.drop_column('post', 'author')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'post',
        sa.Column('author', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    )
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.create_foreign_key(
        'post_author_fkey', 'post', 'user', ['author'], ['ip_address']
    )
    op.drop_column('post', 'thread_id')
    op.drop_column('post', 'author_id')
    # ### end Alembic commands ###