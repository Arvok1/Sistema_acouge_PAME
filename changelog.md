
Versão 0.02:
Modifica as tabelas de usuário, endereço, itens, pedidos e lojas, pois as mesmas possuíam alguns erros em que possuíam mais de uma ligação entre si(as que possuem relacionamentos)
Adiciona "Sessões" através do uso de tokens JWT
Adiciona encriptação de senha através de bcrypt
Adiciona a vinculação de Usuários a Lojas
Adiciona Criação de itens -> O usuário precisa ter permissão na Loja em que o item será criado
Adiciona Modificação de itens -> O usuário precisa ter permissão na Loja em que o item será criado

TODO:
Criação de Loja
Compra de pedido
Visualização de pedidos do usuário
Excluir item do pedido
