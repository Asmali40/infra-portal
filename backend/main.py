from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Bestellung(BaseModel):
  service_type_id: int
  name: str

SERVICE_TYPES = [
  {"id": 1, "name": "PostgreSQL", "description": "Relationale Datenbank"},
  {"id": 2, "name": "Message Queue", "description": "RabbitMQ Broker"},
  {"id": 3, "name": "Container", "description": "Container-Umgebung"},
]

@app.get("/services")
def vorhandene_services():
  return SERVICE_TYPES

@app.post("/requests")
def bestellen(bestellung: Bestellung):
  return {"status": "provisioning", "name": bestellung.name}
