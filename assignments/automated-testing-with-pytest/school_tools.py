def is_even(number: int) -> bool:
    return number % 2 == 0


def calculate_average(scores: list[float]) -> float:
    if not scores:
        raise ValueError("scores cannot be empty")
    return sum(scores) / len(scores)


class MileageTracker:
    def __init__(self) -> None:
        self.mileage = 0

    def update_mileage(self, new_mileage: int) -> None:
        if new_mileage < self.mileage:
            raise ValueError("mileage cannot decrease")
        self.mileage = new_mileage