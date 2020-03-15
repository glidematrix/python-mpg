import sys
import os

from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from mpg import Client


merchant_id = os.getenv('merchant_id')
access_code = os.getenv('access_code')
secret = os.getenv('secret')
currency = 'ZMW'


# pprint(os.environ)
# pprint(os.getenv('merchant_id'))

amount = 1

client = Client(
    merchant_id,
    access_code,
    secret,
    currency,
)

# Generate 3rd Party Payment Link
# link = client.payment_link(amount)
# print(link)


# TEST Card
# card = {
#     'cardnum': '5204740009900014',
#     'expiry': 2212,
#     'csc': 123,
# }


# client.load_card({
#     'amount': amount,
#     'currency': currency,
#     **card
# })

# res = client.process_card()

# pprint(res)
