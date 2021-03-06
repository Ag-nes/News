import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Kyle Mullin',
                                   ' The feud between major artists and Spotify has overlooked problems faced by those with less power and financesThe past week has seen artists such as Neil Young, Joni Mitchell, Graham Nash and Nils Lofgren stand up to Spotify, boycotting the streaming giant be…',
                                   '2022-02-02T07:10:17Z',
                                   'https://www.nytimes.com/2018/08/31/sports/tennis/us-open-results.html',
                                   'https://static01.nyt.com/images/2018/09/01/sports/01openlive7/01openlive7'
                                   '-facebookJumbo.jpg',
                                   'US Open 2018 Results')

    def test_instance(self):
        '''
        Test to check creation of new article instance
        '''
        self.assertTrue(isinstance(self.new_article, Article))
