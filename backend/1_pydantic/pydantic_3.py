from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from pathlib import Path

class Product(BaseModel):
    name: str
    created_at: datetime
    price: float = Field(..., gt=0)
    note: Optional[str] = None

fpath = Path(...)

model = Product.parse_file(fpath)
model.name = "本"
fpath.write_text(model.json())

