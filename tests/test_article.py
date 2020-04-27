import unittest
from app.models import Article
#Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("oilfluctuation","oil.com","Duncan Kiragu","Big break in the fuel industry","The fuel industry hits an invisible iceberg and is struggling to keep afloat","https://www.oilfluctuation.com","https://cdn.oilfluctuation.com/article-new/2019/09/iphone-x-display.jpg?retina","2019-03-20")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        self.assertEqual(self.new_article.id,"oilfluctuation")
        self.assertEqual(self.new_article.name,"oil.com")
        self.assertEqual(self.new_article.author,"Duncan Kiragu")
        self.assertEqual(self.new_article.title,"Big break in the fuel industry")
        self.assertEqual(self.new_article.description,"The fuel industry hits an invisible iceberg and is struggling to keep afloat")
        self.assertEqual(self.new_article.url,"https://www.oilfluctuation.com")
        self.assertEqual(self.new_article.image,"https://cdn.oilfluctuation.com/article-new/2019/09/iphone-x-display.jpg?retina")
        self.assertEqual(self.new_article.date,"2019-03-20")






if __name__ == '__main__':
     unittest.main()