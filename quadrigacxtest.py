import quadrigacx
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

class TestQuadrigaCx(unittest.TestCase):
    def test_generate_signature(self):
        self.assertEqual(True, True) #dummy test

    def test_get_account_balance(self):
        self.assertEqual(True, True) #dummy test

    def test_get_user_transactions(self):
        self.assertEqual(True, True) #dummy test

    def test_get_open_orders(self):
        self.assertEqual(True, True) #dummy test

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

class FakeResponse():
    def __init__(self, status_code = 200, text="Default text", parse = False):
        self.status_code = status_code
        self.text = text
        self.parse = parse
    def json(self):
        #fake json method for spy
        pass

if __name__ == '__main__':
    unittest.main()
