"""change a column name

Revision ID: d0a88678a849
Revises: 4d7617aae513
Create Date: 2023-06-13 10:58:02.420524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0a88678a849'
down_revision = '4d7617aae513'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("scholars", 'name', new_column_name='student_name')


def downgrade() -> None:
    op.alter_column("scholars", 'name', new_column_name='student_name')

