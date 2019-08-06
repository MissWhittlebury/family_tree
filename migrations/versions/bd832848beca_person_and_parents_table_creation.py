"""person and parents table creation

Revision ID: bd832848beca
Revises: 
Create Date: 2019-08-05 18:46:02.528832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd832848beca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('email_address', sa.String(length=255), nullable=True),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('parents_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(constraint_name='uq_person_first_last_birth',
                                table_name='person',
                                columns=['first_name', 'last_name',
                                         'birth_date'])

    op.create_table('parents',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('mother_person_id', sa.Integer(), nullable=True),
    sa.Column('father_person_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['father_person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['mother_person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(constraint_name='uq_mother_father',
                                table_name='parents',
                                columns=['mother_person_id', 'father_person_id'])

    op.create_foreign_key(constraint_name='fk_parents_person',
                          source_table='person',
                          referent_table='parents',
                          local_cols=['parents_id'],
                          remote_cols=['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_parents_person', 'person')
    op.drop_table('parents')
    op.drop_table('person')
    # ### end Alembic commands ###
