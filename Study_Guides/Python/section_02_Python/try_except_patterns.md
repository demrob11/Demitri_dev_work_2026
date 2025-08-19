# Try/Except/Else Patterns, Multiple Except Blocks, and Tuples in Python

Understanding Python's error handling mechanisms is essential for writing resilient, maintainable code. This document covers the `try/except/else` pattern, handling multiple exceptions with `except` blocks, and using tuples for grouped exceptions.

---

## The `try/except/else` Pattern

This structure allows you to catch and handle exceptions that may arise during code execution:

```python
try:
    # Code that might raise an exception
    risky_operation()
except SomeException:
    # Code to run if SomeException occurs
    handle_error()
else:
    # Code to run if no exception occurs
    continue_normal_flow()
```

### Key Points:

- ``** block**: Place code here that may raise an exception.
- ``** block**: Executes if a specified exception occurs.
- ``** block**: Executes only if the `try` block does *not* raise an exception.

The `else` block is useful for code that should only run if everything in `try` succeeded, keeping the `try` focused strictly on error-prone logic.

---

## Multiple `except` Blocks

Python allows you to specify different handlers for different exceptions:

```python
try:
    process_input()
except ValueError:
    print("Invalid value!")
except TypeError:
    print("Wrong type!")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Tips:

- Order matters. More specific exceptions should come before more general ones.
- The final `except Exception` block acts as a fallback catch-all.

---

## Grouping Exceptions with Tuples

You can catch multiple exception types using a tuple:

```python
try:
    handle_task()
except (IOError, OSError):
    print("File or OS error occurred.")
```

This is useful when the handling logic is the same for multiple exception types.

---

## Common Use Case Example

```python
def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
    except (FileNotFoundError, PermissionError) as e:
        print(f"File error: {e}")
    else:
        print("File read successfully:")
        print(content)
```

This pattern ensures errors are managed gracefully and that success cases are handled cleanly.

---

## Summary

- Use `try/except` to catch runtime errors.
- Add `else` for code that should only run when no exception occurs.
- Use multiple `except` blocks for specific error responses.
- Group exceptions with tuples when the response logic is identical.

This pattern improves code readability, robustness, and fault tolerance, which are especially important in larger systems and user-facing tools.

