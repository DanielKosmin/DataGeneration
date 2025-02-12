import time
from data_generation.constants.constant import COMPOUND_UPPER_EXERCISES, ISOLATION_UPPER_EXERCISES, \
    COMPOUND_LOWER_EXERCISES, ISOLATION_LOWER_EXERCISES
from random import randint, randrange, choice
from dataclasses import dataclass


@dataclass
class GenerationRequest:
    weight: float = None
    exercise: str = None
    sets: int = None
    reps: str = None
    created_at = None

    def __post_init__(self):
        self.exercise = choice(
            COMPOUND_UPPER_EXERCISES + COMPOUND_LOWER_EXERCISES + ISOLATION_LOWER_EXERCISES + ISOLATION_UPPER_EXERCISES)
        self.sets = randint(3, 5)
        if self.exercise in (COMPOUND_UPPER_EXERCISES + COMPOUND_LOWER_EXERCISES + ISOLATION_LOWER_EXERCISES):
            self.weight = randrange(50, 300, 5)
        if self.exercise in ISOLATION_UPPER_EXERCISES:
            self.weight = randrange(5, 40, 5)
        self.reps = ','.join(str(randint(5, 30)) for _ in range(self.sets))
        self.created_at = randint(int(time.mktime(time.strptime("2020-01-01", "%Y-%m-%d"))),
                                  int(time.mktime(time.strptime("2025-01-01", "%Y-%m-%d"))))

    def to_obj(self) -> dict:
        return {
            "exercise": self.exercise,
            "weight": self.weight,
            "sets": self.sets,
            "reps": self.reps,
            "created_at": self.created_at
        }
