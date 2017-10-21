from app import app
import urllib.request,json#module help us create a connection to our api url and json module will format the json response to a python dictonary
from .models import news#from package models import module news and select class news\

News = news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']#we then access our app config objects by app.config['name_of_object']


def get_news_source(category):
	"""
	function that gets the json reponse to our url request
	"""
	get_news_url = base_url.format(category,api_key)#takes news by category and places this at the end of our api key


	with urllib.request.urlopen(get_news_url) as url:#send a request using the get_news_url as final url
		get_news_data = url.read()#read the response and store it in the variable
		get_news_response = json.loads(get_news_data)#convert the json reponse to a python dictonary

		news_results = None#create empty variable

		if get_news_response['sources']:#check if the reponse contains any results
			news_results_list = get_news_response['sources']#store the results 
			news_results = process_results(news_results_list)#call a funtcion thet take in the list of dictionary objects and returns a list of news objects

			return news_results#list of news objects

def process_results(news_list):
	"""
	function that processes news list dictonary and turns them to a list of objects
	
	Args:
		news_list: A list of dictonatires that contain news sources
	
	Return:
		new_results: A lists of news objects
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

