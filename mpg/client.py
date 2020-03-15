import hmac
import requests
from collections import OrderedDict
from hashlib import sha256
from urllib.parse import urlencode, parse_qs, quote
from time import time


class Client:
    """docstring for Mastercard Payment Gateway Client"""

    def __init__(self, merchant_id, access_code, secret, currency, locale='en_US', receipt_url='http://127.0.0.1/receipt', is_test=True):
        base_url_test = 'https://migs-mtf.mastercard.com.au'
        base_url_prod = 'https://migs.mastercard.com.au'
        self.merchant_id = merchant_id
        self.access_code = access_code
        self.secret = secret
        self.currency = currency
        self.locale = locale
        self.receipt_url = receipt_url
        self.base_url = base_url_test if is_test else base_url_prod

    def gen_hash(self, data):
        '''
        generates hash from ordered dictionary
        '''
        data_str = '&'.join(f'{key}={val}' for (key, val) in data.items())
        generated_hash = hmac.new(bytes.fromhex(self.secret),
                                  data_str.encode(),
                                  sha256).hexdigest().upper()
        return generated_hash

    def payment_link(self, amount):
        '''
        Takes in an amount and generates a payment link for 3rd party payments
        '''

        vpc_OrderInfo = f"Order_{int(time())}"
        vpc_MerchTxnRef = f"Ref_{int(time())}"

        vpc_Amount = int(amount * 100)

        data = {
            'vpc_OrderInfo': vpc_OrderInfo,
            'vpc_MerchTxnRef': vpc_MerchTxnRef,
            'vpc_Amount': vpc_Amount,
            'vpc_ReturnURL': self.receipt_url,
            'vpc_Version': 1,
            'vpc_Command': 'pay',
            'vpc_Merchant': self.merchant_id,
            'vpc_AccessCode': self.access_code,
            'vpc_Currency': self.currency,
            'vpc_Locale': self.locale,
        }

        data = OrderedDict(sorted(data.items()))

        data['vpc_SecureHash'] = self.gen_hash(data)

        data['vpc_SecureHashType'] = 'SHA256'

        urlencoded_data_str = urlencode(data)

        link = f"{self.base_url}/vpcpay?{urlencoded_data_str}"

        return link

    def load_card(self, data):
        '''
            Load card details and amount for 2nd Party Transaction.
            Process 2nd Party Transaction.
        '''
        vpc_OrderInfo = f"Order_{int(time())}"
        vpc_MerchTxnRef = f"Ref_{int(time())}"
        vpc_Amount = int(data.get('amount') * 100)
        # vpc_Currency = data.get('currency', 'ZMW')
        vpc_Currency = self.currency
        vpc_CardNum = data.get('cardnum')
        vpc_CardExp = data.get('expiry')
        vpc_CardSecurityCode = data.get('csc')
        payload_data = {
            'vpc_AccessCode': self.access_code,
            'vpc_Merchant': self.merchant_id,
            'vpc_Amount': vpc_Amount,
            'vpc_OrderInfo': vpc_OrderInfo,
            'vpc_MerchTxnRef': vpc_MerchTxnRef,
            'vpc_Command': 'pay',
            'vpc_Currency': vpc_Currency,
            'vpc_Locale': 'en_US',
            'vpc_Version': 1,
            'vpc_CardNum': vpc_CardNum,
            'vpc_CardExp': vpc_CardExp,  # YYMM
            'vpc_CardSecurityCode': vpc_CardSecurityCode,
        }
        payload_data = OrderedDict(sorted(payload_data.items()))
        payload_data['vpc_SecureHash'] = self.gen_hash(payload_data)
        payload_data['vpc_SecureHashType'] = 'SHA256'

        self.card_payload = payload_data

        # r = requests.post(f"{self.base_url}/vpcdps", data=payload_data)

        # return parse_qs(r.text)
    def process_card(self):
        '''
            Process 2nd Party Transaction.
        '''
        r = requests.post(f"{self.base_url}/vpcdps", data=self.card_payload)

        return parse_qs(r.text)
