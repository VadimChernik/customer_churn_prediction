import requests

# Here is your API url:
url = 'http://localhost:9696/predict'

# Here are your customer characteristics, in a dict:
client = {
    "citytier": "3",
    "preferredlogindevice": "Mobile Phone",
    "preferredpaymentmode": "Debit Card",
    "satisfactionscore": "5",
    "gender": "Male",
    "complain": "1",
    "preferedordercat": "Laptop & Accessory",
    "maritalstatus": "Single",
    "tenure": 1.0,
    "warehousetohome": 30.0,
    "hourspendonapp": 3.0,
    "numberofdeviceregistered": 3,
    "numberofaddress": 9,
    "orderamounthikefromlastyear": 11.0,
    "couponused": 1.0,
    "ordercount": 1.0,
    "daysincelastorder": 5.0,
    "cashbackamount": 159.93
}

# Here your get your response from your API using the customer above
response = requests.post(url, json=client).json()
print(response)
