import os



class Config:
    DB_USER    = os.getenv('DB_USER')
    DB_PWD     = os.getenv('DB_PWD')
    DB_HOST    = os.getenv('DB_HOST')
    DB_PORT    = os.getenv('DB_PORT')
    DB_NAME    = os.getenv('DB_NAME') or 'family_tree'
    DB_DIALECT = os.getenv('DB_DIALECT') or 'postgresql'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PWD}@' \
                              f'{DB_HOST}:{DB_PORT}/{DB_NAME}'
