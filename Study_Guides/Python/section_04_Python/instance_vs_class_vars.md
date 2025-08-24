### 🧠 Instance vs. Class Variables: Initialization Patterns

Understanding the difference between **instance** and **class** variables is key to writing clean and effective object-oriented code.

---

### ✅ **Instance Variables**

These are **unique to each object** created from a class. They're usually initialized in the `__init__()` constructor method using `self`.

```python
class Robot:
    def __init__(self, name):
        self.name = name      # Instance variable
        self.status = "idle"  # Each object gets its own status
```

**Use Case:** Storing per-object state (e.g., configuration, device status, position).

---

### ✅ **Class Variables**

These are **shared across all instances** of a class. They're declared **outside of any instance methods**, usually directly under the class definition.

```python
class Robot:
    model_type = "StandardBot"  # Class variable

    def __init__(self, name):
        self.name = name        # Instance variable
```

**Use Case:** Shared settings or constants (e.g., max voltage, firmware version).

---

### 🧪 Key Differences

| Feature       | Instance Variable             | Class Variable                          |
| ------------- | ----------------------------- | --------------------------------------- |
| Scope         | Unique to each object         | Shared across all objects               |
| Defined in    | `__init__()` or other methods | At class level                          |
| Accessed with | `self.variable`               | `ClassName.variable` or `self.variable` |
| Common Usage  | Device name, runtime status   | Hardware model, default config          |

---

### ⚙️ Practical Example

```python
class Sensor:
    total_sensors = 0  # Class variable

    def __init__(self, id):
        self.id = id   # Instance variable
        Sensor.total_sensors += 1
```

- `self.id`: each sensor gets a unique ID.
- `total_sensors`: shared count updated every time a new sensor is created.

---
