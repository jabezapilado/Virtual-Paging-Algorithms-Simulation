from src.algorithms import get_algorithm_map
from src.cli import (
    prompt_algorithm_choice,
    prompt_frames,
    prompt_reference_string,
    prompt_run_again,
    print_not_implemented,
    print_result,
)


def run_app() -> None:
    print("OPSYSFUN Final Project - Virtual Paging Algorithms Simulation")

    while True:
        choice = prompt_algorithm_choice()
        if choice == "0":
            print("Exiting simulation. Goodbye.")
            return

        algorithm_map = get_algorithm_map()
        selected = algorithm_map.get(choice)
        if selected is None:
            print("Invalid choice. Please choose from the menu.")
            continue

        algorithm_name, algorithm_fn = selected
        frames = prompt_frames()
        reference_string = prompt_reference_string()

        try:
            result = algorithm_fn(frames, reference_string)
            print_result(result)
        except NotImplementedError as error:
            print_not_implemented(algorithm_name, error)

        if not prompt_run_again():
            print("Exiting simulation. Goodbye.")
            return
