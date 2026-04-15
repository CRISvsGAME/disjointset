"""Tests for Disjoint Set (Union Find) Data Structure."""

import pytest
from disjointset import DisjointSet

# ------------------------------------------------------------------------------
# Core Operations Tests
# ------------------------------------------------------------------------------


def test_make_set():
    """Test make_set() operation."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    dsu.make_set(2)
    assert dsu.find(1) == 1
    assert dsu.find(2) == 2


def test_find():
    """Test find() operation."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3])
    dsu.union(1, 2)
    assert dsu.find(1) == dsu.find(2)
    assert dsu.find(1) != dsu.find(3)


def test_union():
    """Test union() operation."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3])
    dsu.union(1, 2)
    assert dsu.same_set(1, 2)
    assert not dsu.same_set(1, 3)


def test_same_set():
    """Test same_set() operation."""
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
    """Test make_set_many() operation."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3])
    assert dsu.find_many([1, 2, 3]) == (1, 2, 3)


def test_find_many():
    """Test find_many() operation."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3])
    dsu.union_many([1, 2])
    roots = dsu.find_many([1, 2, 3])
    assert len(roots) == 3
    assert roots[0] == roots[1]
    assert roots[0] != roots[2]


def test_union_many():
    """Test union_many() operation."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3, 4])
    dsu.union_many([1, 2, 3])
    assert dsu.same_set_many([1, 2, 3])
    assert not dsu.same_set_many([1, 2, 3, 4])


def test_same_set_many():
    """Test same_set_many() operation."""
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
    """Test that find() raises KeyError for missing element."""
    dsu = DisjointSet[int]()
    with pytest.raises(KeyError):
        dsu.find(1)


def test_union_missing_raises():
    """Test that union() raises KeyError for missing element."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    with pytest.raises(KeyError):
        dsu.union(1, 2)


def test_same_set_missing_raises():
    """Test that same_set() raises KeyError for missing element."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    with pytest.raises(KeyError):
        dsu.same_set(1, 2)


def test_find_many_missing_raises():
    """Test that find_many() raises KeyError for missing element."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    with pytest.raises(KeyError):
        dsu.find_many([1, 2])


def test_union_many_empty_raises():
    """Test that union_many() raises ValueError for empty input."""
    dsu = DisjointSet[int]()
    with pytest.raises(ValueError):
        dsu.union_many([])


def test_union_many_missing_raises():
    """Test that union_many() raises KeyError for missing element."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    with pytest.raises(KeyError):
        dsu.union_many([1, 2])


def test_same_set_many_empty_raises():
    """Test that same_set_many() raises ValueError for empty input."""
    dsu = DisjointSet[int]()
    with pytest.raises(ValueError):
        dsu.same_set_many([])


def test_same_set_many_missing_raises():
    """Test that same_set_many() raises KeyError for missing element."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    with pytest.raises(KeyError):
        dsu.same_set_many([1, 2])


# --------------------------------------------------------------------------
# Metadata Helpers Tests
# --------------------------------------------------------------------------


def test_len_and_get_element_count():
    """Test __len__ and get_element_count() reflect the number of elements."""
    dsu = DisjointSet[int]()
    assert len(dsu) == 0
    assert dsu.get_element_count() == 0
    dsu.make_set_many([1, 2, 3])
    assert len(dsu) == 3
    assert dsu.get_element_count() == 3
    dsu.make_set(3)
    assert len(dsu) == 3
    assert dsu.get_element_count() == 3


def test_component_count_tracks_components():
    """Test get_component_count() reflects the number of disjoint sets."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3, 4])
    assert dsu.get_component_count() == 4
    dsu.union(1, 2)
    assert dsu.get_component_count() == 3
    dsu.union(2, 3)
    assert dsu.get_component_count() == 2
    dsu.union(1, 3)
    assert dsu.get_component_count() == 2
    dsu.union(1, 4)
    assert dsu.get_component_count() == 1


def test_component_count_idempotent_make_set():
    """Test make_set() idempotency does not affect component count."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    assert dsu.get_component_count() == 1
    dsu.make_set(1)
    assert dsu.get_component_count() == 1


def test_get_component_size_singletons():
    """Test get_component_size() returns 1 for singleton sets."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3])
    assert dsu.get_component_size(1) == 1
    assert dsu.get_component_size(2) == 1
    assert dsu.get_component_size(3) == 1


def test_get_component_size_after_unions():
    """Test get_component_size() reflects merged sets."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3, 4, 5])
    dsu.union(1, 2)
    assert dsu.get_component_size(1) == 2
    assert dsu.get_component_size(2) == 2
    dsu.union(3, 4)
    assert dsu.get_component_size(3) == 2
    assert dsu.get_component_size(4) == 2
    dsu.union(1, 3)
    for x in (1, 2, 3, 4):
        assert dsu.get_component_size(x) == 4
    assert dsu.get_component_size(5) == 1


def test_get_component_size_missing_raises():
    """Test get_component_size() raises KeyError for missing elements."""
    dsu = DisjointSet[int]()
    with pytest.raises(KeyError):
        dsu.get_component_size(1)


# ------------------------------------------------------------------------------
# Hashing and Identity Semantics Tests
# ------------------------------------------------------------------------------


# pylint: disable=too-few-public-methods
class Person:
    """Simple hashable object using default identity equality."""

    def __init__(self, name: str):
        self.name = name


def test_default_object_identity_semantics_preserve_distinct_instances():
    """Test that default object identity semantics preserve distinct instances."""
    dsu = DisjointSet[Person]()
    alice1 = Person("Alice")
    alice2 = Person("Alice")
    dsu.make_set(alice1)
    dsu.make_set(alice2)
    assert dsu.get_element_count() == 2
    assert dsu.get_component_count() == 2
    assert not dsu.same_set(alice1, alice2)


def test_duplicate_hashable_values_are_idempotent():
    """Test that duplicate hashable values are treated as the same element."""
    dsu = DisjointSet[str]()
    alice1 = "Alice"
    alice2 = "Alice"
    dsu.make_set(alice1)
    dsu.make_set(alice2)
    assert dsu.get_element_count() == 1
    assert dsu.get_component_count() == 1
    assert dsu.same_set(alice1, alice2)


# ------------------------------------------------------------------------------
# Structural Invariant Tests
# ------------------------------------------------------------------------------


def test_chain_unions_create_single_component():
    """Test connectivity, component count, and component size across a chain."""
    dsu = DisjointSet[int]()
    n = 1000
    dsu.make_set_many(range(n))
    for i in range(n - 1):
        dsu.union(i, i + 1)
    for i in range(n):
        assert dsu.same_set(0, i)
    assert dsu.get_element_count() == n
    assert dsu.get_component_count() == 1
    assert dsu.get_component_size(0) == n


def test_find_is_idempotent_after_path_compression():
    """Test repeated find() calls preserve the same representative."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3, 4, 5])
    dsu.union(1, 2)
    dsu.union(2, 3)
    dsu.union(3, 4)
    dsu.union(4, 5)
    root = dsu.find(1)
    for x in (1, 2, 3, 4, 5):
        assert dsu.find(x) == root
        assert dsu.same_set(x, 1)


def test_union_element_with_itself_is_noop():
    """Test union(x, x) does not change component metadata."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3])
    dsu.union(1, 1)
    dsu.union(2, 2)
    dsu.union(3, 3)
    assert dsu.get_element_count() == 3
    assert dsu.get_component_count() == 3
    assert dsu.get_component_size(1) == 1
    assert dsu.get_component_size(2) == 1
    assert dsu.get_component_size(3) == 1


def test_duplicate_union_is_noop():
    """Test repeated union() of the same component does not change metadata."""
    dsu = DisjointSet[int]()
    dsu.make_set_many([1, 2, 3])
    dsu.union(1, 2)
    dsu.union(2, 1)
    dsu.union(1, 2)
    assert dsu.get_element_count() == 3
    assert dsu.get_component_count() == 2
    assert dsu.get_component_size(1) == 2
    assert dsu.get_component_size(2) == 2
    assert dsu.get_component_size(3) == 1


def test_same_set_many_single_element_is_true():
    """Test same_set_many() returns True for a single existing element."""
    dsu = DisjointSet[int]()
    dsu.make_set(1)
    assert dsu.same_set_many([1])
