from types import SimpleNamespace

from backend.config import SCORING_WEIGHTS
from backend.services.scoring import score_candidate


def test_high_priority_agent_score_is_numeric():
    agent = SimpleNamespace(rating=4.5, cumulative_assignments=0)
    order = SimpleNamespace(priority="high")
    assert isinstance(score_candidate(agent, order, graph=None, weights=SCORING_WEIGHTS), float)
