from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from app.models.item import Item, ItemCreate

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Item not found"}},
)

# In-memory database for demonstration
items_db = []
item_id_counter = 0

@router.get("/", response_model=List[Item])
async def read_items(skip: int = 0, limit: int = 10):
    """Get a list of items with pagination."""
    return items_db[skip : skip + limit]

@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int):
    """Get a specific item by ID."""
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.post("/", response_model=Item, status_code=201)
async def create_item(item: ItemCreate):
    """Create a new item."""
    global item_id_counter
    item_id_counter += 1
    new_item = Item(id=item_id_counter, **item.model_dump())
    items_db.append(new_item)
    return new_item

@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemCreate):
    """Update an existing item."""
    for i, existing_item in enumerate(items_db):
        if existing_item.id == item_id:
            updated_item = Item(id=item_id, **item.model_dump())
            items_db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int):
    """Delete an item."""
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Item not found")