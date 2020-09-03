import base64
from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token
import keys



#print(datetime.now())
#2020-09-01 20:15:44.178417
unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

#print(formatted_time, "This is the formatted time")

data_to_encode = keys.business_shortCode + keys.lipa_na_mpesa_passkey + formatted_time
encoded_string = base64.b64encode(data_to_encode.encode())
#print(encoded_string)
decoded_password = encoded_string.decode("utf-8")


#print(my_access_token, "this should be an access token")

def lipa_na_mpesa():

	access_token = generate_access_token()
	api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

	headers = { "Authorization": "Bearer %s" % access_token }

	request = {
		"BusinessShortCode": keys.business_shortCode,
		"Password": decoded_password,
		"Timestamp": formatted_time,
		"TransactionType": "CustomerPayBillOnline",
		"Amount": "1",
		"PartyA": keys.phone_number,
		"PartyB": keys.business_shortCode,
		"PhoneNumber": keys.phone_number,
		"CallBackURL": "https://fullstackdjango.com/lipanampesa/",
		"AccountReference": "12345678",
		"TransactionDesc": "Pay School Fees"
	}

	response = requests.post(api_url, json = request, headers=headers)

	print (response.text)



lipa_na_mpesa()



























