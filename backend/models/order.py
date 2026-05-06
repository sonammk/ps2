from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    order_id: str
    timestamp: datetime
    location: tuple[int, int]
    prep_time_minutes: int
    priority: str
    sla_minutes: int
    state: str = "PENDING"
