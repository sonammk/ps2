from dataclasses import dataclass, field


@dataclass
class Graph:
    adjacency: dict[tuple[int, int], list[tuple[tuple[int, int], float]]] = field(default_factory=dict)

    def add_edge(self, start: tuple[int, int], end: tuple[int, int], travel_time: float) -> None:
        self.adjacency.setdefault(start, []).append((end, travel_time))
        self.adjacency.setdefault(end, [])

    def locations(self) -> set[tuple[int, int]]:
        return set(self.adjacency)
