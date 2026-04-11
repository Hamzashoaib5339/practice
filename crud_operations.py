from fastapi import FastAPI

app = FastAPI()

items = []
@app.post("/add")
def add_item(name: str):
    items.append(name)
    return {"message": "added", "items": items}
@app.get("/items")
def get_items():
    return items
@app.put("/update/{index}")
def update_item(index: int, name: str):
    items[index] = name
    return {"message": "updated", "items": items}
@app.delete("/delete/{index}")
def delete_item(index: int):
    items.pop(index)
    return {"message": "deleted", "items": items}