"""empty message

Revision ID: 6037175038f9
Revises: 
Create Date: 2021-07-15 23:40:35.477722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6037175038f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loja',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=30), nullable=True),
    sa.Column('telefone', sa.String(length=11), nullable=True),
    sa.Column('zona_entrega', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=30), nullable=True),
    sa.Column('login', sa.String(length=10), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('hash_senha', sa.String(length=300), nullable=False),
    sa.Column('telefone', sa.String(length=10), nullable=True),
    sa.Column('user_role', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('login')
    )
    op.create_table('endereco',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('loja_id', sa.Integer(), nullable=True),
    sa.Column('endereco', sa.String(length=50), nullable=True),
    sa.Column('complemento', sa.String(length=6), nullable=True),
    sa.Column('bairro', sa.String(length=10), nullable=True),
    sa.Column('cep', sa.String(length=10), nullable=True),
    sa.Column('cidade', sa.String(length=20), nullable=True),
    sa.Column('estado', sa.String(length=3), nullable=True),
    sa.ForeignKeyConstraint(['loja_id'], ['loja.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('horario_atualizado', sa.Time(timezone=True), nullable=True),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.Column('validade', sa.DateTime(), nullable=True),
    sa.Column('imagem', sa.String(length=30), nullable=True),
    sa.Column('peso', sa.Float(), nullable=True),
    sa.Column('valor', sa.Float(), nullable=True),
    sa.Column('loja_id', sa.Integer(), nullable=True),
    sa.Column('quantidade_disponivel', sa.Integer(), nullable=True),
    sa.Column('disponivel', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['loja_id'], ['loja.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_horario', sa.DateTime(), nullable=False),
    sa.Column('modo_entrega', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('metodo_pagamento', sa.Integer(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios_lojas_permissoes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('loja_id', sa.Integer(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('permissao', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['loja_id'], ['loja.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('itens_pedidos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('pedido_id', sa.Integer(), nullable=True),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.Column('peso', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['pedido_id'], ['pedido.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('itens_pedidos')
    op.drop_table('usuarios_lojas_permissoes')
    op.drop_table('pedido')
    op.drop_table('item')
    op.drop_table('endereco')
    op.drop_table('usuario')
    op.drop_table('loja')
    # ### end Alembic commands ###