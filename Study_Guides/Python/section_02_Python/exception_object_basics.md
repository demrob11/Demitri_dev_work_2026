# Exception Object Basics

When an exception is raised in Python, it creates an **object**. This object carries structured information about the error, making it more than just a message—it’s a fully inspectable and actionable piece of data.

---

## Binding the Exception Object

When catching an exception, use the `as` keyword to assign it to a variable:

```python
try:
    int("abc")
except ValueError as e:
    print(type(e))  # <class 'ValueError'>
    print(str(e))   # invalid literal for int() with base 10: 'abc'
```

Here, `e` is the exception object, and you can inspect its type, contents, and even customize its behavior if it's a user-defined exception.

---

## Why This Matters

- **Structure**: Exceptions are not just strings. They are class instances, often with rich data.
- **Access**: You can use attributes like `.args`, `.message`, or custom fields.
- **Extendability**: You can define your own exception classes with tailored data.

---

## Quick Overview

- `type(e)` shows what kind of error occurred.
- `str(e)` gives a readable message.
- `e.args` holds all arguments passed during exception creation.
- Exceptions behave like normal objects—you can inspect them, log them, and pass them around.

Understanding this object-oriented nature of exceptions lets you handle errors more precisely and build clearer, more informative systems.

