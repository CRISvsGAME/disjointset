# DisjointSet

## Disjoint Set (Union-Find) Data Structure for Python

A generic, type-safe Disjoint Set Union (Union-Find) data structure.

---

## 📦 Installation

Install from PyPI:

```bash
pip install disjointsetunion
```

Import the main class:

```python
from disjointset import DisjointSet
```

---

## 🚀 Quick Start

```python
from disjointset import DisjointSet


class Person:
    def __init__(self, name: str):
        self.name = name


ali = Person("Ali")
bob = Person("Bob")
tom = Person("Tom")

dsu = DisjointSet[int | str | Person]()

# make_set and make_set_many ---------------------------------------------------
dsu.make_set(1)
# (1)

dsu.make_set("Ali")
# (1, "Ali")

dsu.make_set(ali)
# (1, "Ali", ali)

dsu.make_set_many([2, "Bob", bob, 3, "Tom", tom])
# (1, "Ali", ali, 2, "Bob", bob, 3, "Tom", tom)

# union and union_many ---------------------------------------------------------
dsu.union(1, "Ali")
# ({1, "Ali"}, ali, 2, "Bob", bob, 3, "Tom", tom)

dsu.union("Ali", ali)
# ({1, "Ali", ali}, 2, "Bob", bob, 3, "Tom", tom)

dsu.union_many([2, "Bob", bob])
# ({1, "Ali", ali}, {2, "Bob", bob}, 3, "Tom", tom)

dsu.union_many([3, "Tom", tom])
# ({1, "Ali", ali}, {2, "Bob", bob}, {3, "Tom", tom})

# same_set and same_set_many ---------------------------------------------------
print(dsu.same_set(1, ali))
# True

print(dsu.same_set("Ali", 2))
# False

print(dsu.same_set(2, bob))
# True

print(dsu.same_set("Bob", tom))
# False

print(dsu.same_set_many([2, "Bob", bob]))
# True

print(dsu.same_set_many([3, "Tom", tom, 1]))
# False

# get_element_count -------------------------------------------------------------
print(dsu.get_element_count())
# 9 elements (1, "Ali", ali, 2, "Bob", bob, 3, "Tom", tom)

# get_component_count ----------------------------------------------------------
print(dsu.get_component_count())
# 3 components ({1, "Ali", ali}, {2, "Bob", bob}, {3, "Tom", tom})

# get_component_size -----------------------------------------------------------
print(dsu.get_component_size(1))
# 3 (the size of the component containing 1, which is {1, "Ali", ali})

print(dsu.get_component_size("Bob"))
# 3 (the size of the component containing "Bob", which is {2, "Bob", bob})

print(dsu.get_component_size(tom))
# 3 (the size of the component containing tom, which is {3, "Tom", tom})
```

---

## 🔧 Features

### Core Operations

- `make_set(x)`
- `find(x)`
- `union(x, y)`
- `same_set(x, y)`

### Batch Helpers

- `make_set_many(iterable)`
- `find_many(iterable)`
- `union_many(iterable)`
- `same_set_many(iterable)`

### Metadata Helpers

- `get_element_count()`
- `get_component_count()`
- `get_component_size(x)`

### Fully Typed

Supports any hashable type:

```python
# int, float, complex
# bool
# tuple¹, range
# str
# bytes, memoryview²
# frozenset

dsu = DisjointSet[int | float | complex | bool | str]()
```

Notes:

¹ tuple is hashable if all contained elements are hashable.

² memoryview is hashable if the underlying buffer is read-only.

---

## 📂 Project Structure

```bash
src/
    disjointset/
        disjointset.py
stats/
    main.py
tests/
    disjointset/
        test_disjointset.py
```

---

## 🧪 Testing

Run the full test suite:

```bash
pytest
```

---

## 📝 License

MIT License

---

## 🔗 Links

- PyPI: https://pypi.org/project/disjointsetunion/
- Source Code: https://github.com/CRISvsGAME/disjointset
