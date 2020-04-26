import unittest
from app.models import Source
# Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("Bit-coin news","Crypto Coins News","Providing breaking cryptocurrency news.", "https://www.bitcoin.com","technology","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
    def test_init(self):
        self.assertEqual(self.new_source.id,"Bit-coin news")
        self.assertEqual(self.new_source.name,"Crypto Coins News")
        self.assertEqual(self.new_source.description,"Providing breaking cryptocurrency news.")
        self.assertEqual(self.new_source.url,"https://www.bitcoin.com")
        self.assertEqual(self.new_source.category,"technology")
        self.assertEqual(self.new_source.language,"en")
        self.assertEqual(self.new_source.country,"us")




class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("oilfluctuation","Macrumors.com","Duncan Kiragu","Big break in the fuel industry","The fuel industry hits an invisible iceberg and is struggling to keep afloat","https://www.oilfluctuation.com","https://cdn.oilfluctuation.com/article-new/2019/09/iphone-x-display.jpg?retina","2019-03-20")

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






# if __name__ == '__main__':
#     unittest.main()