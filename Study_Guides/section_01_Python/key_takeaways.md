# Key Takeaways: Python Modules, Packages, and Layouts

## 1. Modules

- A **module** is a single `.py` file containing functions, classes, or variables.
- Functions are defined with the `def` keyword.
- Example: `mathutils.py` with a function:

```python
def add(a, b):
    return a + b
```

## 2. Packages

- A **package** is a directory with an `__init__.py` file and one or more modules.
- Packages can contain **nested packages** (subdirectories with their own `__init__.py`).
- Example structure:

```
mathutils/
    __init__.py
    arithmetic.py
    geometry.py
```

## 3. Nested Packages

- A package inside another package.
- Allows deeper organization, e.g., `models/deep/cnn.py`.
- Import example:

```python
from models.deep import cnn
```

## 4. Directory Trees vs. Packages

- A directory tree shows the overall file/folder structure.
- Only directories with `__init__.py` (or implicit namespace packages) are treated as **packages**.

## 5. How Python Searches for Packages

Python searches in this order:

1. Built-in modules.
2. Current directory.
3. `PYTHONPATH` environment variable.
4. `site-packages` (third-party installs).

Check with:

```python
import sys
print(sys.path)
```

## 6. Best Practices

- Use packages to group related code.
- Keep `__init__.py` minimal but clear.
- Avoid unnecessary nesting.
- Document the layout for collaboration.
- Use descriptive names for clarity.

## 7. Analogy

- **Modules** = individual books.
- **Packages** = bookshelves.
- **Nested packages** = sections within sections.
- **Import search path** = the librarian’s map for finding resources.

