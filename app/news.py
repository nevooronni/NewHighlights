from flask import render_template
from app import app#loads the app instance from the app folder
from .request import get_news_source

#news
@app.route('/')#route decorator int: tranforms the content into an integer
def index():
	"""
	new root page functioni return the page with all of its dat
	"""

	#getting general news
	general_news = get_news_source('general')
	entertainment_news = get_news_source('entertainment')
	politics_news = get_news_source('politics')
	technology_news =  get_news_source('technology')
	business_news = get_news_source('business')
	title = 'Home - welcome to News Highlight the best news source website there is.'
	return render_template('index.html',title = title,general = general_news,entertainment = entertainment_news,politics = politics_news,technology = technology_news,business = business_news)