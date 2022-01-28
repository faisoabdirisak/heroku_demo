import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('Last Roman Amphitheater','Mysterious News Briefly','https://mysteriousuniverse.org/2022/01/la','https://mysteriousuniverse.org/wp-content/uploads/2020/08/breaking-1.jpg','2022-01-27T12:33:11Z','Mysterious News Briefly January 27,2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()