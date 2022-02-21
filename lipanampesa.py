import requests
import keys
import base64


from datetime import datetime


ctime = datetime.now().strftime("%Y%m%d%H%M%S") # convert the current sys time to string using (strftime)
print(ctime)

data_to_encode = keys.business_short_code + keys.lipa_na_mpesa_passkey + ctime # collection of parameters that make the password variable
encode_data = base64.b64encode(data_to_encode.encode()) # encode the data to a base64 format
password = encode_data.decode('utf-8') # change the byte-like to str by decoding
print(password)


def lipa_na_mpesa():
    access_token = "access_token"

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = { "Authorization": "Bearer %s" % access_token }

    request = {
        "BusinessShortCode": keys.business_short_code,
        "Password": password,  # is a base64 encoded utf-8 string format consisting of Shortcode+Passkey+Timestamp
        "Timestamp": ctime,  # current system date + time
        "TransactionType": "CustomerPayBillOnline",
        "Amount":"1",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_short_code,
        "PhoneNumber": keys.phone_number,
        "CallBackURL":"https://mydomain.com/pat",
        "AccountReference":"Ness cakes mpesa",
        "TransactionDesc":"Lipa na Mpesa Test STK Push"
    }

    response = requests.post(api_url, json = request, headers = headers)

    print(response.text)

#lipa_na_mpesa()
