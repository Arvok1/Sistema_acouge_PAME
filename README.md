# Sistema_acouge_PAME

informações necessárias em sensive:

class Sensive:

    SQLALCHEMY_DATABASE_URI = #configuração de tipo de banco de dados do sqlalchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = 
    JSON_SORT_KEYS = #retorna na sequencia que foram criados e não em ordem alfabética
    server_email = #seu email, configurado no sendgrid como sender

    #as configurações que começam com MAIL são as configurações de serviço SMTP
    MAIL_SERVER = 
    MAIL_PORT = 
    MAIL_USERNAME = 
    MAIL_KEY = 
    JWT_SECRET_KEY = 

Rotas e Métodos já feitos para cada classe no momento:

Endereço:
Nenhuma rota foi feita ainda

Item:
/itens -> responsável por listar todos os itens disponíveis na plataforma

/loja/item/<int:item_id>/details -> quando recebe um GET, mostra os dados do item.
Quando recebe um PATCH, atualiza os dados informados de maneira diferente, caso alguma informação precise ser atualizada pela loja ou tenha sido inserida errada

Quando recebe um DELETE, apaga as informações do item, pode ser usada no caso de o item ter sido vendido ao vivo, em vez de pelo sistema web(necessita a implementação no futuro)

Loja:
Nenhuma rota foi feita ainda

Pedido:
/item/addtocart/<int:usuario_id> -> adiciona os itens recebidos via JSON para o pedido mais atual do usuario

Usuario:
#/user/create -> GET mostraria uma página de registro, POST faz o registro

#/user/login -> GET mostra a página de login, POST faz o "login"

#/user/details -> GET mostra as informações do usuário, PATCH modifica as informações que forem enviados do usuário

