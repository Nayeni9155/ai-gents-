import requests, os

TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"

def get_token():
    r = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": os.getenv("AMADEUS_CLIENT_ID"),
            "client_secret": os.getenv("AMADEUS_CLIENT_SECRET"),
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return r.json()["access_token"]

def search_flights(from_city, to_city, date, passengers):
    token = get_token()
    r = requests.get(
        FLIGHT_URL,
        headers={"Authorization": f"Bearer {token}"},
        params={
            "originLocationCode": from_city,
            "destinationLocationCode": to_city,
            "departureDate": date,
            "adults": passengers
        }
    )
    offer = r.json()["data"][0]
    return {
        "airline": offer["validatingAirlineCodes"][0],
        "price": float(offer["price"]["total"])
    }

def book_flight(airline, price):
    return {"pnr": "FL12345", "status": "BOOKED", "airline": airline}
