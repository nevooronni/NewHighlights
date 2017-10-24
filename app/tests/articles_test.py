import unittest
from app.models import Articles

class TestArticles(unittest.TestCase):
	"""
	Test case to test the behaviour of the articles 
	"""
	def setup(self):
		"""function runs before each test is executed
		"""
		self.new_article = Articles("soiruweo","alsfkjlasjff","owieruweiour","ierwoiur","eirwui","oweruoire")

	def test_init(self):
		"""
		tests if the objects is initialized correctly
		"""

		self.assertEqual(self.new_article.author,"soiruweo")
		self.assertEqual(self.new_article.title,"alsfkjlasjff")
		self.assertEqual(self.new_article.description,"owieruweiour")	
		self.assertEqual(self.new_article.link,"erwoiur")	
		self.assertEqual(self.new_article.image,"eirwui")
		self.assertEqual(self.new_article.time,"oweruoire")

	def test_init(self):
		"""
		Function to test if the object is initialized properly
		"""
		self.assertTrue(isinstance(self.new_article,Articles))		