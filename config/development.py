# Secret key for hasing
SECRET_KEY = 'a%6s5as6d%'
DEBUG = True
# database setting
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:123@localhost/sporulecms'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# WTF Setting
WTF_CSRF_ENABLED = True  # CSRF is a token to prevent fake post

# Auto Login as admin
AUTO_LOGIN = True
