import requests
import keys
import encode
import access_token

from datetime import datetime
from requests.auth import HTTPBasicAuth


def lipa_na_mpesa():
    generated_access_token = access_token.access_token_generator()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {"Authorization": "Bearer %s" % generated_access_token}

    request = {
        "BusinessShortCode": keys.business_short_code,
        "Password": encode.encode_password(),  # is a base64 encoded utf-8 string format consisting of
        # Shortcode+Passkey+Timestamp
        "Timestamp": encode.sys_time(),  # current system date + time
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_short_code,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://mydomain.com/pat",
        "AccountReference": 5514749,
        "TransactionDesc": "Ness Cakes Bakery"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


lipa_na_mpesa()
