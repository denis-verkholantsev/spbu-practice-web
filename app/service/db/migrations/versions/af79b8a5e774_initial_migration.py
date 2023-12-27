"""Initial migration

Revision ID: af79b8a5e774
Revises: 
Create Date: 2023-12-20 22:42:22.558550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af79b8a5e774'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('password', sa.String(length=16), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('file',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('filename', sa.String(length=256), nullable=False),
    sa.Column('file_data', sa.LargeBinary(), nullable=True),
    sa.Column('task_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user_.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teacher',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user_.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.Column('end', sa.DateTime(), nullable=False),
    sa.Column('teacher_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('teacher_id', sa.Uuid(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['task.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('homework',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=True),
    sa.Column('teacher_id', sa.Uuid(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['task.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teacher_student',
    sa.Column('teacher_id', sa.Uuid(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ),
    sa.PrimaryKeyConstraint('teacher_id', 'student_id')
    )
    op.create_table('homework_exercise',
    sa.Column('homework_id', sa.Uuid(), nullable=False),
    sa.Column('exercise_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercise.id'], ),
    sa.ForeignKeyConstraint(['homework_id'], ['homework.id'], ),
    sa.PrimaryKeyConstraint('homework_id', 'exercise_id')
    )
    op.create_table('homework_student',
    sa.Column('homework_id', sa.Uuid(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['homework_id'], ['homework.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('homework_id', 'student_id')
    )
    op.create_table('solution',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.Column('exercise_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercise.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['id'], ['task.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_event',
    sa.Column('student_id', sa.Uuid(), nullable=False),
    sa.Column('event_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('student_id', 'event_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_event')
    op.drop_table('solution')
    op.drop_table('homework_student')
    op.drop_table('homework_exercise')
    op.drop_table('teacher_student')
    op.drop_table('homework')
    op.drop_table('exercise')
    op.drop_table('event')
    op.drop_table('teacher')
    op.drop_table('student')
    op.drop_table('file')
    op.drop_table('user_')
    op.drop_table('task')
    # ### end Alembic commands ###