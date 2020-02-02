import unittest
from trends import news
news = news.news

class newsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        # self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):import unittest
from trends import news
news = news.news


class newsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the news class
    '''


    def setUp(self):
        
        self.assertTrue(isinstance(self.trending_news,news))


if __name__ == '__main__':
    unittest.main()