from flask import render_template,request,redirect,url_for
from . import main#loads the app instance from the app folder
from ..request import get_news_source,get_newsource_articles#python relative import system two dots in other packages

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

#dynamically route our articles templates
@app.route('/news/<id>')
def news(id):
	"""
	function that return a list of news articlses belonging to a specific news source
	"""

	news_article = get_newsource_articles(id)
	title = f'{id} Latest News'

	return render_template('news.html',title = title, article = news_article)