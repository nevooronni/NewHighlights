from app import app
from urllib.request,json#module help us create a connection to our api url and json module will format the json response to a python dictonary
from .models import news#from package models import module news and select class news\

News = news.News

#Getting api key
api_key = app.congig['NEWS_API_KEY']

#Getting the news base url
base_url = app.config['MOVIE_API_BASE_URL']