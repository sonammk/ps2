from datetime import datetime
from types import SimpleNamespace

from backend.services.queue_manager import OrderQueue


def test_queue_prioritizes_high_orders():
    queue = OrderQueue()
    queue.push(SimpleNamespace(order_id="low", priority="low", timestamp=datetime(2026, 5, 3, 9, 0)))
    queue.push(SimpleNamespace(order_id="high", priority="high", timestamp=datetime(2026, 5, 3, 9, 1)))
    assert queue.pop().order_id == "high"
