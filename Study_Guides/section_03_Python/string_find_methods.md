# Methods: `find()`, `rfind()`, and the `str` Family

When working with text in Python, string methods help you locate and manipulate substrings effectively. Among them, `find()` and `rfind()` are essential tools for locating text.

---

## `find()` – First Occurrence Finder

```python
text = "banana"
text.find("a")  # 1
```

- Returns the **index of the first occurrence** of the substring.
- If not found, returns `-1`.
- Optional arguments: `text.find(sub, start, end)`

```python
text.find("a", 2)  # 3
```

---

## `rfind()` – Reverse Finder

```python
text = "banana"
text.rfind("a")  # 5
```

- Returns the **index of the last occurrence** of the substring.
- Also returns `-1` if not found.
- Optional arguments: `text.rfind(sub, start, end)`

```python
text.rfind("a", 0, 4)  # 3
```

---

## Related Methods in the `str` Family

These methods do not raise errors if the substring isn’t found (unlike `index()`):

- `find()` → first match
- `rfind()` → last match
- `index()` → like `find()`, but raises `ValueError` if not found
- `startswith()` / `endswith()` → check positions
- `in` keyword → general membership check

```python
"ana" in "banana"        # True
"banana".startswith("ba")  # True
"banana".endswith("na")    # True
```

---

## Use Case Comparison

| Method         | Purpose                           | Raises Error? |
| -------------- | --------------------------------- | ------------- |
| `find()`       | Index of first match              | No            |
| `rfind()`      | Index of last match               | No            |
| `index()`      | Like `find()`, but strict         | Yes           |
| `in`           | Boolean presence check            | No            |
| `startswith()` | True if string starts with prefix | No            |

---

## Summary

- Use `find()` and `rfind()` to locate text safely by index.
- Use `in`, `startswith()`, and `endswith()` for boolean checks.
- All are part of the `str` method family—Python’s core string manipulation toolkit.

These methods help you navigate and manipulate text clearly, without falling into common error traps.

