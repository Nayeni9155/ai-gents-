import requests

def payment_agent(amount):
    r = requests.post(
        "http://localhost:8001/tools/create_payment",
        json={"amount": amount}
    )
    return r.json()
