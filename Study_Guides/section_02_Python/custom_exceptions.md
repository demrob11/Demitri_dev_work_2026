# Defining and Using Custom Exceptions in Python

Sometimes built-in exceptions like `ValueError` or `TypeError` don't clearly communicate what's gone wrong in your specific context. In those cases, defining your own custom exceptions can make your code more readable, testable, and maintainable.

---

## How to Define a Custom Exception

Create a new class that inherits from `Exception`:

```python
class DataFormatError(Exception):
    pass
```

You can also add custom logic or attributes:

```python
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")
```

This pattern creates a reusable object that holds both what went wrong and where. Think of it as a more descriptive and structured error message wrapped in a class.

---

## How to Use a Custom Exception

Raise your exception with `raise`, just like with built-in exceptions:

```python
def process_data(data):
    if not isinstance(data, dict):
        raise DataFormatError("Expected a dictionary.")
```

Catch and handle it as needed:

```python
try:
    process_data("not a dict")
except DataFormatError as e:
    print(f"Custom error caught: {e}")
```

---

## Clarifying the Confusion

It’s common to feel unsure about **why** or **when** to use custom exceptions, especially when starting out. Here’s how to think about it:

- Built-in exceptions are generic. If you raise `ValueError`, you (and others) may not know what value or context caused it.
- Custom exceptions let you name and organize your errors clearly. It’s like creating **vocabulary specific to your application**.
- They make debugging and logging easier. When reading logs, `DataFormatError` is much clearer than `ValueError`.
- They work just like regular objects. You can store details (e.g., field names, error codes) and still use `try/except` as usual.

### Analogy

If you're building a storytelling engine and something goes wrong with the input file structure, which makes more sense to raise?

```python
raise ValueError("Missing 'scenes' field")
# vs
raise StoryStructureError("Missing 'scenes' field")
```

The second version tells you **what kind of problem** happened and **what part of your system it relates to**.

---

## When to Use Custom Exceptions

Use them when:

- Built-in exceptions don’t convey enough meaning
- You want fine-grained control over specific error types
- You're building a module or API where clarity and maintainability matter

---

## Summary

- Custom exceptions are subclasses of `Exception`
- They can carry additional context with attributes
- Use them to make error messages and control flow more meaningful

By defining your own exceptions, you're embracing object-oriented principles and designing clearer, more intentional systems. It may feel abstract at first, but with use, it becomes a powerful tool in your development toolkit.

