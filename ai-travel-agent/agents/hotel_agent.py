import requests

def hotel_agent(data):
    r = requests.post(
        "http://localhost:8001/tools/search_hotels",
        json=data
    )
    return r.json()
