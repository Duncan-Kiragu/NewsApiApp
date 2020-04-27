import unittest
from app.models import Source,Article
#Source = source.Source
#Article = article.Article

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
        self.new_article = Article("null","Softpedia.com","Softpedia Windows","Netbox Browser 80.0.3987.149 (Freeware)","Download Netbox Browser - A straightforward browser that doesn't snoop into your browsing history, and on the top of it, it rewards you with NBX crypto coins each time you use it","https://www.softpedia.com/get/Internet/Browsers/Netbox-Browser.shtml","null","2020-04-27T01:44:01Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        self.assertEqual(self.new_article.id,"null")
        self.assertEqual(self.new_article.name,"Softpedia.com")
        self.assertEqual(self.new_article.author,"Softpedia Windows")
        self.assertEqual(self.new_article.title,"Netbox Browser 80.0.3987.149 (Freeware)")
        self.assertEqual(self.new_article.description,"Download Netbox Browser - A straightforward browser that doesn't snoop into your browsing history, and on the top of it, it rewards you with NBX crypto coins each time you use it")
        self.assertEqual(self.new_article.url,"https://www.softpedia.com/get/Internet/Browsers/Netbox-Browser.shtml")
        self.assertEqual(self.new_article.image,"null")
        self.assertEqual(self.new_article.date,"2020-04-27T01:44:01Z")


 
# if __name__ == '__main__':
#	unittest.main()
