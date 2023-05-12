import requests
import json


# api.1
def signin():
    url = "http://127.0.0.1:8000/Payment_weha/signin/"

    payload = {"username": "zhengdu", "password": "Beijing"}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def signup():
    url = "http://127.0.0.1:8000/Payment_weha/signup/"

    payload = {"username": "zhengdu", "password": "123456", "name": "zd"}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def deposit():
    url = "http://127.0.0.1:8000/Payment_weha/deposit/"

    payload = {"uid": 1}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def information():
    url = "http://127.0.0.1:8000/Payment_weha/Payment_information/"

    payload = {"order_id": 9, "seat_price": 20, "air_name": "airline_xyf10"}
    post = requests.post(url, json=payload)
    res = post
    data = res.json()
    print(data)


def statement():
    url = "http://127.0.0.1:8000/Payment_weha/statement/"

    payload = {"uid": 1}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def order():
    url = "http://127.0.0.1:8000/Payment_weha/Payment_order/"

    payload = {"uid": 1, "Airline_order": 1}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def check():
    url = "http://127.0.0.1:8000/Payment_weha/Payment_check/"

    payload = {"state": True, "order_id": 1}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def returnn():
    url = "http://127.0.0.1:8000/Payment_weha/Payment_return/"

    payload = {"state": "unsuccessful", "order_id": 1}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def transfer():
    url = "http://127.0.0.1:8000/Payment_weha/transfer/"

    payload = {"uid": 2, "password": "123456", "u2": "cty", "u3": "cty", "money":1}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


def balance():
    url = "http://127.0.0.1:8000/Payment_weha/balance/"

    payload = {"uid": 3}
    res = requests.post(url, json=payload)
    data = res.json()
    print(data)


if __name__ == '__main__':
    signin()
    signup()
    deposit()
    information()
    statement()
    order()
    check()
    returnn()
    transfer()
    balance()
