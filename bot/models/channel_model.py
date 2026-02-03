from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class Channel(BaseModel):
    name: str
    username: str
    subscriber_count: int
    category: Optional[str] = None
    source: str = "tgstat"
    keyword: Optional[str] = None
    scraped_at: Optional[datetime] = None
