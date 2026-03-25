import json
import os
import sys
from typing import Callable


def _load_algorithms() -> dict[str, Callable[[int, list[str]], object]]:
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

    from src.fifo import fifo
    from src.lru import lru
    from src.mru import mru
    from src.optimal import optimal
    from src.second_chance import second_chance

    return {
        "FIFO": fifo,
        "LRU": lru,
        "MRU": mru,
        "OPTIMAL": optimal,
        "SECOND_CHANCE": second_chance,
        "SECOND CHANCE": second_chance,
    }


def _to_page_list(values: list[object]) -> list[str]:
    parsed: list[str] = []
    for value in values:
        token = str(value).strip()
        if not token:
            raise ValueError("Reference string contains an empty page token.")
        parsed.append(token)
    return parsed


def _serialize_frames(frames_after: list[str | None]) -> str:
    return "[" + " ".join("-" if item is None else str(item) for item in frames_after) + "]"


def run() -> None:
    raw = sys.stdin.read().strip()
    if not raw:
        raise ValueError("Request body is empty.")

    payload = json.loads(raw)
    algorithm = str(payload.get("algorithm", "")).strip().upper()
    frames = int(payload.get("frames", 0))
    reference_raw = payload.get("referenceString", [])

    if not algorithm:
        raise ValueError("Algorithm is required.")
    if frames <= 0:
        raise ValueError("Frames must be greater than 0.")
    if not isinstance(reference_raw, list) or len(reference_raw) == 0:
        raise ValueError("Reference string is required.")

    reference_string = _to_page_list(reference_raw)

    algorithm_map = _load_algorithms()
    simulation_fn = algorithm_map.get(algorithm)
    if simulation_fn is None:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    result = simulation_fn(frames, reference_string)

    response = {
        "algorithm": result.algorithm_name,
        "pageFaults": result.faults,
        "pageHits": result.hits,
        "failureRate": result.failure_rate,
        "successRate": result.success_rate,
        "totalReferences": result.number_of_pages,
        "steps": [
            {
                "page": step.requested_page,
                "frames": _serialize_frames(step.frames_after),
                "result": "FAULT" if step.is_fault else "HIT",
            }
            for step in result.steps
        ],
    }

    print(json.dumps(response))


if __name__ == "__main__":
    try:
        run()
    except NotImplementedError as error:
        print(json.dumps({"error": str(error)}))
        sys.exit(2)
    except Exception as error:
        print(json.dumps({"error": str(error)}))
        sys.exit(1)
