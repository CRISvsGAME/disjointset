# DisjointSet

## Disjoint Set (Union Find) Data Structure for Python

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

# make_set and make_set_many
dsu.make_set(1)
dsu.make_set("Ali")
dsu.make_set(ali)
dsu.make_set_many([2, 3, "Bob", "Tom", bob, tom])

# union and union_many
dsu.union(1, 2)
dsu.union("Ali", ali)
dsu.union(1, ali)
dsu.union_many(["Bob", bob])
dsu.union_many([3, "Tom", tom])

# True
print(dsu.same_set(1, ali))
print(dsu.same_set(2, "Ali"))
print(dsu.same_set("Bob", bob))
print(dsu.same_set_many([3, "Tom", tom]))
print(dsu.same_set_many([1, 2, "Ali", ali]))
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

### Fully Typed

Supports any hashable type:

```python
dsu = DisjointSet[str]()
```

---

## 📂 Project Structure

```bash
src/
    disjointset/
        disjointset.py
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
