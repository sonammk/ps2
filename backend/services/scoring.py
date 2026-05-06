PRIORITY_BOOST = {
    "high": 1.0,
    "normal": 0.5,
    "low": 0.2,
}


def score_candidate(agent, order, graph, weights):
    workload_penalty = agent.cumulative_assignments
    priority_score = PRIORITY_BOOST.get(order.priority, 0.0)
    rating_score = agent.rating / 5

    return (
        weights["priority"] * priority_score
        + weights["rating"] * rating_score
        - weights["workload_fairness"] * workload_penalty
    )
