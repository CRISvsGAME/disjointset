"""Tests for Disjoint Set (Union Find) Data Structure."""

import pytest
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


# ------------------------------------------------------------------------------
# Convenience Helpers Tests
# ------------------------------------------------------------------------------


def test_make_set_many():
    """Test make_set_many operation."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3])
    assert dsu.find_many([1, 2, 3]) == (1, 2, 3)


def test_find_many():
    """Test find_many operation."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3])
    dsu.union_many([1, 2])
    roots = dsu.find_many([1, 2, 3])
    assert len(roots) == 3
    assert roots[0] == roots[1]
    assert roots[0] != roots[2]


def test_union_many():
    """Test union_many operation."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3, 4])
    dsu.union_many([1, 2, 3])
    assert dsu.same_set_many([1, 2, 3])
    assert not dsu.same_set_many([1, 2, 3, 4])


def test_same_set_many():
    """Test same_set_many operation."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3, 4, 5])
    dsu.union_many([1, 2, 3])
    dsu.union_many([4, 5])
    assert dsu.same_set_many([1, 2, 3])
    assert dsu.same_set_many([4, 5])
    assert not dsu.same_set_many([1, 2, 3, 4, 5])


# ------------------------------------------------------------------------------
# Error Handling Tests
# ------------------------------------------------------------------------------


def test_find_missing_raises():
    """Test that find raises KeyError for missing element."""
    dsu = DisjointSet[int]()
    with pytest.raises(KeyError):
        dsu.find(1)


def test_union_missing_raises():
    """Test that union raises KeyError for missing element."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    with pytest.raises(KeyError):
        dsu.union(1, 2)


def test_same_set_missing_raises():
    """Test that same_set raises KeyError for missing element."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    with pytest.raises(KeyError):
        dsu.same_set(1, 2)


def teste_find_many_missing_raises():
    """Test that find_many raises KeyError for missing element."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    with pytest.raises(KeyError):
        dsu.find_many([1, 2])


def test_union_many_empty_raises():
    """Test that union_many raises ValueError for empty input."""
    dsu = DisjointSet[int]()
    with pytest.raises(ValueError):
        dsu.union_many([])


def test_union_many_missing_raises():
    """Test that union_many raises KeyError for missing element."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    with pytest.raises(KeyError):
        dsu.union_many([1, 2])


def test_same_set_many_empty_raises():
    """Test that same_set_many raises ValueError for empty input."""
    dsu = DisjointSet[int]()
    with pytest.raises(ValueError):
        dsu.same_set_many([])


def test_same_set_many_missing_raises():
    """Test that same_set_many raises KeyError for missing element."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    with pytest.raises(KeyError):
        dsu.same_set_many([1, 2])
