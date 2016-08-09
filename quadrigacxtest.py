import quadrigacx
import unittest

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
        self.assertEqual(True, True)
        quadriga = quadrigacx.Quadriga()

        successful_response = FakeResponse(status_code = 200, text = "Success")
        returnval = quadriga._handle_response(successful_response)
        self.assertEqual(returnval, "Success")

        successful_response = FakeResponse(status_code = 401, text = "Failed")
        returnval = quadriga._handle_response(successful_response)
        self.assertEqual(returnval['error'], 'code: 401')

class FakeResponse():
    def __init__(self, status_code = 200, text="Default text"):
        self.status_code = status_code
        self.text = text

if __name__ == '__main__':
    unittest.main()
