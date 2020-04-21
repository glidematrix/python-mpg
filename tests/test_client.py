
import sys
import os
from pprint import pprint

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError as e:
    pass


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
    receipt_url='http://127.0.0.1:8080/receipt'
)

# Generate 3rd Party Payment Link
# link = client.payment_link(amount)
# print(link)


# TEST Card
card = {
    'cardnum': '5204740009900014',
    'expiry': 2212,
    'csc': 123,
}


client.load_card({
    'amount': amount,
    'currency': currency,
    **card
})

pprint({**client.card_payload})

res = client.process_card()


pprint(res)
