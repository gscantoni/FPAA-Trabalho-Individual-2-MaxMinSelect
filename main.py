from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence

@dataclass
class MaxMinResult:
    minimum: int
    maximum: int
    comparisons: int

def maxmin_select(seq: Sequence[int]) -> MaxMinResult:
    n = len(seq)
    if n == 0:
        raise ValueError("Empty sequence.")
    if n == 1:
        return MaxMinResult(seq[0], seq[0], 0)
    if n == 2:
        if seq[0] <= seq[1]:
            return MaxMinResult(seq[0], seq[1], 1)
        else:
            return MaxMinResult(seq[1], seq[0], 1)

    mid = n // 2
    left = maxmin_select(seq[:mid])
    right = maxmin_select(seq[mid:])

    comparisons = left.comparisons + right.comparisons

    if left.minimum <= right.minimum:
        global_min = left.minimum
        comparisons += 1
    else:
        global_min = right.minimum
        comparisons += 1

    if left.maximum >= right.maximum:
        global_max = left.maximum
        comparisons += 1
    else:
        global_max = right.maximum
        comparisons += 1

    return MaxMinResult(global_min, global_max, comparisons)

if __name__ == "__main__":
    import sys
    data = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [7, -3, 9, 2, 11, 5, -10, 4]
    print("Input:", data)
    result = maxmin_select(data)
    print("Minimum:", result.minimum)
    print("Maximum:", result.maximum)
    print("Comparisons:", result.comparisons)
