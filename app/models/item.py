from pydantic import BaseModel, Field
from typing import Optional

class ItemBase(BaseModel):
    """Base model for item data."""
    name: str = Field(..., description="The name of the item", min_length=1, max_length=100)
    description: Optional[str] = Field(None, description="The description of the item")
    price: float = Field(..., description="The price of the item", gt=0)
    is_available: bool = Field(True, description="Whether the item is available")

class ItemCreate(ItemBase):
    """Model for creating a new item."""
    pass

class Item(ItemBase):
    """Model for an item with ID."""
    id: int = Field(..., description="The unique identifier of the item")
    
    class Config:
        from_attributes = True