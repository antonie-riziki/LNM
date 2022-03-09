import requests
import keys
import access_token

# Customer to Business Online
# Register Url


def register_url():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {'Authorization': 'Bearer %s' % access_token.access_token_generator()}

    request = {
        "ShortCode": keys.c2bShortCode,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://mydomain.com/confirmation",
        "ValidationURL": "https://mydomain.com/validation",
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


register_url()


# simulate registered url


def simulate_c2b_payment():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": 'Bearer %s' % access_token.access_token_generator()}

    request = {
        "ShortCode": keys.c2bShortCode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "3",
        "Msisdn": keys.msisdn,  # phone number of virtual customer simulating the transaction
        "BillRefNumber": "1234567",
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


simulate_c2b_payment()
