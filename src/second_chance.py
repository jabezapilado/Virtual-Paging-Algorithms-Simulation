from src.contracts import SimulationResult, SimulationStep
from src.metrics import compute_metrics


def second_chance(frames: int, reference_string: list[int]) -> SimulationResult:
    if frames <= 0:
        raise ValueError("Number of frames must be greater than 0.")

    frame_slots: list[int | None] = [None] * frames
    reference_bits: list[int] = [0] * frames
    clock_hand = 0
    faults = 0
    steps: list[SimulationStep] = []

    for index, page in enumerate(reference_string, start=1):
        page_in_memory = page in frame_slots

        if page_in_memory:
            is_fault = False
            hit_index = frame_slots.index(page)
            reference_bits[hit_index] = 1
        else:
            is_fault = True
            faults += 1

            if None in frame_slots:
                empty_index = frame_slots.index(None)
                frame_slots[empty_index] = page
                reference_bits[empty_index] = 1
            else:
                while True:
                    if reference_bits[clock_hand] == 0:
                        frame_slots[clock_hand] = page
                        reference_bits[clock_hand] = 1
                        clock_hand = (clock_hand + 1) % frames
                        break

                    reference_bits[clock_hand] = 0
                    clock_hand = (clock_hand + 1) % frames

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
        algorithm_name="SECOND CHANCE",
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