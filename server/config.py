import getpass

print(getpass.getuser())
SQLALCHEMY_DATABASE_URI = 'postgresql://'+getpass.getuser()+':dbpasswd@localhost/bookbagging'
SQLALCHEMY_ECHO = True
DEBUG = True
