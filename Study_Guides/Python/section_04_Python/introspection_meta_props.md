### 🧬 Python Meta-Properties (Metaprogramming)

Understanding **meta-properties** in Python — often referred to as **metaprogramming** — empowers you to write code that can inspect, modify, or generate other code dynamically. This is especially useful in building frameworks, automation tools, and developer utilities.

---

### 🔧 What Are Meta-Properties?

Meta-properties are mechanisms that allow **code to manipulate the behavior or structure of classes and objects** at runtime. Python is particularly powerful in this domain due to its flexible type system and support for runtime introspection and modification.

---

### ⚙️ Core Meta-Programming Tools

#### ✅ `type()` as a Dynamic Class Constructor

You can use the `type()` function to dynamically create classes:

```python
MyClass = type("MyClass", (object,), {"greet": lambda self: "Hello!"})
obj = MyClass()
print(obj.greet())  # Hello!
```

#### ✅ Metaclasses

Metaclasses are **classes of classes** — they define how classes behave. If you want to automatically inject, validate, or alter class properties at definition time, metaclasses are the tool.

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['category'] = 'dynamic'  # Inject a new class attribute 'category' into the class namespace
        return super().__new__(cls, name, bases, dct)

class DynamicRobot(metaclass=Meta):
    pass

print(DynamicRobot.category)  # dynamic
```

#### ✅ Attribute Control Hooks

- `__getattr__`, `__setattr__`, and `__delattr__` let you control how attributes are accessed, set, or deleted.

```python
class AutoLogger:
    def __setattr__(self, name, value):
        print(f"Setting {name} = {value}")
        super().__setattr__(name, value)

obj = AutoLogger()
obj.speed = 100  # Setting speed = 100
```

#### ✅ Decorators

Decorators wrap or modify functions, methods, or even entire classes, enabling injection of additional behavior (e.g., logging, validation, memoization).

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def greet():
    return "Hi"

print(greet())  # Calling greet \n Hi
```

---

### 🧠 Bonus: Introspection Powers Metaprogramming

Python’s introspection tools make meta-programming easier by allowing real-time inspection of object properties.

```python
print(type(obj))      # See what class an object belongs to
print(dir(obj))       # See available attributes and methods
print(getattr(obj, 'speed', 'N/A'))  # Dynamically access properties
```

---

### 🚀 Why Use Meta-Programming?

- Build reusable and dynamic frameworks
- Automate boilerplate (e.g., class registration, validation)
- Extend or wrap third-party classes without modifying them
- Enable plugin systems, serialization layers, and adaptive APIs

Used well, meta-properties help you write **flexible**, **scalable**, and **powerful** code.


