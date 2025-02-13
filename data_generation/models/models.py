import time
from data_generation.services.file_comprehension import file_comprehension
from random import randint, randrange, choice
from dataclasses import dataclass


@dataclass
class DataGenerationPayload:
    number_test_records: int
    payload_key: str

    def __post_init__(self):
        self.errors = []
        if not isinstance(self.number_test_records, int):
            self.errors.append(
                f"number_test_records must be an integer, got {type(self.number_test_records).__name__}"
            )
            raise ValueError(self.errors)
        if self.number_test_records < 1:
            self.errors.append("number_test_records must be greater than or equal to 1")

        if not isinstance(self.payload_key, str):
            self.errors.append(
                f"payload_key must be a string, got {type(self.payload_key).__name__}"
            )

        if self.errors:
            raise ValueError(self.errors)


@dataclass
class GenerationRequest:
    weight: float = None
    exercise: str = None
    sets: int = None
    reps: str = None
    created_at = None

    def __post_init__(self):
        self.exercise = choice(file_comprehension())
        self.sets = randint(3, 5)
        self.weight = randrange(50, 300, 5)
        self.reps = ",".join(str(randint(5, 30)) for _ in range(self.sets))
        self.created_at = randint(
            int(time.mktime(time.strptime("2020-01-01", "%Y-%m-%d"))),
            int(time.mktime(time.strptime("2025-01-01", "%Y-%m-%d"))),
        )

    def to_obj(self) -> dict:
        return {
            "exercise": self.exercise,
            "weight": self.weight,
            "sets": self.sets,
            "reps": self.reps,
            "created_at": self.created_at,
        }
