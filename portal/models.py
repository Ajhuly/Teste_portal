import os

SECRET_KEY = 'nib-portal'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'nib',
        senha = 'Administrador@25',
        servidor = '127.0.0.1',
        database = 'portal'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'