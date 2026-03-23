def compute_metrics(total_requests: int, faults: int) -> tuple[int, int, float, float]:
    if total_requests <= 0:
        return 0, 0, 0.0, 0.0

    hits = total_requests - faults
    failure_rate = (faults / total_requests) * 100
    success_rate = (hits / total_requests) * 100
    return faults, hits, failure_rate, success_rate
