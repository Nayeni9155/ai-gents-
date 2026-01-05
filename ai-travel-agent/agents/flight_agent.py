import requests

def flight_agent(data):
    r = requests.post(
        "http://localhost:8001/tools/search_flights",
        json=data
    )
    return r.json()
