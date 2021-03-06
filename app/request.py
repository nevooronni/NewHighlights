import urllib.request,json#module help us create a connection to our api url and json module will format the json response to a python dictonary
from .models import News,Articles#from package models import module news and select class news

#Getting api key
api_key = None

#Getting the news base url
base_url = None#we then access our app config objects by app.config['name_of_object']

def configure_request(app):
	global api_key,base_url
	api_key = app.config['NEWS_API_KEY']
	base_ulr = app.config['NEWS_API_BASE_URL']

def get_news_source(category):
	"""
	function that gets the json reponse to our url request
	"""
	get_news_url = 'https://newsapi.org/v1/sources'.format(category,api_key)#takes news by category and places this at the end of our api key


	with urllib.request.urlopen(get_news_url) as url:#send a request using the get_news_url as final url
		get_news_data = url.read()#read the response and store it in the variable
		get_news_response = json.loads(get_news_data)#convert the json reponse to a python dictonary

		news_results = None#create empty variable

		if get_news_response['sources']:#check if the reponse contains any results
			news_results_list = get_news_response['sources']#store the results 
			news_results = process_results(news_results_list)#call a function thet take in the list of dictionary objects and returns a list of news objects

			return news_results#list of news objects

def process_results(news_list):
	"""
	function that processes news list dictonary and turns them to a list of objects
	
	Args:
		news_list: A list of dictonatires that contain news sources
	
	Return:
		news_results: A lists of news objects
	"""
	news_results = []
	for source in news_list:
		id = source.get('id')
		name = source.get('name')
		description = source.get('description')
		url = source.get('url')
		category = source.get('category')

		news_object = News(id,name,description,url,category)
		news_results.append(news_object)

	return news_results

def get_newsource_articles(id):
	get_newsource_articles_url = 'https://newsapi.org/v1/articles?source={}&apiKey={}'.format(id,api_key)

	with urllib.request.urlopen(get_newsource_articles_url) as url:
		news_source_articles_data = url.read()
		news_source_articles_response = json.loads(news_source_articles_data)

		news_source_results  = None
		if news_source_articles_response['articles']:
			news_source_result_list = news_source_articles_response['articles']
			news_source_results = process_articles_results(news_source_result_list)
		
	return news_source_results		

def process_articles_results(articles_list):
	"""
	function that process the news articles list dictionary and tunrs them to a list of objects
	
	Args:
		news_source_result_list: A list of dictionaries that contain news sources

	Return:
		news_source_results: A lists of news objects
	"""
	news_source_results = []
	for article in articles_list:
		author = article.get('author')
		title	= article.get('title')
		description = article.get('description')
		link = article.get('url')
		image = article.get('urlToImage')
		time = article.get('publishedAt')

		if image:
			articles_object = Articles(author,title,description,link,image,time)
			news_source_results.append(articles_object)

	return news_source_results	

