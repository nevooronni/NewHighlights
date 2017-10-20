import unittest 
from models import news
News = news.News

class NewsTest(unittest.TestCase):
	"""
	Test case to test the behaviour of the news class
	"""

	def setUp(self):
		"""
		set up method that will run before every test
		"""
		self.new_news_source = News("al-jazeera-english","Al Jazeera English","News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.","http://www.aljazeera.com","general")

	def test_instance(self):
		self.assertTrue(isinstance(self.new_news_source,News))

	def test_init(self):
		"""
		test_init test case to test if the object is initialized porperly
		"""

		self.assertEqual(self.new_news_source.id,"al-jazeera-english")
		self.assertEqual(self.new_news_source.name,"Al Jazeera English")
		self.assertEqual(self.new_news_source.description,"News, analysis from the Middle East and worldwide, multimedia and interactives, opinions, documentaries, podcasts, long reads and broadcast schedule.")	

		self.assertEqual(self.new_news_source.url,"http://www.aljazeera.com")

if __name__ == '__main__':
  unittest.main()