import requests
import time
import hmac
import hashlib

class Quadriga:
    # Setting parseDicts to False returns all responses as strings, rather than parsing them as dictionaries when json responses are possible
    def __init__(self, apiKey='string', apiSecret='string', clientID='integer', parseDicts=True):
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.clientID = clientID
        self.parseDicts = parseDicts # Return json data as a dictionary. False -> string responses

    def generate_signature(self):
        #uses ms for nonce to avoid collision
        nonce = str(int(time.time()*1000))
        key = self.apiKey
        client = str(self.clientID)
        secret = self.apiSecret
        msg = str(nonce)+str(client)+key
        signature = hmac.new(secret.encode(), msg=msg.encode(), digestmod=hashlib.sha256).hexdigest()
        return signature, nonce

    def get_account_balance(self):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/balance', data={'key':self.apiKey,'signature':signature,'nonce':nonce})
        return self._handle_response(response, parse = self.parseDicts)

    def get_user_transactions(self, offset=0, limit=100, sort='desc', book='btc_cad'):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/user_transactions',
                                 data={'key': self.apiKey, 'signature': signature, 'nonce': nonce, 'offset':offset,'limit':limit,'sort':sort,'book':book})
        return self._handle_response(response, parse = self.parseDicts)

    def get_order_book(self):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/order_book', data={'key':self.apiKey,'signature':signature,'nonce':nonce})
        return self._handle_response(response, parse = self.parseDicts)

    def get_current_trading_info(self):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/ticker', data={'key':self.apiKey,'signature':signature,'nonce':nonce})
        return self._handle_response(response, parse = self.parseDicts)

    def get_open_orders(self, book='btc_cad'):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/open_orders',
                                 data={'key': self.apiKey, 'signature': signature, 'nonce': nonce, 'book': book})
        return self._handle_response(response, parse = self.parseDicts)

    def lookup_order(self, id = ''):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/lookup_order',
                                 data={'key': self.apiKey, 'signature': signature, 'nonce': nonce, 'id': id})
        return self._handle_response(response, parse = self.parseDicts)

    def cancel_order(self, id = ''):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/cancel_order',
                                 data={'key': self.apiKey, 'signature': signature, 'nonce': nonce, 'id': id})
        return self._handle_response(response, parse = False)

    def buy_order_limit(self, amount, price, book='btc_cad'):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/buy',
                                 data={'key': self.apiKey, 'signature': signature, 'nonce': nonce, 'amount':amount, 'price':price, 'book':book})
        return self._handle_response(response, parse = self.parseDicts)

    def buy_order_market(self, amount, book='btc_cad'):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/buy',
                                 data={'key': self.apiKey, 'signature': signature, 'nonce': nonce, 'amount':amount, 'book':book})
        return self._handle_response(response, parse = self.parseDicts)

    def sell_order_limit(self, amount, price, book='btc_cad'):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/sell',
                                 data={'key': self.apiKey, 'signature': signature, 'nonce': nonce, 'amount':amount, 'price':price, 'book':book})
        return self._handle_response(response, parse = self.parseDicts)

    def sell_order_market(self, amount, book='btc_cad'):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/sell',
                                 data={'key': self.apiKey, 'signature': signature, 'nonce': nonce, 'amount':amount, 'book':book})
        return self._handle_response(response, parse = self.parseDicts)

    def bitcoin_deposit(self):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/bitcoin_deposit_address',
                                 data={'key': self.apiKey, 'signature': signature, 'nonce': nonce})
        return self._handle_response(response, parse = False)

    def bitcoin_withdrawal(self, amount, address):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/bitcoin_withdrawal',
                                 data={'key': self.apiKey, 'signature': signature, 'nonce': nonce, 'amount':amount, 'address':address})
        return self._handle_response(response, parse = False)

    def ether_deposit(self):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/ether_deposit_address',
                                 data={'key': self.apiKey, 'signature': signature, 'nonce': nonce})
        return self._handle_response(response, parse = False)

    def ether_withdrawal(self, amount, address):
        signature, nonce = self.generate_signature()
        response = requests.post('https://api.quadrigacx.com/v2/ether_withdrawal',
                                 data={'key': self.apiKey, 'signature': signature, 'nonce': nonce, 'amount':amount, 'address':address})
        return self._handle_response(response, parse = False)

    def _handle_response(self, response, parse = False):
        if response.status_code == 200:
            if parse:
                return response.json()
            else:
                return response.text
        else:            
            if parse:
                return {'error': 'code: ' + str(response.status_code)}
            else:
                return 'error - code: ' + str(response.status_code)
