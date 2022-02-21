import requests
import keys

access_token = "access_token"

api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

headers = { "Authorization": "Bearer %s" % access_token }

request = {
    "BusinessShortCode": keys.business_short_code,
    "Password": "",
    "Timestamp":"",
    "TransactionType": "CustomerPayBillOnline",
    "Amount":"1",
    "PartyA":"",
    "PartyB":"",
    "PhoneNumber":"",
    "CallBackURL":"https://mydomain.com/pat",
    "AccountReference":"Lipa na Mpesa Test Push",
    "TransactionDesc":""
}

response = requests.post(api_url, json = request, headers = headers)

print(response.text)