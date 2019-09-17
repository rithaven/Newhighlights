import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_Articlese = Articles('the-next-web','The Next Web','Satoshi Nakaboto','Satoshi Nakaboto: ‘Portugal declares Bitcoin trading and payments tax-free','https://thenextweb.com/hardfork/2019/08/30/satoshi-nakaboto-portugal-declares-bitcoin-trading-and-payments-tax-free/','https://img-cdn.tnwcdn.com/image/hardfork?','2019-08-30T08:44:13Z','Our robot colleague Satoshi Nakaboto writes about Bitcoin BTC every fucking day.')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_Articlese,Articles))