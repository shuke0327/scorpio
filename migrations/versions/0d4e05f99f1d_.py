"""empty message

Revision ID: 0d4e05f99f1d
Revises: 
Create Date: 2018-04-16 14:41:22.983495

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '0d4e05f99f1d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blocks',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('index', sa.INTEGER(), nullable=False),
    sa.Column('hash', sa.String(length=64), nullable=False),
    sa.Column('previous_hash', sa.String(length=64), nullable=False),
    sa.Column('difficulty', sa.INTEGER(), nullable=False),
    sa.Column('timestamp', sqlite.DATETIME(), nullable=False),
    sa.Column('nonce', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blocks_hash'), 'blocks', ['hash'], unique=True)
    op.create_index(op.f('ix_blocks_index'), 'blocks', ['index'], unique=True)
    op.create_index(op.f('ix_blocks_previous_hash'), 'blocks', ['previous_hash'], unique=True)
    op.create_table('transactions',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('txid', sa.String(length=64), nullable=False),
    sa.Column('block_id', sa.INTEGER(), nullable=False),
    sa.Column('position', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transactions_block_id'), 'transactions', ['block_id'], unique=False)
    op.create_index(op.f('ix_transactions_position'), 'transactions', ['position'], unique=False)
    op.create_index(op.f('ix_transactions_txid'), 'transactions', ['txid'], unique=False)
    op.create_table('tx_ins',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('transaction_id', sa.INTEGER(), nullable=False),
    sa.Column('signature', sa.String(length=256), nullable=False),
    sa.Column('tx_out_id', sa.String(length=64), nullable=False),
    sa.Column('tx_out_index', sa.INTEGER(), nullable=False),
    sa.Column('position', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tx_ins_position'), 'tx_ins', ['position'], unique=False)
    op.create_index(op.f('ix_tx_ins_transaction_id'), 'tx_ins', ['transaction_id'], unique=False)
    op.create_table('tx_outs',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('transaction_id', sa.INTEGER(), nullable=False),
    sa.Column('position', sa.INTEGER(), nullable=False),
    sa.Column('address', sa.String(length=64), nullable=False),
    sa.Column('amount', sa.NUMERIC(precision=8, scale=6, asdecimal=False), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tx_outs_position'), 'tx_outs', ['position'], unique=False)
    op.create_index(op.f('ix_tx_outs_transaction_id'), 'tx_outs', ['transaction_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tx_outs_transaction_id'), table_name='tx_outs')
    op.drop_index(op.f('ix_tx_outs_position'), table_name='tx_outs')
    op.drop_table('tx_outs')
    op.drop_index(op.f('ix_tx_ins_transaction_id'), table_name='tx_ins')
    op.drop_index(op.f('ix_tx_ins_position'), table_name='tx_ins')
    op.drop_table('tx_ins')
    op.drop_index(op.f('ix_transactions_txid'), table_name='transactions')
    op.drop_index(op.f('ix_transactions_position'), table_name='transactions')
    op.drop_index(op.f('ix_transactions_block_id'), table_name='transactions')
    op.drop_table('transactions')
    op.drop_index(op.f('ix_blocks_previous_hash'), table_name='blocks')
    op.drop_index(op.f('ix_blocks_index'), table_name='blocks')
    op.drop_index(op.f('ix_blocks_hash'), table_name='blocks')
    op.drop_table('blocks')
    # ### end Alembic commands ###
