def complete_delivery(agent, order):
    order.state = "DELIVERED"
    agent.current_location = order.location
    if order.order_id in agent.active_orders:
        agent.active_orders.remove(order.order_id)
    agent.refresh_availability()
    return order
