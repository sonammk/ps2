from backend.services.dispatcher import Dispatcher


def test_dispatcher_returns_none_without_agents():
    dispatcher = Dispatcher(graph=None, weights={})
    assert dispatcher.choose_assignment(order=None, agents=[]) is None
