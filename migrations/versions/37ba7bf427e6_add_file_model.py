"""add file model

Revision ID: 37ba7bf427e6
Revises: ae99ad0faf91
Create Date: 2024-12-01 10:52:35.424995

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '37ba7bf427e6'
down_revision: Union[str, None] = 'ae99ad0faf91'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'file',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('link', sa.String(), nullable=False),
        sa.Column('size', sa.FLOAT(), nullable=False),
        sa.Column(
            'created_at',
            postgresql.TIMESTAMP(),
            server_default=sa.text('now()'),
            nullable=False,
        ),
        sa.Column('width', sa.Integer(), nullable=True),
        sa.Column('height', sa.Integer(), nullable=True),
        sa.Column('post_id', sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ['post_id'],
            ['post.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('link'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file')
    # ### end Alembic commands ###