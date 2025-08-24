# Python Lambdas Explained

Python lambda functions are **anonymous functions** — meaning they don't require a name. They're typically used when you need a small, short-lived function.

## Regular Function vs Lambda

```python
# Regular function definition:
def add(x, y):
    return x + y

# Lambda equivalent:
add_lambda = lambda x, y: x + y
```

Both functions do the same thing.

## Why Use Lambdas Over Regular Functions?

### 1. **Conciseness**
Lambdas reduce boilerplate when performing simple operations.

```python
square = lambda x: x * x  # More compact than defining a full function
```

### 2. **Use-Once / Throwaway Functions**
They shine in one-liner use cases, especially with functions like `map()`, `filter()`, or `sorted()`.

```python
nums = [1, 2, 3, 4]

# Using lambda with map:
squared = list(map(lambda x: x ** 2, nums))
```

### 3. **Inline Functionality**
Lambdas help keep code concise and readable when the logic is minimal.

```python
# Sort list of tuples by the second item:
pairs = [("a", 3), ("b", 1), ("c", 2)]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
```

## When *Not* to Use Lambdas

- The logic is complex or spans multiple lines
- The function is reused in multiple places
- You need to debug or log inside the function (harder with anonymous functions)

In such cases, regular `def` functions are more appropriate.

---

> Lambdas are perfect for functional-style quick operations. But for anything more complex or reusable, stick to named functions for clarity and maintainability.
