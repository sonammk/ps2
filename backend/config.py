from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

MAX_ACTIVE_ORDERS_PER_AGENT = 2
DECISION_LATENCY_TARGET_MS = 500
THROUGHPUT_TARGET_ORDERS_PER_MINUTE = 100

SCORING_WEIGHTS = {
    "delivery_time": 0.35,
    "sla_risk": 0.25,
    "workload_fairness": 0.20,
    "priority": 0.15,
    "rating": 0.05,
}
