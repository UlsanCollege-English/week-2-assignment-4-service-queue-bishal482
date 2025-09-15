"""Service Queue — Starter

Simulate a simple customer queue with pure functions.
Implement without mutating inputs.
"""
from typing import List, Tuple


def take_next(queue: List[str]) -> Tuple[str | None, List[str]]:
    """Return (next_name, remaining_queue).

    If queue is empty, return (None, []).
    """
    if not queue:
        return None, []
    return queue[0], queue[1:]


def move_to_back(queue: List[str], name: str) -> List[str]:
    """Return a new queue where the first occurrence of `name` is moved to the back.

    If `name` is not present, return the queue unchanged (new list).
    """
    new_queue = queue.copy()
    try:
        new_queue.append(new_queue.pop(new_queue.index(name)))
    except ValueError:
        pass  # name not in queue, leave as is
    return new_queue


def interleave(q1: List[str], q2: List[str]) -> List[str]:
    """Return an interleaved queue: q1[0], q2[0], q1[1], q2[1], ...

    After the shorter queue runs out, append the rest.
    """
    result = []
    len1, len2 = len(q1), len(q2)
    for i in range(max(len1, len2)):
        if i < len1:
            result.append(q1[i])
        if i < len2:
            result.append(q2[i])
    return result
