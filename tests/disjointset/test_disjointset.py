"""Tests for Disjoint Set (Union Find) Data Structure."""

from disjointset import DisjointSet

# ------------------------------------------------------------------------------
# Core Operations Tests
# ------------------------------------------------------------------------------


def test_make_set():
    """Test make_set operation."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    dsu.make_set(2)
    assert dsu.find(1) == 1
    assert dsu.find(2) == 2
    assert dsu.parent[1] == 1
    assert dsu.parent[2] == 2


def test_find():
    """Test find operation."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3])
    dsu.union(1, 2)
    assert dsu.find(1) == dsu.find(2)
    assert dsu.find(1) != dsu.find(3)


def test_union():
    """Test union operation."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3])
    dsu.union(1, 2)
    assert dsu.same_set(1, 2)
    assert not dsu.same_set(1, 3)


def test_same_set():
    """Test same_set operation."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3, 4])
    dsu.union(1, 2)
    dsu.union(2, 3)
    assert dsu.same_set(1, 3)
    assert not dsu.same_set(1, 4)
