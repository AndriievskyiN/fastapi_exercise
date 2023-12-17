from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

app = FastAPI()

inventory = {
    1: {
        "name": "iPhone",
        "price": 3.99,
        "brand": "Apple"
    }
}

@app.get("/")
def home():
    return {"Data": "Testing 1"}

@app.get("/about")
def about():
    return {"Data": "About"}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item you would like to view")):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    
    return {"Data": "Not Found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    
    inventory[item_id] = item
    return inventory[item_id]
