"""DB creation

Revision ID: afc3fe873dd4
Revises: 
Create Date: 2023-06-05 11:28:04.340962

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'afc3fe873dd4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('permissions', sa.JSON(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('role_id', sa.Integer(), nullable=True),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('registered', sa.TIMESTAMP(), nullable=True),
                    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###
