# Smart Delivery Dispatch System

## Team Information
- **Team Name**: codezilla
- **Year**: 2026
- **All-Female Team**: yes

## Architecture Overview
Our system works like a smart dispatcher that looks at every incoming order and decides which delivery agent is the best fit at that moment. Orders are first checked for valid data and then arranged in a queue, where high-priority orders get attention first and older orders are handled before newer ones within the same priority level.

When an order needs to be assigned, the system checks which agents are available, how far they are from the order location, how many deliveries they are already handling, and how reliable they are based on rating. It then gives each possible agent-order match a score. The score balances fast delivery, SLA deadlines, priority orders, fair workload distribution, and agent rating.

After choosing the best agent, the system updates the order and agent states together so the data stays consistent. If no agent is free, the order simply waits in the queue and is retried when an agent completes a delivery. As deliveries happen, the system tracks delivery time, SLA breaches, and workload fairness, then reports these metrics in JSON and summary form.

#### Describe your approach here. Keep it short and clear.

    - What is your dispatch strategy?
    - How do you score agents for incoming orders?
    - How do you manage SLA deadlines, priority orders, and agent capacity?
    - What are the main steps in your pipeline?
    Our approach uses a priority-based real-time dispatch system. Incoming orders are validated and placed in a queue where high-priority orders are handled first, and orders with the same priority follow arrival time.

For each order, the system checks agents who are available, have fewer than 2 active orders, and can reach the order location through the graph. Each feasible agent is scored using estimated delivery time, SLA urgency, current workload, order priority, and agent rating. The best-scoring agent is selected for assignment.

SLA deadlines are managed by giving urgent orders higher weight during scoring and tracking any breaches after delivery. Priority orders are handled through the queue, while agent capacity is enforced by limiting each agent to 2 active orders. Agents become available again after completing deliveries.

The pipeline is: load and validate CSV data, build the environment graph, queue orders, generate feasible agent candidates, score candidates, assign the best agent, update order and agent states, retry pending orders when agents free up, and export delivery, SLA, and fairness metrics.

    


**Note:** Please do not change the format or spelling of anything in this README. The fields are extracted using a script, so any changes to the structure or formatting may break the extraction process.
