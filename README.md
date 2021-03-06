[![Build Status](https://travis-ci.com/glidematrix/python-mpg.svg?branch=master)](https://travis-ci.com/glidematrix/python-mpg)
![GitHub](https://img.shields.io/github/license/glidematrix/python-mpg)
![Twitter Follow](https://img.shields.io/twitter/follow/glidematrix?style=social)

# Python MPG (Mastercard Payment Gateway)

MPG (Mastercard Payment Gateway) formerly MIGS python package to integrate through Virtual Payment
Client Integration.

## Install

Install with pip:

`pip install git+https://git@github.com/glidematrix/python-mpg.git`

### Initialize

```python

from mpg import Client

merchant_id = 'YOUR MERCHANT ID'
access_code = 'YOUR ACCESS CODE'
secret = 'YOUR SECRET'
currency = 'ZMW' #The currency you want to process


client = Client(
    merchant_id,
    access_code,
    secret,
    currency,
)


```

### 2-Party Transactions

```python

payload = {
    'amount': 10,
    'cardnum': '5204740009900014', #Test card number
    'expiry': 2212, #Expiry Year and Month in format 2212
    'csc': 123, #Card Security Code[CVV etc]
}

client.load_card(payload)

res = client.process_card()

print(res)

```

### 3-Party Transactions

```python

amount = 10

link = client.payment_link(amount)
print(link)


```
