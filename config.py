import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = 'sadkjhfkdjshgeytertgfasdgdfahgfhds'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	@staticmethod
	def init_app(app):
		pass

class Development(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/noahfrenkel/dev/websites/carpoll/db.sqlite'

class Testing(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite////Users/noahfrenkel/dev/websites/carpoll/db.sqlite'


class Production(Config):
	pass

config = {
	'development' : Development,
	'testing' : Testing,
	'production' : Production,
	'default' : Development 
}