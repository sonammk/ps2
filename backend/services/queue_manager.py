import heapq


PRIORITY_ORDER = {
    "high": 0,
    "normal": 1,
    "low": 2,
}


class OrderQueue:
    def __init__(self):
        self._items = []

    def push(self, order):
        priority = PRIORITY_ORDER.get(order.priority, 1)
        heapq.heappush(self._items, (priority, order.timestamp, order.order_id, order))

    def pop(self):
        if not self._items:
            return None
        return heapq.heappop(self._items)[-1]

    def depth(self):
        return len(self._items)
