"""first migration

Revision ID: ecf080d8d15c
Revises: 
Create Date: 2023-06-26 14:29:50.407303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecf080d8d15c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_name', sa.String(), nullable=False),
    sa.Column('off_rank_2022', sa.Integer(), nullable=True),
    sa.Column('def_rank_2022', sa.Integer(), nullable=True),
    sa.Column('points_per_game_2022', sa.Float(), nullable=True),
    sa.Column('points_allowed_2022', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_date', sa.DateTime(), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('matchup', sa.String(length=100), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prediction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('machine_predicted_score', sa.Float(), nullable=True),
    sa.Column('user_predicted_score', sa.Float(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prediction')
    op.drop_table('game')
    op.drop_table('team')
    # ### end Alembic commands ###
