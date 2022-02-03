from typing import List


def fibonacci(n: int) -> List[int]:
    fibs = [0, 1]
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
