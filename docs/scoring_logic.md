# Scoring Logic

Candidate agents are scored using delivery speed, SLA risk, workload fairness, priority handling, and agent rating. The weights live in `backend/config.py` so the team can tune the trade-off between faster delivery, lower SLA breach rate, and fairer assignment distribution.
