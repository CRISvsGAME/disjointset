"""Disjoint Set (Union Find) Data Structure."""

from __future__ import annotations
from typing import Generic, Iterable, TypeVar
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

    def find(self, x: T) -> T:
        """
        Return the representative (root) of the set containing x.
        Applies path compression to keep trees shallow.

        Args:
            x: The element to find its set representative for.

        Raises:
            KeyError: If x has not been added via make_set().

        Returns:
            The representative element of the set containing x.
        """
        if x not in self.parent:
            raise KeyError(f"{x!r} is not in the DisjointSet.")

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: T, y: T) -> None:
        """
        Merge the sets containing x and y using union-by-rank.
        If x and y are already in the same set, this is a no-op.

        Args:
            x: An element in the first set.
            y: An element in the second set.

        Raises:
            KeyError: If x or y has not been added via make_set().
        """
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same_set(self, x: T, y: T) -> bool:
        """
        Check if elements x and y are in the same set.

        Args:
            x: An element in the first set.
            y: An element in the second set.

        Raises:
            KeyError: If x or y has not been added via make_set().

        Returns:
            True if x and y are in the same set, False otherwise.
        """
        return self.find(x) == self.find(y)

    # --------------------------------------------------------------------------
    # Convenience Helpers
    # --------------------------------------------------------------------------

    def make_set_many(self, elements: Iterable[T]) -> None:
        """
        Convenience method to make_set() many elements at once.

        Args:
            elements: An iterable of elements to add to the DisjointSet.
        """
        for x in elements:
            self.make_set(x)

    def find_many(self, elements: Iterable[T]) -> tuple[T, ...]:
        """
        Convenience method to find() many representatives at once.

        Args:
            elements: An iterable of elements to find representatives for.

        Raises:
            KeyError: If any element has not been added via make_set().

        Returns:
            A tuple of representatives corresponding to the elements.
        """
        return tuple(self.find(x) for x in elements)

    def union_many(self, elements: Iterable[T]) -> None:
        """
        Convenience method to union() many elements into a single set.

        Args:
            elements: An iterable of elements to union together.

        Raises:
            ValueError: If no elements are provided.
            KeyError: If any element has not been added via make_set().
        """
        iterator = iter(elements)

        try:
            first = next(iterator)
        except StopIteration as e:
            raise ValueError("union_many() requires at least one element.") from e

        for x in iterator:
            self.union(first, x)

    def same_set_many(self, elements: Iterable[T]) -> bool:
        """
        Convenience method to check if all elements are in the same set.

        Args:
            elements: An iterable of elements to check.

        Raises:
            ValueError: If no elements are provided.
            KeyError: If any element has not been added via make_set().

        Returns:
            True if all elements are in the same set, False otherwise.
        """
        iterator = iter(elements)

        try:
            first = next(iterator)
        except StopIteration as e:
            raise ValueError("same_set_many() requires at least one element.") from e

        root = self.find(first)

        for x in iterator:
            if self.find(x) != root:
                return False

        return True
