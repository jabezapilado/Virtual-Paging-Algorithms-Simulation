from src.contracts import SimulationResult, SimulationStep
from src.metrics import compute_metrics


def optimal(frames: int, reference_string: list[str]) -> SimulationResult:
    if frames <= 0:
        raise ValueError("Number of frames must be greater than 0.")

    frame_slots: list[str | None] = [None] * frames
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
                future = reference_string[index:]
                victim_index = 0
                farthest_next_use = -1

                for slot_index, slot_page in enumerate(frame_slots):
                    if slot_page is None:
                        continue

                    try:
                        next_use = future.index(slot_page)
                    except ValueError:
                        victim_index = slot_index
                        break

                    if next_use > farthest_next_use:
                        farthest_next_use = next_use
                        victim_index = slot_index

                frame_slots[victim_index] = page

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
        algorithm_name="OPTIMAL",
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