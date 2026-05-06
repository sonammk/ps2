from services.scoring import score_candidate


class Dispatcher:
    def __init__(self, graph, weights):
        self.graph = graph
        self.weights = weights

    def choose_assignment(self, order, agents):
        candidates = [agent for agent in agents if agent.availability]
        if not candidates:
            return None
        return max(candidates, key=lambda agent: score_candidate(agent, order, self.graph, self.weights))
