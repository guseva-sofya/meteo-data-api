"""create_temperatures_table

Revision ID: bfc353d6d95f
Revises: 
Create Date: 2023-10-15 11:30:10.548490

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bfc353d6d95f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "temperature_records",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("temperature", sa.Float, nullable=False),
        sa.Column("location", sa.String(255), nullable=False),
        sa.Column("recorded_at", sa.DateTime(timezone=True), nullable=False),
    )


# alternatively, we can use raw SQL:
# def upgrade() -> None:
#     op.execute(
#         """
#         CREATE TABLE temperature_records (
#             id SERIAL PRIMARY KEY,
#             temperature FLOAT NOT NULL,
#             location TEXT NOT NULL,
#             recorded_at TIMESTAMP NOT NULL
#         )
#         """
#     )


def downgrade() -> None:
    op.drop_table("temperature_records")
