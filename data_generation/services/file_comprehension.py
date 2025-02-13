import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
TARGET_DIR = os.path.join(ROOT_DIR, "constants")


def file_comprehension():
    exercises = []
    txt_files = [file for file in os.listdir(TARGET_DIR) if file.endswith(".txt")]
    for file in txt_files:
        path = os.path.join(TARGET_DIR, file)
        with open(path, "r") as f:
            for line in f:
                exercises.append(line.strip())
    return exercises


if __name__ == "__main__":
    print(file_comprehension())
