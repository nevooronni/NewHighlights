class Config:
	"""
	General config parent class
	"""
	NEWS_API_BASE_URL = 'https://newsapi.org/v1/sources?&apiKey={}'

class prodConfig(Config):
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