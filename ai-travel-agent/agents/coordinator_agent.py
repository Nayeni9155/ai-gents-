from agents.flight_agent import flight_agent
from agents.hotel_agent import hotel_agent
from agents.payment_agent import payment_agent

def coordinator_agent(user_input):
    flight = flight_agent({
        "from_city": "HYD",
        "to_city": "DXB",
        "date": "2026-02-10",
        "passengers": 1
    })

    hotel = hotel_agent({
        "city": "Dubai",
        "checkin": "2026-02-10",
        "checkout": "2026-02-13"
    })

    total_amount = flight["price"] + hotel["price"]
    payment = payment_agent(total_amount)

    return {
        "flight": flight,
        "hotel": hotel,
        "payment": payment
    }
