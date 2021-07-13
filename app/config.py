class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data-dev.db' #banco de dados a ser usado 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False #retorna na sequencia que foram criados e não em ordem alfabética
    