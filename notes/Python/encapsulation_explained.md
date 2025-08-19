# Encapsulation in Object-Oriented Programming (OOP)

---

## What is Encapsulation?

Encapsulation is a core concept in object-oriented programming that involves:

### 1. **Bundling Data and Behavior**

Encapsulation means grouping related data (variables) and the operations (methods) that manipulate that data into a single unit, which helps in organizing code logically and makes maintenance easier by keeping related logic together. typically a class.

> **Analogy**: Like a medical device module that contains both its sensors (data) and its internal logic (functions) inside one physical enclosure.

### 2. **Restricting Direct Access to Internal State**

Encapsulation protects the internal state of an object by preventing external access and modification. Access to internal data is typically done through well-defined interfaces like getter and setter methods, which also allow validation and error handling, adding robustness to the code.

> **Analogy**: Just as hospital technicians interact with a medical device through its UI rather than accessing its circuit board, code should interact with an object through public methods rather than manipulating internal data directly.

---

## Key Concepts

### Access Modifiers (in languages like Python, Java, C++)

*Note: In Python, access control is enforced by naming conventions (like **`_protected`** or **`__private`**) rather than strict compiler rules, unlike in Java or C++ which have formal access modifiers.*

- **Private** (`__variable`): Can only be accessed inside the class.
- **Public**: Can be accessed from outside the class.
- **Protected** (`_variable`): Accessible within the class and subclasses.

---

## Python Example (Encapsulation in Action)

```python
# This class demonstrates encapsulation by hiding its internal state
# and providing controlled access through public methods
class DiagnosticTool:
    def __init__(self):
        self.__calibration_code = "ABC123"  # private attribute (encapsulated data)

    def get_calibration_code(self):
        # public getter method (interface to access private data)
        return self.__calibration_code

    def set_calibration_code(self, new_code):
        # public setter method with validation (encapsulation logic)
        if isinstance(new_code, str) and len(new_code) == 6:
            self.__calibration_code = new_code
        else:
            raise ValueError("Invalid calibration code")
```

This design hides `__calibration_code` from direct access and ensures that any change to it must go through validation, preventing accidental or malicious modifications from outside the class.

---

## Lithography and FBX Example (Encapsulation in Action)

*Lithography-based rendering refers to a technique that simulates the process of patterning layers on microfabricated surfaces, often used in semiconductor or precision 3D printing workflows. In digital tools, it may involve organizing and visualizing asset layers with strict control for downstream processes.* Here's an example of encapsulation using a system that manages 3D FBX assets in a lithography-based rendering pipeline:

```python
# Encapsulation used to protect and manage FBX asset metadata
class FBXAsset:
    def __init__(self, file_path):
        self.__file_path = file_path  # private attribute
        self.__layer_data = {}        # private attribute to store lithographic layer info

    def add_layer(self, layer_name, params):
        # Public method with validation to add or update lithography layers
        if isinstance(layer_name, str) and isinstance(params, dict):
            self.__layer_data[layer_name] = params
        else:
            raise ValueError("Invalid layer input")

    def get_layer(self, layer_name):
        # Controlled access to layer data
        return self.__layer_data.get(layer_name, None)

    def export_asset_metadata(self):
        # Expose encapsulated metadata safely
        return {
            "file_path": self.__file_path,
            "layers": dict(self.__layer_data)
        }
```

This class encapsulates sensitive metadata about FBX assets and provides safe, validated interfaces for interacting with it—ideal for ensuring pipeline integrity and preventing corruption in downstream tools.python

# Encapsulation used to protect the balance of a bank account

class BankAccount: def **init**(self, owner, balance=0): self.owner = owner self.\_\_balance = balance  # private attribute

```
def deposit(self, amount):
    if amount > 0:
        self.__balance += amount
    else:
        raise ValueError("Deposit amount must be positive")

def withdraw(self, amount):
    if 0 < amount <= self.__balance:
        self.__balance -= amount
    else:
        raise ValueError("Invalid withdrawal amount")

def get_balance(self):
    return self.__balance
```

```
This class encapsulates the account balance, ensuring it can only be modified through validated operations like deposit and withdrawal, thus protecting against invalid transactions.python
# Encapsulation shown by keeping metadata private and exposing
# functionality through controlled methods only
class CharacterProfile:
    def __init__(self):
        self.__metadata = {}  # private metadata store (encapsulated)

    def update_trait(self, trait, value):
        # Public method to modify internal state safely
        self.__metadata[trait] = value

    def export_traits(self):
        # Public method to access internal state safely
        return dict(self.__metadata)
```

This design keeps the `__metadata` dictionary encapsulated, allowing updates and access only through defined methods.

---

## Why Encapsulation Matters

- **Reliability**: Prevents unintended interference with object internals.
- **Control**: Enforces rules and validation.
- **Maintainability**: Internals can change without affecting external code.
- **Clean Interfaces**: Easier collaboration and testing.

Encapsulation is essential for building robust, modular, and scalable software.

