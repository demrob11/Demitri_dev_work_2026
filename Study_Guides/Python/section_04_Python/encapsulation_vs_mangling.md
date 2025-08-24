### 🔐 Encapsulation vs. Name Mangling in Python

Understanding the difference between **encapsulation** and **name mangling** is key to writing secure and maintainable object-oriented code in Python.

---

### ✅ **Encapsulation** (Concept)

**Encapsulation** is a **design principle** in object-oriented programming that bundles data (attributes) and the methods that operate on them into a single unit — the class. It aims to **restrict direct access** to some of an object's components and **protect the internal state** of the object.

**Key Goals:**

- Prevent external code from breaking the internal state
- Create clear interfaces using methods
- Improve maintainability and modularity

```python
class Device:
    def __init__(self):
        self._status = "idle"  # Suggests internal use

    def start(self):
        self._status = "running"
```

In this example:

- `_status` is "protected" by convention (not enforced).
- The `start()` method provides controlled access.

---

### 🔁 **Name Mangling** (Mechanism)

**Name mangling** is a **Python-specific feature** that automatically changes the name of any attribute with two leading underscores (`__`) to include the class name. This is intended to **avoid name clashes in subclasses** and discourage direct access.

```python
class SecureDevice:
    def __init__(self):
        self.__password = "1234"  # Becomes _SecureDevice__password

    def get_password(self):
        return self.__password

secure = SecureDevice()
print(secure.get_password())         # ✅ Works
print(secure.__password)             # ❌ AttributeError
print(secure._SecureDevice__password)  # ✅ Works, but discouraged
```

---

### 🧩 How They Relate

| Feature       | Encapsulation                           | Name Mangling                               |
| ------------- | --------------------------------------- | ------------------------------------------- |
| Type          | Design Principle                        | Python language mechanism                   |
| Purpose       | Hide internal state & expose interface  | Prevent accidental access & name clashes    |
| Syntax        | Uses `_` or `__` as a naming convention | Uses `__var` → `_ClassName__var` internally |
| Enforced?     | Not enforced, guided by convention      | Partially enforced by Python                |
| Real Privacy? | No (Python doesn't enforce access)      | No, but harder to access accidentally       |

---

### 🛠️ Summary

- **Encapsulation** is about structuring and protecting your code.
- **Name mangling** is Python's way of making certain attributes harder to access directly.
- Both help make your classes **safer**, **cleaner**, and **more maintainable**.

