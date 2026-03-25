from src.contracts import SimulationResult


def parse_reference_string(raw: str) -> list[str]:
    parts = [part.strip() for part in raw.replace(",", " ").split() if part.strip()]
    if not parts:
        raise ValueError("Reference string cannot be empty.")

    return parts


def prompt_frames() -> int:
    while True:
        raw = input("Enter number of frames: ").strip()
        try:
            frames = int(raw)
            if frames <= 0:
                print("Frames must be greater than 0.")
                continue
            return frames
        except ValueError:
            print("Invalid input. Enter a whole number.")


def prompt_reference_string() -> list[str]:
    while True:
        raw = input("Enter page reference string (e.g., 7 0 1 2 or A B C D): ").strip()
        try:
            return parse_reference_string(raw)
        except ValueError as error:
            print(f"Invalid input: {error}")


def prompt_algorithm_choice() -> str:
    print("\nChoose an algorithm")
    print("1) First-In, First-Out (FIFO)")
    print("2) Least Recently Used (LRU)")
    print("3) Most Recently Used (MRU)")
    print("4) Optimal Page Replacement (OPTIMAL)")
    print("5) Second Chance (Clock) (SECOND CHANCE)")
    print("0) Exit")
    return input("Choice: ").strip()


def prompt_run_again() -> bool:
    while True:
        answer = input("\nRun another simulation? (y/n): ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please answer y or n.")


def format_frames(frames: list[str | None]) -> str:
    return "[" + " ".join("-" if value is None else str(value) for value in frames) + "]"


def print_result(result: SimulationResult) -> None:
    print("\n" + "=" * 62)
    print(f"Algorithm: {result.algorithm_name}")
    print(f"Number of pages: {result.number_of_pages}")
    print(f"Number of frames: {result.number_of_frames}")
    print("Reference string:", " ".join(map(str, result.reference_string)))
    print("-" * 62)
    print("Step-by-step table")
    print("Idx  Requested  Frames               Status")

    for step in result.steps:
        status = "FAULT" if step.is_fault else "HIT"
        print(f"{step.index:>3}  {step.requested_page:>9}  {format_frames(step.frames_after):<20}  {status}")

    print("-" * 62)
    print(f"Page interrupts: {result.page_interrupts}")
    print(f"Faults:          {result.faults}")
    print(f"Hits:            {result.hits}")
    print(f"Failure Rate:    {result.failure_rate:.2f}%")
    print(f"Success Rate:    {result.success_rate:.2f}%")
    print("=" * 62)


def print_not_implemented(name: str, error: Exception) -> None:
    print("\n" + "-" * 62)
    print(f"{name} is not implemented yet.")
    print(f"Details: {error}")
    print("-" * 62)
