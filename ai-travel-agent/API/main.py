from fastapi import FastAPI
from agents.coordinator_agent import coordinator_agent

app = FastAPI(title="AI Travel API")

@app.post("/chat")
def chat(data: dict):
    return coordinator_agent(data["message"])
