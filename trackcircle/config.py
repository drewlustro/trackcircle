DEBUG = True
SECRET_KEY = 'OMG-RANDOM-KEY'
DB_USERNAME = 'dev'
DB_PASSWORD = 'pass'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'trackcircle'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://%s:%s@%s:%s/%s' % \
                            (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
                            
FACEBOOK_APP_ID = '179835715363182'
FACEBOOK_APP_SECRET = 'b68ea76de379400734e2a5ef792e30aa'
UPLOAD_FOLDER = '/tmp'

AMAZON_S3_ID = 'AKIAJIRHFLNDAK4USTTQ'
AMAZON_S3_SECRET = 'd560Ka2iDsFMEZ9MxUxGq97XSSpFP6FlhGcL'