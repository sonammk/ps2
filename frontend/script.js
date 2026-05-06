import { renderOrders } from "./components/orders.js";
import { renderAgents } from "./components/agents.js";
import { renderMetrics } from "./components/metrics.js";

renderOrders(document.getElementById("orders"));
renderAgents(document.getElementById("agents"));
renderMetrics(document.getElementById("metrics"));
