def require_fields(row, required_fields):
    missing = [field for field in required_fields if not row.get(field)]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
