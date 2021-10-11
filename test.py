import requests
from flask import Flask, jsonify

def get_price():
    url = "http://api.coincap.io/v2/assets?"
    response = requests.request("GET", url, headers={}, data = {}).json()
    return float(response['data'][0]['priceUsd'])

data={'num':7}
price=jsonify(data)
print(price)