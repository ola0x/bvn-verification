import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: int

@app.get("/")
def home():
    return{"hello": "world"}

@app.get('/item/{item_id}')
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post('/items/')
def post_item(item: Item):

    return{
        "Item_name": item.name,
        "item_price": item.price
    }

# @app.post("/items/")
# def put_item(item: Item):

#     it = item.dict()
#     name = it['name']
#     price = it['price']

#     return {"item_name": name,
#             "item_price": price}


if __name__ == "__main__":
    uvicorn.run("main:app")