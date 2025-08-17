# Python Import Variants

In Python, there are several ways to bring in external modules and their functions. Each method has its own advantages and trade-offs.

---

## 1. Basic Import

```python
import math
```

- Imports the **entire module**.
- You must prefix functions/variables with the module name.

```python
print(math.sqrt(16))  # -> 4.0
```

✅ Clear and explicit, but can be verbose.

---

## 2. From … Import

```python
from math import sqrt
```

- Imports **specific objects** from a module.
- Lets you use them directly, without the module prefix.

```python
print(sqrt(16))  # -> 4.0
```

✅ Useful when you only need a few functions.

---

## 3. Aliasing (as)

```python
import math as m
```

- Gives the module a **shorter or custom name**.

```python
print(m.sqrt(16))  # -> 4.0
```

You can alias specific imports too:

```python
from math import sqrt as square_root
print(square_root(25))  # -> 5.0
```

✅ Great for readability in commonly used libraries (e.g., `import numpy as np`).

---

## 4. Wildcard Import (\*)

```python
from math import *
```

- Imports **everything** from the module into the current namespace.

```python
print(sqrt(16))  # -> 4.0
```

⚠️ **Warning**: Can cause name conflicts if multiple modules have the same function names.

✅ Sometimes convenient in interactive environments (Jupyter, quick scripts).

---

## Best Practices

- Use `import module` when clarity matters.
- Use `from module import thing` for selective imports.
- Use `as` for readability and brevity.
- Avoid `*` except in controlled or experimental contexts.

---

## Quick Analogy

- `import module` → Like referencing a full library in Git or PowerShell.
- `from module import thing` → Like pulling a specific command.
- `as` → Like giving a shortcut alias to a command (`git status` → `gs`).
- `*` → Like blindly importing all commands into your shell—convenient, but risky.

