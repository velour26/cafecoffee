"""Add delivery fields to orders

Revision ID: 002
Revises: 001
Create Date: 2026-03-27 00:00:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "002"
down_revision: Union[str, None] = "001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("orders", sa.Column("delivery_type", sa.String(length=20), nullable=False, server_default="pickup"))
    op.add_column("orders", sa.Column("delivery_address", sa.Text(), nullable=True))


def downgrade() -> None:
    op.drop_column("orders", "delivery_address")
    op.drop_column("orders", "delivery_type")
