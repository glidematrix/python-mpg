import unittest

import sys
import os
from pprint import pprint

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError as e:
    pass

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ama import Ama

ama_user = os.getenv('ama_user')
ama_password = os.getenv('ama_password')

merchant_id = os.getenv('merchant_id')
access_code = os.getenv('access_code')
secret = os.getenv('secret')
currency = 'ZMW'
amount = 1

ama_client = Ama(ama_user, ama_password, merchant_id,
                 access_code, secret, currency)


merchant_txn_ref = 'Ref_1584311782'
txn_num = '43'
order_info = 'Order_1584311782'
amount = 1

# res = ama_client.refund(merchant_txn_ref, txn_num, order_info, amount)

# pprint(res)
'''
{'vpc_Amount': ['100'],
 'vpc_BatchNo': ['0'],
 'vpc_Command': ['refund'],
 'vpc_Locale': ['en_US'],
 'vpc_MerchTxnRef': ['Ref_1584311782'],
 'vpc_Merchant': ['EZMT011'],
 'vpc_Message': ['I5426-03152303: Invalid Permission : advanceMA'],
 'vpc_OrderInfo': ['Order_1584311782'],
 'vpc_TransactionNo': ['0'],
 'vpc_TxnResponseCode': ['7'],
 'vpc_Version': ['1']}
'''

res = ama_client.qry_txn(merchant_txn_ref)
pprint(res)
'''
{'vpc_Amount': ['0'],
 'vpc_BatchNo': ['0'],
 'vpc_Command': ['queryDR'],
 'vpc_Locale': ['en_US'],
 'vpc_MerchTxnRef': ['Ref_1584311782'],
 'vpc_Merchant': ['EZMT011'],
 'vpc_Message': ['E5429-03152313: QueryDR Error : I5426 Context: advanceMA'],
 'vpc_TransactionNo': ['0'],
 'vpc_TxnResponseCode': ['7'],
 'vpc_Version': ['1']}
'''
