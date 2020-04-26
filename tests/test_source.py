import unittest
from app.models import Source
Source = source.Source

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


 
if __name__ == '__main__':
	unittest.main()
