import quadrigacx
import unittest
import requests
from unittest.mock import patch
from unittest.mock import MagicMock

class TestQuadrigaCx(unittest.TestCase):


    def test_generate_signature(self):
        self.assertEqual(True, True) #dummy test

    def test_get_account_balance(self):
        self.assertEqual(True, True) #dummy test

    def test_get_user_transactions(self):
        self.assertEqual(True, True) #dummy test

    @patch('quadrigacx.Quadriga._handle_response')
    @patch('requests.get') #mock the get method of requests for the duration of this method
    def test_get_order_book(self, requestsget, _handle_response):
        api_definition ={
            'method': 'get',
            'url': 'https://api.quadrigacx.com/v2/order_book',
            'query_parameters': ['book', 'group']
        }
        def mock_get_request(url, params):
            self.assertEqual(url, api_definition['url']) #make sure the URL corresponds to the one give by Quadrigacx
            for api_parameter in api_definition['query_parameters']:
                self.assertNotEqual(params[api_parameter], None) #make sure all query_parameters are passed to the uut

        requestsget.side_effect = mock_get_request #define the function to be called, instead of the original requests.get
        _handle_response.side_effect = lambda response, parse: None #mock _handle_response will do nothing

        quadriga = quadrigacx.Quadriga();

        quadriga.get_order_book()
        self.assertEqual(requestsget.call_count, 1)

    @patch('quadrigacx.Quadriga._handle_response')
    @patch('requests.get') #mock the get method of requests for the duration of this method
    def test_get_current_trading_info(self, requestsget, _handle_response):
        api_definition ={
            'method': 'get',
            'url': 'https://api.quadrigacx.com/v2/ticker',
            'query_parameters': ['book']
        }
        def mock_get_request(url, params):
            self.assertEqual(url, api_definition['url']) #make sure the URL corresponds to the one give by Quadrigacx
            for api_parameter in api_definition['query_parameters']:
                self.assertNotEqual(params[api_parameter], None) #make sure all query_parameters are passed to the uut

        requestsget.side_effect = mock_get_request #define the function to be called, instead of the original requests.get
        _handle_response.side_effect = lambda response, parse: None

        quadriga = quadrigacx.Quadriga();
        quadriga.get_current_trading_info()
        self.assertEqual(requestsget.call_count, 1)

    @patch('quadrigacx.Quadriga.generate_signature')
    @patch('quadrigacx.Quadriga._handle_response')
    @patch('requests.post')
    def test_get_open_orders(self, requestspost, _handle_response, generate_signature):
        api_definition ={
            'method': 'post',
            'url': 'https://api.quadrigacx.com/v2/open_orders',
            'query_parameters': ['book']
        }
        def mock_post_request(url, data):
            self.assertEqual(url, api_definition['url']) #make sure the URL corresponds to the one give by Quadrigacx
            self.assert_payload_data_dictionary(data)


        generate_signature.side_effect = fake_signature
        requestspost.side_effect = mock_post_request #define the function to be called, instead of the original requests.get
        _handle_response.side_effect = lambda response, parse: None #handle response does nothing

        quadriga = quadrigacx.Quadriga();
        quadriga.get_open_orders()
        self.assertEqual(requestspost.call_count, 1)

    def test_lookup_order(self):
        self.assertEqual(True, True) #dummy test

    def test_cancel_order(self):
        self.assertEqual(True, True) #dummy test

    def test_buy_order_limit(self):
        self.assertEqual(True, True) #dummy test

    def test_buy_order_market(self):
        self.assertEqual(True, True) #dummy test

    def test_sell_order_limit(self):
        self.assertEqual(True, True) #dummy test

    def test_sell_order_market(self):
        self.assertEqual(True, True) #dummy test

    def test_bitcoin_deposit(self):
        self.assertEqual(True, True) #dummy test

    def test_bitcoin_withdrawal(self):
        self.assertEqual(True, True) #dummy test

    def test_ether_deposit(self):
        self.assertEqual(True, True) #dummy test

    def test_ether_withdrawal(self):
        self.assertEqual(True, True) #dummy test

    def test__handle_response(self):
        def _assert_handle_response_200(oFakeResponse, expectation=None):
            returnval = quadriga._handle_response(oFakeResponse, oFakeResponse.parse)
            self.assertEqual(returnval, expectation)

        quadriga = quadrigacx.Quadriga()
        #############status_code is 200
        #with parse = False
        fake_response = FakeResponse(200, "Success", False)
        fake_response.json = MagicMock(return_value=None) #our mock json method returns nothing

        _assert_handle_response_200(fake_response, "Success")
        fake_response.json.assert_not_called() #when parse = False, the response.json() method should not be called

        #with parse = True
        fake_response = FakeResponse(200, "Success", True)
        fake_response.json = MagicMock(return_value=None)#our mock json method returns nothing

        _assert_handle_response_200(fake_response, None) #nothing is returned in .json() method of FakeResponse class
        self.assertEqual(fake_response.json.call_count, 1) #check that the .json() method was called on the mock

        #############status_code is 401
        #with parse = False
        fake_response = FakeResponse(401, "Fail", False)
        returns = quadriga._handle_response(fake_response, False)
        self.assertEqual(type(returns), str) # returns a string
        self.assertTrue('401' in returns) #string contains the error code

        #with parse = True
        returns = quadriga._handle_response(fake_response, True)
        self.assertEqual(type(returns), dict) # returns a dictionary
        self.assertTrue('401' in returns['error']) #string contains the error code

    ##helper methods
    def assert_query_parameters(self, params, api_definition):
        for api_parameter in api_definition['query_parameters']:
            self.assertNotEqual(params[api_parameter], None) #make sure all query_parameters are passed to the uut
    def assert_payload_data_dictionary(self, datadictionary):
        payload_dictionarykeys= ['key', 'signature', 'nonce', 'book']
        for payload_key in payload_dictionarykeys: #payload key found in the data arguments
            self.assertNotEqual(datadictionary[payload_key], None) #make sure the data dictionary has all the required keys
class FakeResponse():
    def __init__(self, status_code = 200, text="Default text", parse = False):
        self.status_code = status_code
        self.text = text
        self.parse = parse
    def json(self):
        #fake json method for spy
        pass


def fake_signature():
    return "FakeSignature", "FakeNonce"


if __name__ == '__main__':
    unittest.main()
