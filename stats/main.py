"""DisjointSet Profiler"""

import cProfile
import pstats
from disjointset import DisjointSet


# pylint: disable=too-few-public-methods
class Person:
    """Person"""

    def __init__(self, name: str):
        self.name = name


def main(n: int = 1000000):
    """DisjointSet Profiler"""
    dsu = DisjointSet[Person]()
    people = [Person(f"Person {i}") for i in range(n)]

    for person in people:
        dsu.make_set(person)

    for i in range(0, n, 2):
        dsu.union(people[i], people[i + 1])

    for i in range(0, n, 4):
        dsu.union(people[i], people[i + 2])

    for i in range(0, n, 4):
        assert dsu.same_set(people[i + 1], people[i + 3])


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    main()

    profiler.disable()
    pstats.Stats(profiler).sort_stats("cumtime").print_stats()
