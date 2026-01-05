import requests, os

def search_hotels(city, checkin, checkout):
    url = "https://booking-com.p.rapidapi.com/v1/hotels/search"
    headers = {
        "X-RapidAPI-Key": os.getenv("BOOKING_API_KEY"),
        "X-RapidAPI-Host": "booking-com.p.rapidapi.com"
    }
    params = {
        "dest_type": "city",
        "dest_id": city,
        "checkin_date": checkin,
        "checkout_date": checkout,
        "order_by": "popularity"
    }
    r = requests.get(url, headers=headers, params=params)
    h = r.json()["result"][0]
    return {
        "hotel": h["hotel_name"],
        "price": float(h["min_total_price"])
    }

def book_hotel(hotel, price):
    return {"booking_id": "HT67890", "status": "BOOKED"}
