class News:
	"""
	New class to define News Source objects
	"""

	def __init__(self,id,name,description,url,category):
		self.id = id
		self.name = name
		self.description = description
		self.url = url
		self.category = category

class Articles:
	"""
	Articles to define articles from a specific new source
	"""

	def __init__(self,author,title,description,url,image,time):
		self.author = author
		self.title = title
		self.description = description
		self.url = url
		self.image = image
		self.time = time

