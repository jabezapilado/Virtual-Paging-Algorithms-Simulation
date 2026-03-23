from typing import Callable

from src.contracts import SimulationResult
from src.fifo import fifo
from src.lru import lru
from src.mru import mru
from src.optimal import optimal
from src.second_chance import second_chance


def get_algorithm_map() -> dict[str, tuple[str, Callable[[int, list[int]], SimulationResult]]]:
    return {
        "1": ("FIFO", fifo),
        "2": ("LRU", lru),
        "3": ("MRU", mru),
        "4": ("OPTIMAL", optimal),
        "5": ("SECOND CHANCE", second_chance),
    }
