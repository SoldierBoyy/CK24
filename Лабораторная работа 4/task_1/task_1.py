import json

INPUT_FILENAME = "input.json"


def task() -> float:
    result = 0

    with open(INPUT_FILENAME, "r") as f:
        for dictionary in json.load(f):
            result += dictionary["score"] * dictionary["weight"]

    return round(result, 3)


print(task())
