from dataclasses import dataclass, field


@dataclass
class Agent:
    agent_id: str
    current_location: tuple[int, int]
    rating: float
    active_orders: list[str] = field(default_factory=list)
    cumulative_assignments: int = 0
    availability: bool = True

    def refresh_availability(self, max_active_orders: int = 2) -> None:
        self.availability = len(self.active_orders) < max_active_orders
