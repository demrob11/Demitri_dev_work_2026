# Python Sequence Mechanics: Indexing, Splicing, Immutability, Iteration, Concatenation, Repetition

This is a practical breakdown of key operations used in working with Python sequences like `str`, `list`, and `tuple`. Less drama, more function.

---

## Indexing (Access by Position)

```python
word = "python"
word[0]   # 'p'
word[-1]  # 'n'
```

- Access a single element by index.
- Index starts at 0; negative indices count from the end.

---

## Splicing / Slicing (Extract Sub-Sequences)

```python
text = "abcdefg"
text[2:5]    # 'cde'
text[:4]     # 'abcd'
text[::2]    # 'aceg'
```

- Format: `sequence[start:stop:step]`
- Non-destructive: returns a new sequence

---

## Immutability (What Can Be Changed)

```python
word = "immutable"
# word[0] = 'I'  → ❌ TypeError

name = ["Ada", "Alan"]
name[0] = "Grace"  # ✅ Lists are mutable
```

- Strings and tuples: **immutable**
- Lists and sets: **mutable**

---

## Iteration (Loop Through)

```python
for char in "loop":
    print(char)
```

- Works on any iterable (list, str, tuple, etc.)
- Enables element-by-element processing

---

## Concatenation (Combine Sequences)

```python
"Hello " + "World"   # 'Hello World'
[1, 2] + [3, 4]       # [1, 2, 3, 4]
```

- Uses `+` to join sequences of the same type

---

## Repetition (Multiply Sequences)

```python
"ha" * 3       # 'hahaha'
[1, 2] * 2     # [1, 2, 1, 2]
```

- Uses `*` to repeat the sequence
- Commonly used for pattern building or padding

---

## Converting a String to a Method or Object

Sometimes, you have the name of a method or object as a **string**, and you want to access the real function or attribute it refers to.

### Built-in Access Example:

```python
import builtins
method_name = "len"
func = getattr(builtins, method_name)
print(func([1, 2, 3]))  # Outputs: 3
```

### Object Attribute Access Example:

```python
class Tool:
    def greet(self):
        return "Hello from Tool!"

tool = Tool()
method_name = "greet"
result = getattr(tool, method_name)()
print(result)  # Outputs: Hello from Tool!
```

- `getattr(obj, "attr_name")` retrieves a reference to the attribute or method.
- If it's a method, you can call it using `()` after retrieval.
- This is commonly used in frameworks, plugins, and dynamic dispatch systems.

---

## Summary Table

| Operation     | Syntax Example           | Result                         |
| ------------- | ------------------------ | ------------------------------ |
| Indexing      | `x[1]`                   | Single element                 |
| Slicing       | `x[1:3]`                 | Sub-sequence                   |
| Iteration     | `for i in x`             | Loop through values            |
| Concatenation | `x + y`                  | Combined sequences             |
| Repetition    | `x * 2`                  | Repeated values                |
| Immutability  | `x[0] = val`             | ❌ if `x` is immutable          |
| getattr()     | `getattr(obj, 'name')()` | Calls method or gets attribute |

These mechanics form the foundation of Pythonic sequence manipulation. Learn them well—they're everywhere.

