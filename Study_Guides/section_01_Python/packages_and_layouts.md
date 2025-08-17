# Packages, Layouts, and Nested Packages in Python

Python uses a structured approach for organizing code into **modules**, **packages**, and **nested packages**. Understanding layouts and how Python searches for packages is key to building scalable projects.

---

## Packages vs. Directory Trees

- A **package** is a directory containing an `__init__.py` file. Without it, Python will just see a plain folder, not a package (in Python 3.3+, implicit namespace packages are also possible without `__init__.py`).
- A **directory tree** is simply the folder structure of your project. Only the directories with `__init__.py` (or namespace packages) are treated as packages by Python.

Example:

```
project_root/
│   main.py
│
├── utils/               <- package
│   ├── __init__.py
│   └── helpers.py
│
├── data/                <- plain directory (no __init__.py)
│   └── raw.txt
│
└── models/              <- nested package
    ├── __init__.py
    ├── linear.py
    └── deep/            <- nested subpackage
        ├── __init__.py
        └── cnn.py
```

- `utils` → Package with `helpers.py` module.
- `models` → Package containing a **nested subpackage** `deep`.
- `deep` → Another package inside `models`, showing further hierarchy.
- `data` → Not a package (just a folder).

---

## Why the Name "deep"?

In this example, `deep` is simply the name of a **subpackage**. It could have been called anything (like `advanced`, `extra`, or `layers`). The name `deep` was chosen to illustrate a common convention in machine learning projects, where submodules for **deep learning models** (e.g., CNNs, RNNs) are placed inside a folder called `deep`. It helps signal the purpose of the package.

So `deep` here represents **further specialization** within `models`, but in general, the folder name is up to the developer.

---

## Nested Packages

A **nested package** is simply a package inside another package. It allows deeper organization.

Example usage:

```python
from models.deep import cnn
cnn.run_model()
```

Here, Python traverses the package hierarchy: `models` → `deep` → `cnn`.

---

## How Python Searches for Packages

When you write `import something`, Python searches in the following order:

1. **Built-in modules**: Python’s own compiled modules.
2. **Current directory**: Where the script is being run.
3. **PYTHONPATH environment variable**: Custom paths you can add.
4. **Site-packages directory**: Where third-party libraries are installed.

You can inspect the search path using:

```python
import sys
print(sys.path)
```

This prints a list of directories Python searches when looking for modules and packages.

---

## Best Practices for Layouts

- Keep related code grouped in packages.
- Use **nested packages** for large projects to separate concerns.
- Avoid making every folder a package—only use them where logical.
- Keep `__init__.py` minimal—just expose key functionality.
- Document the package layout so others can navigate easily.

---

## Analogy

Think of a project as a **library building**:

- **Modules** are like individual books (files).
- **Packages** are shelves grouping related books (folders with `__init__.py`).
- **Nested packages** are sections within sections (like “Science → Astronomy → Radio Astronomy”).
- Python’s **import search path** is the librarian’s map of where to look first.

