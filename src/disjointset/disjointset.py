"""Disjoint Set (Union Find) Data Structure."""

from __future__ import annotations
from typing import Generic, TypeVar
from collections.abc import Hashable

T = TypeVar("T", bound=Hashable)


class DisjointSet(Generic[T]):
    """
    A generic, type-safe Disjoint Set Union (Union-Find) data structure.

    Supports:
        Core Operations:
            - make_set(x)
            - find(x)
            - union(x, y)
            - same_set(x, y)
        Convenience Helpers:
            - make_set_many([x, y, z])
            - find_many([x, y, z])
            - union_many([x, y, z])
            - same_set_many([x, y, z])
    """

    def __init__(self) -> None:
        self.parent: dict[T, T] = {}
        self.rank: dict[T, int] = {}

    # --------------------------------------------------------------------------
    # Core Operations
    # --------------------------------------------------------------------------

    def make_set(self, x: T) -> None:
        """
        Create a new set containing the single element x.
        If x is already present, this is a no-op.

        Args:
            x: The element to add to the DisjointSet.
        """
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
