import os #lets our app interact with the os dependent functionality


class Config:
	"""
	General config parent class
	"""
	NEWS_API_BASE_URL = 'https://newsapi.org/v1/sources?language=en&apiKey={}'
	NEWS_API_KEY = os.environ.get('NEWS_API_KEY')#get our api key using the os module

class ProdConfig(Config):
	"""
	production configuration child class 

	Args:
		Config: The parent configuration class with Genreal configuration settings
	"""
	pass

class DevConfig(Config):
	"""
	Development configutation child class

	Args:
		Config: The parent configuration class with General configuration settings 
	"""

	DEBUG = True

#dictionary to help us access different configuration options
config_options = {
'development':DevConfig,
'production':ProdConfig
}