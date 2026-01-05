from fastapi import FastAPI
from mcp_server.tools.flight_tools import search_flights, book_flight
from mcp_server.tools.hotel_tools import search_hotels, book_hotel
from mcp_server.tools.payment_tools import create_payment

app = FastAPI(title="MCP Travel Server")

@app.post("/tools/search_flights")
def flight_search(data: dict):
    return search_flights(**data)

@app.post("/tools/book_flight")
def flight_book(data: dict):
    return book_flight(**data)

@app.post("/tools/search_hotels")
def hotel_search(data: dict):
    return search_hotels(**data)

@app.post("/tools/book_hotel")
def hotel_book(data: dict):
    return book_hotel(**data)

@app.post("/tools/create_payment")
def payment(data: dict):
    return create_payment(**data)
