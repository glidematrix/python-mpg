import os
import sys
from flask import Flask, render_template, jsonify, request

from pprint import pprint


try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError as e:
    pass

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from mpg import Client

app = Flask(__name__)


merchant_id = os.getenv('merchant_id')
access_code = os.getenv('access_code')
secret = os.getenv('secret')
currency = 'ZMW'
amount = 1

client = Client(
    merchant_id,
    access_code,
    secret,
    currency,
    receipt_url='http://127.0.0.1:8080/receipt'
)


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/payment-link')
def payment_link():

    link = client.payment_link(amount)
    # print(link)

    res = {
        "res": "Generate 3 Party Link",
        "payment_link": link
    }

    return jsonify(res)


@app.route('/receipt')
def receipt():

    req_data = request.args

    res_data = {
        **req_data
    }

    res_data['txn_is_verified'] = client.verify_txn(res_data)

    return jsonify(res_data)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )
