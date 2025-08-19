# Raising Errors and Assertions in Python

In addition to handling exceptions, Python also allows you to deliberately raise errors or check assumptions using `raise` and `assert`. These tools help enforce constraints, catch logical issues early, and improve debugging. **Used correctly, they provide powerful mechanisms for structuring code that is clear, defensive, and robust.**

---

## Raising Exceptions

You can explicitly raise an exception using the `raise` keyword, typically to signal an error condition:

```python
raise ValueError("Input must be a positive integer")
```

### Syntax:

```python
raise ExceptionType("Optional error message")
```

- `ExceptionType` must be a subclass of `BaseException`.
- The optional message is stored in the exception object.

### Example:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age set to {age}")
```

You can also re-raise the current exception (commonly used inside `except` blocks):

```python
except SomeError:
    log_error()
    raise  # Re-raises the same exception
```

Using `raise` strategically lets you define *clear boundaries and responsibilities* within your code—functions can validate inputs and enforce rules, rather than failing silently or returning vague error codes.

---

## Assertions

Assertions are used for internal checks that should always be true in normal operation. They’re mainly for debugging and development, not user-facing error handling.

### Syntax:

```python
assert condition, "Optional message if condition is false"
```

If the condition is `False`, Python raises an `AssertionError`:

```python
x = -5
assert x >= 0, "x must be non-negative"
```

This helps catch logic bugs or unexpected state early in development.

### Important Notes:

- Assertions can be disabled with the `-O` (optimize) flag when running Python.
- Don’t use assertions for validating user input or handling production logic.

When used thoughtfully, assertions **document internal expectations** and act as early-warning systems for broken logic or side effects.

---

## When to Use What

- Use `raise` when you want to **signal an error intentionally** (e.g., invalid data, failed checks).
- Use `assert` to **catch programming errors early** (e.g., invariants, test conditions).

Both contribute significantly to clean, maintainable, and testable codebases.

---

## Summary

- `raise` lets you generate exceptions manually.
- `assert` helps identify bugs during development by verifying assumptions.
- Prefer `raise` for runtime checks and input validation.
- Use `assert` for sanity checks that should never fail unless there's a bug.
- Both features reinforce strong code structure by making errors **explicit, traceable, and testable**.

Mastering `raise` and `assert` is not just about catching problems—it's about writing better software from the ground up.

