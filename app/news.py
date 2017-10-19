from flask import render_template
from app import app#loads the app instance from the app folder

#news
@app.route('/news/<news_id>')#route decorator int: tranforms the content into an integer
def news(news_id):#news function 
	"""
	news function that returns the index page and its data
	"""

	return render_template('news.html',id = news_id)#message variable on the left represents the variable on our index template while on the right represnts our view variable

def index():
	"""
	new root page functioni return the page with all of its dat
	"""

	title = 'Home - Welcome to The best New Resource Website Online'
	return render_template('index.html',title = title)