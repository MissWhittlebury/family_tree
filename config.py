import os



class Config:
    DB_USER    = os.getenv('DB_USER')
    DB_PWD     = os.getenv('DB_PWD')
    DB_HOST    = os.getenv('DB_HOST')
    DB_PORT    = os.getenv('DB_PORT')
    DB_NAME    = os.getenv('DB_NAME') or 'family_tree'
    DB_DIALECT = os.getenv('DB_DIALECT') or 'postgresql'

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        db_dialect = self.DB_DIALECT.lower()
        ##TODO(dwojtak): allow different db types
        if db_dialect == 'postgresql':
            return f'postgresql://{self.DB_USER}:{self.DB_PWD}@' \
                   f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
