# ruff: file-ignore[suspicious-non-cryptographic-random-usage]

import random

import brain_games.engine as run


def gen_progression():
    start = random.randrange(1, 20)
    step = random.randrange(1, 20)
    nums = []
    for index in range(10):
        currentElement = start + index * step
        nums.append(currentElement)
    indexHideElement = random.randrange(0, 9)
    hideElement = nums[indexHideElement]
    nums = [str(num) for num in nums]
    nums[indexHideElement] = ".."
    num_series = " ".join(nums)
    return num_series, hideElement


def run_game():
    rules = "What number is missing in the progression?"
    run.play(rules, gen_progression)