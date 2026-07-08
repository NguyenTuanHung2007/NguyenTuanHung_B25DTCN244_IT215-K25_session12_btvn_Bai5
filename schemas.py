from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DiscountResponse(BaseModel):
    id: int
    code: str
    is_deleted: bool
    deleted_at: Optional[datetime]

    class Config:
        from_attributes = True