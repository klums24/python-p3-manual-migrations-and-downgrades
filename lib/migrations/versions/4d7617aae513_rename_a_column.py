"""rename a column

Revision ID: 4d7617aae513
Revises: 463114953afb
Create Date: 2023-06-13 10:50:34.663627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d7617aae513'
down_revision = '463114953afb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("scholars", 'name', new_column_name='student_name')


def downgrade() -> None:
    op.alter_column("scholars", 'name', new_column_name='student_name')
