from flask import Flask, jsonify, render_template, request
import requests
import webbrowser
import time

app = Flask(__name__)

def get_price():
    url = "http://api.coincap.io/v2/assets?"
    response = requests.request("GET", url, headers={}, data = {})
    if response.status_code == 200:
        data=response.json()['data'][0]['priceUsd']
        print(data)
        return data
    else:
        print("Error")  
        return 0


@app.route('/Crypto_Price', methods = ['GET'])
def stuff():
    price=get_price()
    return jsonify(result=price)


@app.route('/')
def index():
    return render_template('index.html')
# main driver function
if __name__ == '__main__':

	app.run(debug=True, host='localhost', port=4444)
