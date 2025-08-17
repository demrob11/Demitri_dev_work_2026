# Exception Hierarchy Basics and the Importance of Handler Order

Python exceptions are organized into a class-based hierarchy, with `BaseException` at the top. Understanding this hierarchy is essential when designing exception handling logic, especially when using multiple `except` blocks.

---

## Exception Hierarchy Basics

Here's a simplified view of Python's exception hierarchy:

```
BaseException
 |
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      |
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- FileNotFoundError
      +-- TypeError
      +-- ValueError
```

### Key Points:

- All built-in, non-system-exiting exceptions inherit from `Exception`.
- Specific errors (like `KeyError`, `TypeError`) inherit from broader categories.
- You can catch an entire category or a specific subtype depending on your needs.

### Exceptions Are Objects

- Every exception is an instance of a class derived from `BaseException`.
- When an error is raised, Python creates an object of the corresponding exception class.
- This object contains details about the error, such as message, type, and traceback.

For example:

```python
try:
    int('abc')
except ValueError as e:
    print(type(e))      # <class 'ValueError'>
    print(str(e))       # invalid literal for int() with base 10: 'abc'
```

Here, `e` is a `ValueError` object, and we can access its properties and methods like any other object.

---

## Why Handler Order Matters

Python evaluates `except` blocks from top to bottom. It matches the *first* block that handles the raised exception, ignoring the rest.

### Example:

```python
try:
    data = {}['missing']
except Exception:
    print("General Exception caught")
except KeyError:
    print("KeyError caught")
```

This will print:

```
General Exception caught
```

**Why?** Because `KeyError` is a subclass of `Exception`, and the first `except` catches it.

To handle specific exceptions properly, place them *before* more general ones:

```python
try:
    data = {}['missing']
except KeyError:
    print("KeyError caught")
except Exception:
    print("General Exception caught")
```

Now it prints:

```
KeyError caught
```

---

## Best Practices

- **Always order from most specific to most general**.
- **Use **``** as a fallback**, not the default.
- **Avoid catching **`` unless you're handling system exits or interrupts.
- **Remember that exceptions are objects**, so you can store, inspect, and even raise them later.

---

## Summary

- Python exceptions are class-based and hierarchical.
- Each exception is an object derived from `BaseException`.
- The order of `except` blocks determines which one is executed.
- Always catch specific exceptions first to avoid masking errors.

This understanding is crucial when designing predictable and robust error-handling logic.

