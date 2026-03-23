from src.contracts import SimulationResult, SimulationStep
from src.metrics import compute_metrics


def lru(frames: int, reference_string: list[int]) -> SimulationResult:
    if frames <= 0:
        raise ValueError("Number of frames must be greater than 0.")

    frame_slots: list[int | None] = [None] * frames
    last_used_at: dict[int, int] = {}
    faults = 0
    steps: list[SimulationStep] = []

    for index, page in enumerate(reference_string, start=1):
        page_in_memory = page in frame_slots

        if page_in_memory:
            is_fault = False
        else:
            is_fault = True
            faults += 1

            if None in frame_slots:
                empty_index = frame_slots.index(None)
                frame_slots[empty_index] = page
            else:
                victim_index = min(
                    range(len(frame_slots)),
                    key=lambda slot_index: last_used_at.get(frame_slots[slot_index], -1),
                )
                frame_slots[victim_index] = page

        last_used_at[page] = index

        steps.append(
            SimulationStep(
                index=index,
                requested_page=page,
                frames_after=frame_slots.copy(),
                is_fault=is_fault,
            )
        )

    total_requests = len(reference_string)
    computed_faults, hits, failure_rate, success_rate = compute_metrics(total_requests, faults)

    return SimulationResult(
        algorithm_name="LRU",
        number_of_pages=total_requests,
        number_of_frames=frames,
        reference_string=reference_string,
        steps=steps,
        page_interrupts=computed_faults,
        faults=computed_faults,
        hits=hits,
        failure_rate=failure_rate,
        success_rate=success_rate,
    )
