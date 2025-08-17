# Sorting and Return Values in Python

Sorting is one of the most frequent and essential operations in programming. Python offers intuitive and flexible ways to sort collections using built-in tools like `sorted()` and `.sort()`.

---

## `sorted()` – Non-Destructive Sorting

```python
numbers = [3, 1, 4, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 3, 4]
```

- Returns a **new sorted list**
- Original list is unchanged

```python
sorted(numbers, reverse=True)  # [4, 3, 2, 1]
```

### With Custom Key

```python
words = ["apple", "banana", "cherry"]
sorted(words, key=len)  # ['apple', 'banana', 'cherry']
```

- `key` determines the value used for comparison

---

## `.sort()` – In-Place Sorting (Lists Only)

```python
words = ["apple", "banana", "cherry"]
words.sort()
print(words)  # ['apple', 'banana', 'cherry']
```

- Modifies the list directly
- Returns `None`

### With Reverse or Key

```python
words.sort(reverse=True)
words.sort(key=str.upper)
```

---

## Important Distinctions

| Function   | Mutates List | Returns Sorted List | Returns `None` |
| ---------- | ------------ | ------------------- | -------------- |
| `sorted()` | No           | Yes                 | No             |
| `.sort()`  | Yes          | No                  | Yes            |

- Always use `sorted()` when you need to preserve the original list.
- Use `.sort()` for memory efficiency when working with large lists that don’t need to be preserved.

---

## Summary

- Use `sorted()` when you want a **copy** of the sorted list.
- Use `.sort()` when you want to sort **in-place**.
- Both accept `reverse=` and `key=` arguments for custom sorting.

Remember: `.sort()` modifies, `sorted()` returns.

