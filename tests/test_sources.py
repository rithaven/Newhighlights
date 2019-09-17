import unittest
from app.models import sources

class sourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = sources('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive','https://abcnews.go.com','general','en','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,sources))