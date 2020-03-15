import requests
from urllib.parse import urlencode, parse_qs


class Ama:
    '''
        Advanced Merchant Admnistration
    '''

    def __init__(self, user, password, merchant_id, access_code, secret, currency, locale='en_US', is_test=True):
        base_url_test = 'https://migs-mtf.mastercard.com.au'
        base_url_prod = 'https://migs.mastercard.com.au'

        self.user = user
        self.password = password
        self.merchant_id = merchant_id
        self.access_code = access_code
        self.secret = secret
        self.currency = currency
        self.locale = locale
        self.base_url = base_url_test if is_test else base_url_prod

    def refund(self, merchant_txn_ref, txn_num, order_info, amount):
        payload = {
            'vpc_Version': '1',
            'vpc_Command': 'refund',
            'vpc_MerchTxnRef': merchant_txn_ref,
            'vpc_TransNo': txn_num,
            'vpc_OrderInfo': order_info,
            'vpc_Amount': int(amount * 100),
            'vpc_AccessCode': self.access_code,
            'vpc_Merchant': self.merchant_id,
            'vpc_User': self.user,
            'vpc_Password': self.password
        }

        r = requests.post(f"{self.base_url}/vpcdps", data=payload)

        return parse_qs(r.text)

    def qry_txn(self, merchant_txn_ref):
        payload = {
            "vpc_Version": '1',
            "vpc_Command": 'queryDR',
            "vpc_MerchTxnRef": merchant_txn_ref,
            'vpc_AccessCode': self.access_code,
            'vpc_Merchant': self.merchant_id,
            'vpc_User': self.user,
            'vpc_Password': self.password
        }

        r = requests.post(f"{self.base_url}/vpcdps", data=payload)

        return parse_qs(r.text)
