import unittest

import sys
import os

from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from mpg import Client


# python -m unittest teting

class TestGateway(unittest.TestCase):

    def setUp(self):
        self.merchant_id = os.getenv('merchant_id')
        self.access_code = os.getenv('access_code')
        self.secret = os.getenv('secret')
        self.currency = 'ZMW'
        self.amount = 1

        self.client = Client(
            self.merchant_id,
            self.access_code,
            self.secret,
            self.currency,
        )

    def test_process_card(self):
        card = {
            'cardnum': '5204740009900014',
            'expiry': 2212,
            'csc': 123,
        }

        self.client.load_card({
            'amount': self.amount,
            'currency': self.currency,
            **card
        })

        res = self.client.process_card()

        vpc_Message, *_ = res.get('vpc_Message')

        self.assertEqual(vpc_Message, 'Approved')


if __name__ == '__main__':
    unittest.main()
