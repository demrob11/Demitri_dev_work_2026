# Membership Operators in Python

Membership operators are used to test whether a value is **present in** or **absent from** a container like a list, string, tuple, set, or dictionary.

---

## The Operators

| Operator | Meaning                        | Example                |
| -------- | ------------------------------ | ---------------------- |
| `in`     | Returns `True` if value exists | `'a' in 'cat'  # True` |
| `not in` | Returns `True` if value absent | `3 not in [1, 2, 4]`   |

---

## Examples by Type

### Strings

```python
'a' in 'banana'     # True
'z' not in 'apple'  # True
```

### Lists

```python
3 in [1, 2, 3]      # True
"dog" not in ["cat", "bird"]  # True
```

### Tuples

```python
"x" in ("x", "y", "z")  # True
```

### Sets

```python
5 in {1, 3, 5, 7}    # True
```

### Dictionaries (Checks Keys Only)

```python
"name" in {"name": "Ada", "age": 42}   # True
"Ada" in {"name": "Ada"}               # False (not a key)
```

---

## Use Cases

- Check if a value is in a data structure before accessing it
- Filter inputs or restrict access
- Simplify logic with conditional expressions

```python
if "key" in config:
    print(config["key"])
```

---

## Summary

- `in` and `not in` are **membership operators** used to check for presence in sequences and collections.
- Work with all iterable types.
- In dictionaries, they check for **keys**, not values.

These operators are simple, readable, and highly Pythonic—use them often.

