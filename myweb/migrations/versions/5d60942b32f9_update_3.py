"""update_3

Revision ID: 5d60942b32f9
Revises: e5aa46bc21e8
Create Date: 2023-10-23 18:56:05.751333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d60942b32f9'
down_revision = 'e5aa46bc21e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_constraint('fk_task_project', type_='foreignkey')
        batch_op.create_foreign_key('fk_task_project', 'project', ['project_id'], ['project_id'], ondelete='SET NULL')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_constraint('fk_task_project', type_='foreignkey')
        batch_op.create_foreign_key('fk_task_project', 'project', ['project_id'], ['project_id'])

    # ### end Alembic commands ###