from dataclasses import dataclass
from typing import List


@dataclass
class SimulationStep:
    index: int
    requested_page: int
    frames_after: List[int | None]
    is_fault: bool


@dataclass
class SimulationResult:
    algorithm_name: str
    number_of_pages: int
    number_of_frames: int
    reference_string: List[int]
    steps: List[SimulationStep]
    page_interrupts: int
    faults: int
    hits: int
    failure_rate: float
    success_rate: float
